from sqlalchemy import Integer, String, Column
from database import Base

class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)