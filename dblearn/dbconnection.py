from typing import Collection
from pymongo import MongoClient
import pymongo

class Connection:
    __instance = None
   
    def __init__(self):
        pass

    @staticmethod
    def get_instance():
        instance=Connection.__instance
        if instance is None:
            
            Connection.__instance= pymongo.MongoClient("mongodb://localhost:27017",maxPoolSize=10)
            
            return Connection.__instance
        else:
            return  Connection.__instance




        



