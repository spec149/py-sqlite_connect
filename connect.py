# -*- coding: utf-8 -*-
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = qslite3.connect(path)
        print('yay działa')
    except Error as e:
        print(f'The erroe '{e}' occurred')

    return connection

select_users = "SELECT * FROM invoice WHERE "
users = execute_read_query(connection, select_users)

for user in users:
    print(user)
