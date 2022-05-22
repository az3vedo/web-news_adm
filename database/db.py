from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database.engine import db_engine

Base = declarative_base()

class Login(Base):
  __tablename__ = "login"
  id = Column(Integer, primary_key=True)
  email = Column(String(80), nullable=False)
  senha = Column(String(80), nullable=False)


Base.metadata.create_all(db_engine)
