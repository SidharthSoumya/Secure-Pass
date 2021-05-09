from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:happy@localhost:5432/secure-pass')

JWT_SECRET_KEY = 'myjwtsecretkey'

Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()
