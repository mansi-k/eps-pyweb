from flask import Flask
import cx_Oracle

def connectDB():
    con = cx_Oracle.connect('system/mansik123@127.0.0.1/XE')
    cur = con.cursor()
    return con, cur

def zip_data(cursor, rows):
    columns = [i[0].lower() for i in cursor.description]
    return [dict(zip(columns, row)) for row in rows]

