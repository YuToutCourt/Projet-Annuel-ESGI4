import json
import sqlite3
import requests

from django.shortcuts import render
from django.http import JsonResponse
from .database import DataBase


def index(request):

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

    trains_with_keys = [{"id": train[0], "uuid": train[1], "name": train[2], "track": train[3], "wagon": train[4], "date": train[5], "hour": train[6], "freight": train[7]} for train in trains]

    return JsonResponse({"trains": trains_with_keys}, status=200)



def get_train_by_uuid(request):

    if request.method != "GET":
        return JsonResponse({"message": "GET request required."}, status=403)

    uuid = request.GET.get('uuid')

    dbo = DataBase("db.sqlite3")

    print(uuid)

    train = dbo.getTrain(uuid)

    if train == None:
        return JsonResponse({"message": "Train not found."}, status=404)
    
    train_with_keys = {"id": train[0], "uuid": train[1], "name": train[2], "track": train[3], "wagon": train[4], "date": train[5], "hour": train[6], "freight": train[7]}

    return JsonResponse({"train": train_with_keys}, status=200)