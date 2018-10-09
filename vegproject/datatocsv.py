import pymysql
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM,TimeDistributed,Dense
from keras.optimizers import Adam

from sklearn.preprocessing import scale

from keras import regularizers
import pandas as pd

pymysql . install_as_MySQLdb ()

db = pymysql.Connect(
        host = '127.0.0.1',
        user = 'bruce',
        passwd = '123',
        db = 'vegtable',
        charset='utf8')
            
cur = db.cursor ()
sql =  "SELECT `date`,`item`,`avgprice` from formalprice where item ='FA1 黃秋葵'" 
cur.execute (sql)
db.commit()
Okralist = cur.fetchall() #回傳一個tuple

sql =  "SELECT `date`,`item`,`avgprice` from formalprice where item ='LK2 芥藍菜'" 
cur.execute (sql)
db.commit()
Kalelist = cur.fetchall() #回傳一個tuple

sql =  "SELECT `date`,`item`,`avgprice` from formalprice where item ='FF1 絲瓜'" 
cur.execute (sql)
db.commit()
Loofahlist = cur.fetchall() #回傳一個tuple

avgpriceOkralist = []
for i in range(len(Okralist)):
    avgpriceOkralist.append(Okralist[i][2])

avgpriceKalelist = []
for i in range(len(Kalelist)):
    avgpriceKalelist.append(Kalelist[i][2])

avgpriceLoofahlist = []
for i in range(len(Loofahlist)):
    avgpriceLoofahlist.append(Loofahlist[i][2])

db.close()

df = pd.DataFrame() 
df['avgprice'] = avgpriceLoofahlist
df.to_csv('C:\\Users\\bruce\\Desktop\\vegproject\\avgprice.csv',index = 0)
