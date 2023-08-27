from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import environ as env


engine = create_engine(env["CONNECTION_STRING"])
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()
