from typing import List
from datetime import datetime

## testing the push code
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import crud
import schemas
import models

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/in_out/{in_out}", response_model=schemas.Item)
def create_timelog_for_user(
    user_id: int, in_out: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    if in_out!=1 and in_out !=2:
        raise HTTPException(status_code=400, detail="Invalid input for in_out")
    return crud.create_user_timelog(db=db, item=item, user_id=user_id, in_out=in_out)


@app.get("/users/timelog/", response_model=List[schemas.Item])
def read_timelog(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/users/timesheet/{start_date}/{end_date}", response_model=List[schemas.ReturnTime])
def view_timesheet(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    db_user = crud.get_timelog_date(db, start_date=start_date, end_date=end_date)
    if db_user is None:
        raise HTTPException(status_code=404, detail="No Records Found")
    return db_user    
