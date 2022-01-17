from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import Flask, render_template, request
from flask import render_template, url_for
import pandas as pd
import mysql.connector as mc

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():

    return render_template('index.html')

@app.route("/laporan1", methods=['POST', 'GET'])
def dataLaporan1():

    df = []
    df1 = []
    ftanggal = '2022-01-07'
    
    if request.method == "POST":
       # getting input with name = fname in HTML form
       ftanggal = request.form.get("ftanggal")

    # USING MYSQL.CONNECTOR
    mydb = mc.connect(
                    host="192.168.59.221", 
                    user="root", 
                    passwd="12345678", 
                    database="ic")

    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT MSTXHG.TOKO, toko.NAMA, mstxhg.tanggal1, count(MSTXHG.PRDCD)as BARANG_BERMASALAH FROM MSTXHG join toko on MSTXHG.TOKO=toko.TOKO where mstxhg.tanggal1='"+ftanggal+"'group by MSTXHG.TOKO order by count(MSTXHG.PRDCD) desc")
        rs = mycursor.fetchall()
        
        for row in rs:
            df.append(row)

        df1 = pd.DataFrame(df)
        df1.columns =['Kode Toko', 'Nama Toko', 'Tanggal','Barang Bermasalah']
        header = list(df1.columns.values)
        
        return render_template('laporan1.html', value=df, header=header)

    except:
        return render_template('404.html')

