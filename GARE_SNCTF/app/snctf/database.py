import sqlite3
from .trains import Train


class DataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def getTrain(self, name):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            SELECT * FROM train WHERE private == 0 and name LIKE '%{name}%'
        ''')
        db_train = cursor.fetchall()
        cursor.close()
        
        if len(db_train) == 0:
            return []
        
        train = [Train(train[0], train[1], train[2], train[3], train[4], train[5], train[6], train[7], train[8]) for train in db_train]
        return train
        




    def getTrains(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM train where private == 0
        ''')
        db_trains = cursor.fetchall()
        cursor.close()

        if len(db_trains) == 0:
            return []
        
        trains = [Train(train[0], train[1], train[2], train[3], train[4], train[5], train[6], train[7], train[8]) for train in db_trains]
        return trains