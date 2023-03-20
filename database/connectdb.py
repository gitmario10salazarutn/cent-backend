# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 15:53:32 2023

@author: Mario
"""

import psycopg2 as conn
from decouple import config


def connect_postgresql(hostname, dbname, username, password):
    try:
        conn_query = "host = '" + hostname + "' dbname = '" + dbname + "' user= '" + username + "' password= '" + password + "' port = '5432'"
        conn_post = conn.connect(conn_query)
        print("Database connect successfully to PostgreSQL")
        return conn_post
    except Exception as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        raise Exception(e)

def get_connection():
    try:
        connection = connect_postgresql(
            config('HOSTNAME'),
            config('DATABASE'),
            config('USER_NAME'),
            config('PASSWORD')
        )
        return connection
    except Exception as ex:
        raise ex
