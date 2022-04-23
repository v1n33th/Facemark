from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    time_log: datetime
    
    
class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    user_id: int
    in_out: int    #   1- Int and 2 - Out
    
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    is_active: bool
    first_name: str
    last_name: str
    middle_name: Optional[str]
    department: Optional[str]
    position: Optional[str]


#class UserCreate(UserBase):
   # password: str

class UserCreate(UserBase):
   pass


class User(UserBase):
    emp_id: int
    items: List[Item] = []

    class Config:
        orm_mode = True

class ReturnTime(BaseModel):
    user_id: int
    name: str
    time: Optional[datetime]
    punchIn: Optional[datetime]
    punchOut: Optional[datetime]        
