from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import sqlalchemy
import pandas as pd
import csv

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def running():
    ServerName = 'DESKTOP-CN8MUQ4' #Change to Your Server
    InstanceName = '' #Change to your Instance Name
    DatabaseName = 'gudang'

    df = []

    MSSQLengine = sqlalchemy.create_engine('mssql+pyodbc://' + ServerName + "\\" + InstanceName + '/' + DatabaseName + '?driver=SQL+Server+Native+Client+11.0')
    print(str(MSSQLengine))

    with MSSQLengine.connect() as con:
        rs = con.execute('SELECT TOKO,RTYPE,TANGGAL1,PRDCD,QTY,PRICE FROM MSTXHG12')

        for row in rs:
            df.append(row)

    return render_template('index.html', value=df)

if __name__ == '__main__':
   app.run()