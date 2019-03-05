#!/usr/bin/python3
'''
    Implementation of the StandardC class
'''
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
import models

class StandardC(BaseModel):
    '''
        Implementation for the State.
        Create relationship between class State (parent) to City (child)
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


