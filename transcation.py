from typing import Collection
from pymongo import MongoClient
import pymongo
connection= pymongo.MongoClient("mongodb+srv://dinesh:dinesh@cluster0.ln2gw.mongodb.net/test")
with connection.start_session() as session:
    with session.start_transaction():
        try:

            practiceCollection=connection['paxcom']['practice']
            practiceCollection.insert_many([{ "_id": 219,"name":"ravi"},{"_id":5,"name":"parkash"},{"_id":259,"name":"ram"}],session=session)
           
        except Exception as e:
            print(e)
            print("An exception occurred")
            session.abort_transaction
            session.end_session
        else:
            print("no error occured")
            session.commit_transaction
            session.end_session


        
