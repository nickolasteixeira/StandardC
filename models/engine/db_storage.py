#!/usr/bin/python3
'''
    Define class DatabaseStorage
'''
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models

class DBStorage:
    '''
        Create SQLalchemy database
    '''
    __engine = None
    __session = None

    def __init__(self):
        '''
            Create engine and link to MySQL databse (dev_db)
        '''
        user = getenv("MYSQL_USER")
        pwd = getenv("MYSQL_PWD")
        host = getenv("MYSQL_HOST")
        db = getenv("MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)


    def all(self, cls):
    '''
        Query current database session
    '''
    db_dict = {}

    objs = self.__session.query(models.classes.get(cls)).all()
    for obj in objs:
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        db_dict[key] = obj
    return db_dict

