#!/usr/bin/python3
'''
    Implementation of a User class
'''
from sqlalchemy import Column, String, Boolean, create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from os import getenv

class User(BaseModel, Base):
    '''
        Implementation of a User Class
    '''
    
    __tablename__ = "users"

    username = Column(String(60), nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(60), nullable=False)
    verified = Column(Boolean, nullable=False, default=False)

    @classmethod
    def emailExists(self, email):
        user = getenv("MYSQL_USER")
        pwd = getenv("MYSQL_PWD")
        host = getenv("MYSQL_HOST")
        db = getenv("MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        self.__session = Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

        email = self.__session.query(self).filter_by(email=email).all()
        self.__session.remove()
        return email
