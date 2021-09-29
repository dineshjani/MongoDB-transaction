import collections
from ..dbconnection import Connection

def delete_student(data):
    get_collection=Connection.get_instance().student.section
    get_collection.delete_many(data) 
