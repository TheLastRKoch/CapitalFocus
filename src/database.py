from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import environ as env

# Load .env file
load_dotenv()

engine = create_engine(env["DB_CONNECTION_STRING"])
Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()
