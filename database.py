# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:52:42 2023

@author: yswav
"""

import mysql.connector as msp
import pandas as pd

class data_dloader():
    def download(stock, from_date="0", to_date="0", period="max"):
        mydb = msp.connect(host='localhost', user='root', passwd = 'YASH911',database="investo")
        myc = mydb.cursor()
        myc.execute(f"SELECT * FROM {stock}")
        data = myc.fetchall()
        column_names = [i[0] for i in myc.description]
        df = pd.DataFrame(data, columns=column_names)
        myc.close()
        df['datetime'] = pd.to_datetime(df['datetime'])
        return df[['datetime', 'close','high','low','open','volume']]
    
    def stocks_ticker():
        mydb = msp.connect(host='localhost', user='root', passwd = 'YASH911',database="investo")
        myc = mydb.cursor()
        myc.execute("SHOW TABLES")
        tables = myc.fetchall()
        table_names = [table[0] for table in tables]
        myc.close()
        return table_names
    

# #####Create database####
# mydb = msp.connect(host='localhost', user='root', passwd = 'YASH911',database="investo")
# myc = mydb.cursor()
# # myc.execute("CREATE DATABASE Investo")
# # myc.execute("SHOW DATABASES")

# # for db in myc:
# #     print(db)
    
# ######create table####

# myc.execute('''
#     CREATE TABLE IF NOT EXISTS HINDALCO (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         datetime DATE,
#         close FLOAT,
#         high FLOAT,
#         low FLOAT,
#         open FLOAT,
#         volume INT,
#         instrument VARCHAR(255)
#     )
# ''')

# ####Data uploader function#####

# def insert_rows_to_mysql(cursor, dataframe, table):
#     placeholders = ', '.join(['%s'] * len(dataframe.columns))
#     columns = ', '.join(dataframe.columns)
#     sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)
    
#     for row in dataframe.itertuples(index=False):
#         cursor.execute(sql, tuple(row))
        
# df = pd.read_excel("HINDALCO_1D.xlsx")

# insert_rows_to_mysql(myc, df, 'HINDALCO')
# mydb.commit()

# ######Get the data######

# myc.execute("SELECT * FROM stock_data")
# data = myc.fetchall()

# column_names = [i[0] for i in myc.description]

# df = pd.DataFrame(data, columns=column_names)

# df.head()
# ##########closing the db#######
# myc.close()
