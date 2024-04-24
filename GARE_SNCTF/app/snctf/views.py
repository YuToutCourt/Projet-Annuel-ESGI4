import json
import sqlite3
import requests

from django.shortcuts import render
from django.http import JsonResponse
from .database import DataBase
from icecream import ic

ic.configureOutput(prefix='DEBUG: ')

def index(request):

    if request.method == "GET":

        nom = request.GET.get('name')

        if nom: 
            r = requests.get("http://localhost:8000/api/train?name=" + nom)
            data = r.json().get("train")
            ic(data)

            return render(request, 'index.html', context={"data": data})
        
        else:

            r = requests.get("http://localhost:8000/api/trains")
            data = r.json().get("trains")

            if not data: data = []

            return render(request, 'index.html', context={"data": data})


def connectToDatabase():
    conn = sqlite3.connect('db.sqlite3')
    return conn


def get_all_trains(request):
    
    if request.method != "GET":
        return JsonResponse({"message": "GET request required."}, status=403)

    dbo = DataBase("db.sqlite3")

    trains = dbo.getTrains()

    return JsonResponse({
        "trains": [train.__dict__ for train in trains]
    }, status=200)



def get_train_by_uuid(request):

    if request.method != "GET":
        return JsonResponse({"message": "GET request required."}, status=403)

    name = request.GET.get('name')

    dbo = DataBase("db.sqlite3")

    train = dbo.getTrain(name)

    if train == None:
        return JsonResponse({"message": "Train not found."}, status=404)

    ic(train)

    return JsonResponse({
        "train": [t.__dict__ for t in train]
    }, status=200)