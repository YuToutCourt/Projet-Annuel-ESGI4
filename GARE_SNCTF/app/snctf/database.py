import sqlite3

class DataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def getTrain(self, uuid):
        cursor = self.conn.cursor()
        cursor.execute(f'''
            SELECT * FROM train WHERE uuid = '{uuid}'
        ''')
        train = cursor.fetchone()
        cursor.close()
        return train


    def getTrains(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT * FROM train where private == 0
        ''')
        trains = cursor.fetchall()
        cursor.close()

        return trains