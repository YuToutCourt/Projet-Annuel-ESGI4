import sqlite3
import datetime
import uuid
from random import randint, choice
import string


from itertools import *


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



def update_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        ALTER TABLE train ADD COLUMN private BOOLEAN DEFAULT 0;
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



def getTrain(conn, uuid):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM train WHERE uuid = ?
    ''', (uuid,))
    train = cursor.fetchone()
    cursor.close()
    return train


def getTrains(conn):
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM train
    ''')
    trains = cursor.fetchall()
    cursor.close()
    return trains


def random_date():
    return datetime.datetime(randint(2018, 2024), randint(1, 12), randint(1, 28))

# update_table(connectToDatabase())

date_str_list = [datetime.datetime.strftime(random_date() - datetime.timedelta(days=x), '%Y-%m-%d') for x in range(2000)]


# insertTrain(connectToDatabase(), str(uuid.uuid4()), 'express', 'voie3', 'uWugon', date_str_list[1], '12:00', 'CUIVRE', 1)
# print(date_str_list)
# insertTrain(connectToDatabase(), str(uuid.uuid4()), 'train2', 'voie2', 'wagon2', date_str_list[1], '12:00', 'OR', 1)
# print(getTrains(connectToDatabase()))
# deleteTrain(connectToDatabase(), '1')


def random_hour_str():
    return f"{randint(0, 23)}:{randint(0, 59)}"


def random_freight():
    return choice(["OR", "CUIVRE", "ARGENT", "PLATINE", "DIAMANT", "RUBIS", "EMERAUDE", "SAPHIR", "TOPAZE", "AMETHYSTE", "PERLE", "JADE", "OPALE", "ONYX", "AGATE", "MALACHITE", "LAPIS-LAZULI", "TURQUOISE", "CORAIL", "NACRE", "IVOIRE", "EBENE", "ACAJOU", "PALISSANDRE", "CHENE", "ERABLE", "NOYER", "MERISIER", "BAMBOU", "ROSEAU", "OSIER", "JONC", "BAMBIN", "SAULE", "TILLEUL", "PEUPLIER", "CHARME", "HETRE", "CHATAIGNIER"])


def random_track():
    return f"{randint(1, 10)}{choice(string.ascii_uppercase)}"

def random_wagon():
    return f"{randint(1, 100)}{choice(string.ascii_uppercase)}"


with open("./nom_train.txt", "r") as f:
    names = f.read().split("\n")

    for _ in range(10_000):
        insertTrain(connectToDatabase(), 
                    str(uuid.uuid4()), choice(names), 
                    random_track(), random_wagon(), 
                    choice(date_str_list), 
                    random_hour_str(), 
                    random_freight(), 
                    randint(0, 1)
                )

    
