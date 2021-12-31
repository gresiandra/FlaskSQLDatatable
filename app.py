from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask, render_template, request
import pandas as pd
import mysql.connector

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def running():

    df = []
    df1 = []

    # USING MYSQL.CONNECTOR
    mydb = mysql.connector.connect(host="192.168.59.221", user="root", passwd="12345678", database="ic")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT MSTXHG.TOKO, toko.NAMA, count(MSTXHG.PRDCD)as BARANG_BERMASALAH FROM MSTXHG join toko on MSTXHG.TOKO=toko.TOKO group by MSTXHG.TOKO order by count(MSTXHG.PRDCD) desc")
    rs = mycursor.fetchall()

    for row in rs:
        df.append(row)

    df1 = pd.DataFrame(df)
    df1.columns =['Kode Toko', 'Nama Toko','Barang Bermasalah']
    header = list(df1.columns.values)

    return render_template('index.html', value=df, header=header)


if __name__ == '__main__':
   app.run()