import sqlite3
import datetime
import uuid
from random import randint, choice
import string


from itertools import *
from tqdm import tqdm


def connectToDatabase():
    conn = sqlite3.connect('db.sqlite3')
    return conn

def createTable(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS train (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid VARCHAR(36) NOT NULL,
            name VARCHAR(30) NOT NULL,
            voie VARCHAR(10) NOT NULL,
            wagon VARCHAR(30) NOT NULL,
            date VARCHAR(30) NOT NULL,
            heure VARCHAR(5) NOT NULL,
            cargaison VARCHAR(16) NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    

def insertTrain(conn, uuid, name, voie, wagon, date, heure, cargaison, private):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO train (uuid, name, track, wagon, date, hour, freight, private)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (uuid, name, voie, wagon, date, heure, cargaison, private))
    conn.commit()
    cursor.close()


def deleteTrain(conn, uuid):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM train WHERE id = ?
    ''', (uuid,))
    conn.commit()
    cursor.close()


def getTrains(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM train
    ''')
    trains = cursor.fetchall()
    cursor.close()
    return trains


def random_list_day(n):
    def random_date():
        return datetime.datetime(randint(2018, 2024), randint(1, 12), randint(1, 28))
    return [datetime.datetime.strftime(random_date() - datetime.timedelta(days=x), '%Y-%m-%d') for x in range(n)]


def random_hour_str():
    return f"{randint(0, 23)}:{str(randint(0, 00)).zfill(2)}"


def random_freight():
    return choice(["OR", "CUIVRE", "ARGENT", "TOPAZE", "AMETHYSTE", "ONYX","IVOIRE", "CHENE", "ERABLE",  "BAMBOU", "ROSEAU", "OSIER"])


def random_track():
    return f"{randint(1, 3)}{choice(string.ascii_uppercase[:3])}"

def random_wagon():
    return f"{choice(string.ascii_uppercase[:3])}{randint(1, 4)}"

print("Deleting all trains...")
#delete all trains
for train in tqdm(getTrains(connectToDatabase())):
    deleteTrain(connectToDatabase(), train[0])
print("Done.")


random_date_list = random_list_day(15)


print("Adding new trains...")
with open("./nom_train.txt", "r") as f:
    names = f.read().split("\n")

    for _ in tqdm(range(10_000)):
        insertTrain(connectToDatabase(), 
                    str(uuid.uuid4()), choice(names), 
                    random_track(), random_wagon(), 
                    choice(random_date_list), 
                    random_hour_str(), 
                    random_freight(), 
                    randint(0, 1)
                )
print("Done.")



