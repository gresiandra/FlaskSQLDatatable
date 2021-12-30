from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlalchemy as sql
import pandas as pd
import pypyodbc
import pyodbc
import csv

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def running():

    df = []
    df1 = []

    # USING PYODBC
    # conn = pyodbc.connect('Driver={SQL Server};'
    #                   'Server=DESKTOP-CN8MUQ4;'
    #                   'Database=gudang;'
    #                   'UID=;'
    #                   'PWD=;')
    # cursor = conn.cursor()
    
    # USING MSSQLENGINE/SQLALCHEMY
    # ServerName = 'DESKTOP-CN8MUQ4' #Change to Your Server
    # InstanceName = '' #Change to your Instance Name
    # DatabaseName = 'gudang'

    # MSSQLengine = sql.create_engine('mssql+pyodbc://' + ServerName + "\\" + InstanceName + '/' + DatabaseName + '?driver=SQL+Server+Native+Client+11.0')
    # print(str(MSSQLengine))

    # with MSSQLengine.connect() as con:
    #     rs = con.execute('SELECT TOKO,RTYPE,TANGGAL1,PRDCD,QTY,PRICE FROM MSTXHG12')

    #     for row in rs:
    #         df.append(row)


    # USING PYPYODBC
    connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-CN8MUQ4;Database=gudang;uid=;pwd=')# Creating Cursor    
    cursor = connection.cursor()    

    rs = cursor.execute("SELECT * FROM MSTXHG12")

    for row in rs:
        df.append(row)

    # df1 = pd.DataFrame(df)
    # header = list(df1.columns.values)

    rs1 = cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='MSTXHG12'")
    
    for row1 in rs1:
        df1.append(row1) 

    return render_template('index.html', value=df, header=df1)

if __name__ == '__main__':
   app.run()