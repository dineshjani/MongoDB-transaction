import collections
from ..dbconnection import Connection

def update_student(data):
    get_collection=Connection.get_instance().student.section
    documents={"name":data.Name,"age":data.Age,"gender":data.Gender,"address":data.Address}
    print(get_collection)
    get_collection.update({"name":data.Name},{"$set":{"name":data.Name,"age":data.Age,"gender":data.Gender,"address":data.Address}},upsert=True) 