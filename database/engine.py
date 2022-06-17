from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
db_engine = create_engine("mysql+pymysql://root:12345@localhost:3307/web-news-adm", echo=True)

Session = sessionmaker(bind=db_engine)
db_session= Session()