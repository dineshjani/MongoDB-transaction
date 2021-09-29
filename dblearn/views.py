from django.shortcuts import render
from django.http import HttpResponse
from .Models.models import Student
from .Operations import insert_student
from .Operations import update_student
from .Operations import delete_student
from .Operations import find_student
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.
@csrf_exempt
def get_view(request):
    data = json.load(request)  
    result= find_student(data)
    return HttpResponse(result)
        
@csrf_exempt
def insert_view(request):
    data = json.load(request)
    print(type(data))
    if not isinstance(data,list):
        data=[data]    
    for student in data:
        student_obj=Student(student)
        insert_student(student_obj)

    return HttpResponse("inserted succesfully")
@csrf_exempt
def delete_view(request):
    data = json.load(request)  
    delete_student(data)
    return HttpResponse("deleted succesfully")
    
@csrf_exempt
def update_view(request):
    data = json.load(request)
    student_obj=Student(data)
    update_student(student_obj)
    return HttpResponse("updated succesfully")
    



