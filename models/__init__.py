#!/usr/bin/python3
'''
    Pacakge initializer
'''

from models.engine import db_storage
from models.standardc import StandardC
from models.user import User

storage = db_storage.DBStorage()

classes = {
    "StandardC" : StandardC,
    "User"      : User
}

storage.reload()

