from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import sqlalchemy as sql
import pandas as pd
import pypyodbc
import csv
import pyodbc
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def running():

    df = []
    df1 = []

    # USING MYSQL.CONNECTOR
    mydb = mysql.connector.connect(host="192.168.59.221", user="root", passwd="12345678", database="ic")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT toko.TOKO, MSTXHG.TANGGAL1, MSTXHG.PRDCD, plu_igr.DESC, COUNT(MSTXHG.PRDCD) AS JUMLAH_BARANG FROM toko JOIN MSTXHG ON toko.TOKO=MSTXHG.TOKO JOIN plu_igr ON plu_igr.PRDCD=MSTXHG.PRDCD WHERE MSTXHG.TANGGAL1='2021-12-17' AND toko.TOKO='F2LV' GROUP BY plu_igr.PRDCD")
    rs = mycursor.fetchall()

    for row in rs:
        df.append(row)

    df1 = pd.DataFrame(df)
    header = list(df1.columns.values)

    return render_template('index.html', value=df, header=header)

# @app.route("/laporan1", methods=['POST', 'GET'])
# def running1():

#     df = []
#     df1 = []

#     # USING PYPYODBC
#     connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-CN8MUQ4;Database=gudang;uid=;pwd=')# Creating Cursor    
#     cursor = connection.cursor()    

#     rs = cursor.execute("SELECT RTYPE, TANGGAL1, PRDCD, QTY FROM dbo.MSTXHG12")

#     for row in rs:
#         df.append(row)

#     df1 = pd.DataFrame(df)
#     header = list(df1.columns.values)

#     return render_template('index.html', value=df, header=header)

# @app.route("/laporan2", methods=['POST', 'GET'])
# def running2():

#     df = []
#     df1 = []

#     # USING PYPYODBC
#     connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-CN8MUQ4;Database=gudang;uid=;pwd=')# Creating Cursor    
#     cursor = connection.cursor()    

#     rs = cursor.execute("SELECT TANGGAL1, PRDCD, QTY FROM dbo.MSTXHG12")

#     for row in rs:
#         df.append(row)

#     df1 = pd.DataFrame(df)
#     header = list(df1.columns.values)

#     return render_template('index.html', value=df, header=header)

# @app.route("/laporan3", methods=['POST', 'GET'])
# def running3():

#     df = []
#     df1 = []

#     # USING PYPYODBC
#     connection = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-CN8MUQ4;Database=gudang;uid=;pwd=')# Creating Cursor    
#     cursor = connection.cursor()    

#     rs = cursor.execute("SELECT TANGGAL1, PRDCD, QTY FROM dbo.MSTXHG12")

#     for row in rs:
#         df.append(row)

#     df1 = pd.DataFrame(df)
#     header = list(df1.columns.values)

#     return render_template('index.html', value=df, header=header)


if __name__ == '__main__':
   app.run()