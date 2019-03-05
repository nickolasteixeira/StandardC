#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
import models
from os import getenv


class DBStorage:
    '''Create SQLalchemy database'''
    __engine = None
    __session = None

    def __init__(self):
        '''Create engine and link to MySQL databse (dev_db) '''
        user = getenv("MYSQL_USER")
        pwd = getenv("MYSQL_PWD")
        host = getenv("MYSQL_HOST")
        db = getenv("MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)
        

    def all(self, cls):
        '''Query current database session'''
        db_dict = {}

        objs = self.__session.query(models.classes.get(cls)).all()
        print("OBJS IN ALL", objs)
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            db_dict[key] = obj
        return db_dict


    def new(self, obj):
        '''Add object to current database session'''
        self.__session.add(obj)


    def save(self):
        '''Commit all changes of current database session'''
        self.__session.commit()


    def reload(self):
        self.__session = Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))

    
    def get(self, cls, amount):
        '''Retreives one object based on class and amount'''
        if not cls or not amount:
            return None

        cls_dict = self.all(cls)
        fetch = "{}.{}".format(cls, amount)
        print("FETCH", fetch)
        return cls_dict.get(fetch)


