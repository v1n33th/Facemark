from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, time, timedelta

from database import Base


class User(Base):
    __tablename__ = "users"

    emp_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    middle_name = Column(String, index=True)
    department = Column(String, index=True)
    position = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    timelog = relationship("TimeLog", back_populates="user")


class TimeLog(Base):
    __tablename__ = "timelog"

    id = Column(Integer, primary_key=True, index=True)
    time_log = Column(DateTime, default=datetime.utcnow)
    in_out = Column(Integer, index=True)
    user_id = Column(Integer, ForeignKey("users.emp_id"))

    user = relationship("User", back_populates="timelog")

