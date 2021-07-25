# dbconnection
from logging import exception
import mysql.connector as CON


class mysqlconnection:
    message = ""

    try:
        @staticmethod
        def connect():
            connection = CON.connect(
                host="127.0.0.1",
                port='3306',
                user="root",
                password="root",
                database="python"
            )
            if connection.is_connected():
                mysqlconnection.message = "Connected Successfully"
                return connection
    except Exception as e:
        mysqlconnection.message = e

    @staticmethod
    def Close(self, Connection):
        Connection.close()


# mysqlconnection.connect()
# print(mysqlconnection.message)
