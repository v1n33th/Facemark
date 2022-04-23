from sqlalchemy.orm import Session
from datetime import datetime
from sqlalchemy import and_, or_, not_
from copy import deepcopy

import schemas
import models
from schemas import ReturnTime


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
                         email=user.email, first_name=user.first_name, last_name=user.last_name,
                         middle_name=user.middle_name, department=user.department, position=user.position
                         )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TimeLog).offset(skip).limit(limit).all()


def create_user_timelog(db: Session, item: schemas.ItemCreate, user_id: int, in_out):
    db_item = models.TimeLog(**item.dict(), user_id=user_id, in_out=in_out)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
  
def get_timelog_date(db: Session, start_date:datetime, end_date:datetime):
    # print(start_date)
    start_date = start_date.date()
    end_date = end_date.date()
    # print(start_date)
    # a = db.query(models.TimeLog).filter(models.TimeLog.user_id == 4 and models.TimeLog.time_log > start_date).all()
    a = db.query(models.TimeLog).filter(and_(models.TimeLog.time_log > start_date, models.TimeLog.time_log < end_date)).all()
    result={}
    for i in a:
        key=getKey(i)
        if(key in result):
            newObj=result[key]
        else:
            newObj=createNewObjectFromTimeLog(i)    
                    
        if i.in_out==1 and (not "punchIn" in newObj or newObj["punchIn"]>i.time_log):
            newObj["punchIn"]=i.time_log

        if i.in_out==2 and (not "punchOut" in newObj or newObj["punchOut"]<i.time_log):
            newObj["punchOut"]=i.time_log
        result[key]=newObj
    # print(result)
    list_values = []
    for key, value in zip(result.keys(),result.values()):
        print(key, value["punchIn"])
        user_name = db.query(models.User.first_name,models.User.middle_name, models.User.last_name).filter(models.User.emp_id == value["user_id"]).first()
        if(user_name.middle_name):
            name = user_name.first_name+" "+user_name.middle_name+" "+user_name.last_name
        else:   
             name = user_name.first_name+" "+user_name.last_name

        list_values.append({
            "user_id": value["user_id"], 
            "name": name, 
            "time": value["time_log"], 
            "punchIn": value["punchIn"], 
            "punchOut" : value["punchOut"]
        })   
   
    return list_values

def getKey(i):
    return str(i.user_id)+"-"+str(i.time_log.date())

def createNewObjectFromTimeLog(i):
    return {
    "time_log": i.time_log,
    "id": i.id,
    "user_id": i.user_id,
    "in_out": i.in_out
  }
