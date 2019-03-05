#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime


Base = declarative_base()


class BaseModel:
    '''Base class for other classes to inherit from'''
    
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, **kwargs):

        for attr, val in kwargs.items():
            setattr(self, attr, val)

        setattr(self, 'id', str(uuid4()))
        setattr(self, 'created_at', datetime.utcnow())
        setattr(self, 'updated_at', datetime.utcnow())


    def save(self):
        '''
            Update the updated_at attribute with new.
        '''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

