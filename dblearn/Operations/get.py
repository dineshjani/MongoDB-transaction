import collections
from ..dbconnection import Connection

def find_student(data):
    get_collection=Connection.get_instance().student.section
    return get_collection.find(data) 