@app.route("/laporan2", methods=['POST', 'GET'])
def dataLaporan2():

    df = []
    df1 = []
    toko = 'F04S'
    ftoko = ['F04S', 'F0OA', 'F1AM', 'F1FF', 'F2H7', 'F2LV', 'F2NG', 'F3GA', 'F3IE', 'F4IC', 'F4NB', 'F5CP', 'F7GJ', 'F7IG', 'F7NG', 'F7PW', 'F8C8', 'F8WP', 'F9ML''F9R1', 'F9Z5', 'FA2A', 'FA8H', 'FAKU', 'FAS8', 'FBJE','FBVM', 'FCMG', 'FCYC', 'FDI0', 'FENY', 'FFV2', 'FFZQ', 'FG7H', 'FGL5', 'FGTJ', 
            'FH98', 'FHUG', 'FJ87', 'FKB1', 'FKDI', 'FKMZ', 'FKW4', 'FKWI', 'FLMB', 'FM4R', 'FM54', 'FM7I', 'FMHJ', 'FMMK', 'FMUT', 'FN4K', 'FN71', 'FNNN', 'FNSB', 'FPMA', 'FQCL','FQQU', 'FRG8', 'FRQQ', 'FRY6', 'FSHH', 'FSPK', 'FSW1', 'FU4V', 'FUL4', 'FUUU', 'FVDC', 'FWEK', 'FWWB', 'FX4J', 'T0GG', 'T0YB',
            'T0YY', 'T1AD', 'T1E3', 'T1FD', 'T1LY', 'T1M3', 'T1MH', 'T270', 'T2BF', 'T2JS', 'T2JT', 'T2PR', 'T3BJ', 'T3CY', 'T3GI', 'T3GP', 'T3N8', 'T3RM', 'T3WN', 'T3YC', 'T44V', 'T4GL', 'T4KL', 'T4MN', 'T4MW', 'T4MX', 'T4PD', 'T4PP', 'T4U1', 'T4ZR',
            'T53S', 'T55A', 'T57V', 'T5CO', 'T5E6', 'T5FF', 'T5L3', 'T5QR', 'T69N', 'T6MI', 'T6OW', 'T6PV', 'T6TG', 'T6XX', 'T77E', 'T7GH', 'T7M9', 'T7MA', 'T7P7', 'T7UY', 'T8B8', 'T8FT', 'T8GE', 'T8PJ', 'T8RF', 'T8T8', 'T8U8', 'T8YX', 'T94W',
            'T95A', 'T9DJ', 'T9KO', 'T9KS', 'T9OI', 'T9TJ', 'T9U9', 'T9YE', 'T9ZW', 'TA2N', 'TA9Y', 'TATK', 'TAXA', 'TB1X', 'TB3C', 'TB4Y', 'TB9K', 'TBCD', 'TBEM', 'TBKL', 'TBQD', 'TBRR', 'TBUG', 
            'TBUL', 'TCCT', 'TCEL', 'TCFY', 'TCG9', 'TCJD', 'TCNY', 'TCY3', 'TD0Y', 'TD9I', 'TDGR', 'TDH2', 'TDRZ', 'TDT9', 'TDYC', 'TE9U', 'TEAP', 'TEB5', 'TEG7', 'TEKB', 'TEMV', 'TEUC', 'TF4W', 'TFDE', 'TFFU', 'TGBU', 'TGFS', 'TGL9', 'TGW8', 'TH2Y', 'TH9Y', 'THEE', 'THFS', 'THMR', 'THXJ', 'TI3O', 'TICH', 
            'TIWQ', 'TIZA', 'TJF3', 'TJJB', 'TJUZ', 'TK4G', 'TK9O', 'TKAA', 'TKBT', 'TKDE', 'TKE5', 'TKGM', 'TKKZ', 'TKLZ', 'TKPG', 'TKVO', 'TKWY', 'TKY4', 'TL28', 'TL3L', 'TLMS', 'TLNR', 'TLTV', 'TLUK', 'TLZ4', 'TM0X', 'TM3Y', 'TM73', 'TMBA', 'TMCW',
            'TMF8', 'TMK4', 'TMKP', 'TMO5', 'TMOO', 'TMRV', 'TMU5', 'TMWU', 'TMYA', 'TN17', 'TN3M', 'TN5N', 'TN5T', 'TNC3', 'TNLE', 'TNR4', 'TNRC', 'TNRS', 'TO01', 'TO14', 'TOES', 'TOSA', 'TOVK', 'TPEF', 'TPGL', 'TPHM', 'TPK5', 'TPM3', 'TPPU', 'TPUJ',
            'TQIB', 'TQWQ', 'TR0Z', 'TRBK', 'TRE9', 'TRG4', 'TRKV', 'TRQU', 'TRV3', 'TRVH', 'TSEL', 'TSHI', 'TSHO', 'TTCV', 'TTID', 'TTKK', 'TU3L', 'TU3Q', 'TUDL', 'TUE1', 
            'TUH3', 'TUR3', 'TUUH', 'TV9I', 'TVD4', 'TVFQ', 'TVH3', 'TVXJ', 'TW3F', 'TWBI', 'TWKA', 'TWTU', 'TX0D', 'TX2L', 'TX5T', 'TX7H', 'TXML', 'TXUE', 'TXYE', 'TY2W', 'TYA0', 'TYLW', 'TYPH', 'TYRY', 'TYVB', 'TYXT', 'TYZS', 'TZ8X', 'TZER', 'TZKV', 'TZNB', 'TZOH', 'TZR7', 'TZZI']

    if request.method == "POST":
       # getting input with name = fname in HTML form
       toko = str(request.form.get("ftoko"))

    # USING MYSQL.CONNECTOR
    mydb = mc.connect(
                    host="192.168.59.221", 
                    user="root", 
                    passwd="12345678", 
                    database="ic"
            )

    mycursor = mydb.cursor()

    try:
        mycursor.execute("SELECT MSTXHG.TOKO, toko.NAMA, mstxhg.tanggal1, plu_igr.plu, plu_igr.desc, count(plu_igr.plu) as Jumlah FROM MSTXHG join toko on MSTXHG.TOKO=toko.TOKO join plu_igr on mstxhg.prdcd=plu_igr.prdcd where mstxhg.toko='"+toko+"'group by plu_igr.plu order by mstxhg.tanggal1")
        rs = mycursor.fetchall()

        for row in rs:
            df.append(row)

            df1 = pd.DataFrame(df)
            df1.columns =['Kode Toko', 'Nama Toko', 'Tanggal','PLU', 'Nama Barang', 'Jumlah']
            header = list(df1.columns.values)   

        return render_template('laporan2.html', value=df, header=header, ftoko=ftoko)

    except:
        return render_template('404.html')


if __name__ == '__main__':
   app.run(ssl_context=('cert.pem', 'key.pem'))

# flask run --host=0.0.0.0
# flask run --cert=adhoc --host=0.0.0.0