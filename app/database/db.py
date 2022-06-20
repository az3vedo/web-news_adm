from contextlib import closing
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from database.engine import db_engine, db_session
from flask_login import UserMixin

Base = declarative_base()

class Login(UserMixin, Base):
  __tablename__ = "login"
  id = Column(Integer, primary_key=True)
  userName = Column(String(80), nullable=False)
  senha = Column(String(80), nullable=False)

Base.metadata.create_all(db_engine)

# with closing(db_session):
#   admin = Login(userName='admin', senha='admin')
#   db_session.add(admin)
#   db_session.commit()