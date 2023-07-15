import os
import mysql.connector


connection = None
cursor = None


def connect():
    global connection
    global cursor
    connection = mysql.connector.connect(
        host=os.environ["HOST"],
        database=os.environ["DATABASE"],
        user=os.environ["USER"],
        password=os.environ["PASSWORD"],
    )
    cursor = connection.cursor()


def close():
    cursor.close()
    connection.close()


def select_photos(uid):
    cursor.execute(f"SELECT * FROM photos WHERE uid = '{uid}';")
    return [
        {
            "id": row[0],
            "uid": row[1],
            "name": row[2],
            "content_type": row[3],
            "src": row[4],
            "labels": row[5],
            "word2vec": row[6],
        }
        for row in cursor
    ]
