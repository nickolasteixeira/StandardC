#!/usr/bin/python3
'''
    Implementation of the StandardC class
'''
from sqlalchemy import Column, String, Integer, DateTime, Float
from uuid import uuid4, UUID
from datetime import datetime
import models
from models.base_model import BaseModel, Base


class StandardC(BaseModel, Base):
    '''
        Implementation for the StandardC.
    '''

    __tablename__ = "standardc_math"

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    a = Column(Integer, nullable=False)
    b = Column(Integer, nullable=False)
    c = Column(Integer, nullable=False)
    d = Column(Integer, nullable=False)
    x = Column(Integer, nullable=False)
    y1 = Column(Integer, nullable=False)
    y2 = Column(Float, nullable=False)
    y3 = Column(Float, nullable=False)



    '''
    def __init__(self, **kwargs):
        #user = getenv("MYSQL_USER")
        #pwd = getenv("MYSQL_PWD")
        #host = getenv("MYSQL_HOST")
        #db = getenv("MYSQL_DB")
        #self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        #    user, pwd, host, db), pool_pre_ping=True)

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            "dev", "dev_pwd", "localhost", "dev_db"), pool_pre_ping=True)

        for attr, val in kwargs.items():
            setattr(self, attr, val)

        setattr(self, 'id', str(uuid4()))
        setattr(self, 'created_at', datetime.utcnow())
        setattr(self, 'updated_at', datetime.utcnow())

        print("engine", self.__engine)

    def all(self, cls):
        db_dict = {}

        objs = self.__session.query(models.classes.get(cls)).all()
        for obj in objs:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            db_dict[key] = obj
        return db_dict

    
    def save(self):
        print("Committing...")
        self.__session.commit()


    def new(self, obj):
        self.__session.add(obj)

    def reload(self):
        Base.metadata.create_all(bind=self.__engine)
        self.__session = scoped_session(
            sessionmaker(
                bind=self.__engine,
                expire_on_commit=False))
        print("SESSION", self.__session)
    '''
