#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from sqlalchemy import create_engine, MetaData, desc
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

    
    def getNewest(self, cls, amount):
        '''Retreives newest objects based on class and amount'''
        if not cls or not amount:
            return None

        entity = models.classes.get(cls)
        newest_obj = self.__session.query(entity).order_by(desc(entity.updated_at)).limit(amount).all()
        return newest_obj

    def getBetweenDate(self, cls, date1, date2):
        '''Retereives objects between two dates'''
        if not cls or not date1 or not date2:
            return None

        entity = models.classes.get(cls)
        dates = self.__session.query(entity).filter(entity.updated_at.between(date1, date2))
        return dates

    def to_json(self, all_objs):
        if not all_objs:
            return None

        array = []
        for v in all_objs:
            new_dict  = {}
            arr = [a for a in dir(v) if not a.startswith('_') and not callable(getattr(v,a)) and not a.startswith('meta')]
            for item in arr:
                new_dict[item] = getattr(v, item)
            array.append(new_dict)

        return {"all items": array}

