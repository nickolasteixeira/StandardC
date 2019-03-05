#!/usr/bin/python3
'''
    Pacakge initializer
'''

from models.engine import db_storage
from models.standardc import StandardC

storage = db_storage.DBStorage()

classes = {"StandardC": StandardC}

storage.reload()

print("RELOAD FROM INIT", storage.reload())
