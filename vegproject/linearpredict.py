import tensorflow as tf

import pymysql
import numpy as np
import matplotlib.pyplot as plt
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

x_Okratrain = []
x_Okratest = []
y_Okratrain = []
y_Okratest = []

Okratrainlength = (len(avgpriceOkralist)*8)/10 

for i in range(len(avgpriceOkralist)):
    if (i+11) > len(avgpriceOkralist):
        break
    if (i+11) < Okratrainlength:
        curpen = []
        for j in range(i,i+11):
            if j < (i+11-1):
                curpen.append(avgpriceOkralist[j])
            else:
                y_Okratrain.append(avgpriceOkralist[j])
        x_Okratrain.append(curpen)
    else:
        curpen = []
        for j in range(i,i+11):
             if j < (i+11-1):
                curpen.append(avgpriceOkralist[j])
             else:
                y_Okratest.append(avgpriceOkralist[j])
        x_Okratest.append(curpen)
        
numpyx_Okratrain = np.array(x_Okratrain )
numpyx_Okratest = np.array(x_Okratest)
numpyy_Okratrain = np.array(y_Okratrain )
numpyy_Okratest = np.array(y_Okratest )
Okraweight = np.zeros((len(numpyx_Okratrain[0])))

axiss = []
for i in range(numpyy_Okratest.shape[0]):
    axiss.append(i+1)
numpyaxis = np.array(axiss)

def Okralinearregression(numpyx_Okratrain,Okraweight,numpyy_Okratrain ):
    lr=10
    iteration=10000   #迭代10000次
    s_grad=np.zeros(len(numpyx_Okratrain[0]))
    for i in range(iteration):
        tem=np.dot(numpyx_Okratrain,Okraweight)
        loss = numpyy_Okratrain - tem 
        grad=np.dot(numpyx_Okratrain.transpose(),loss)*(-2)
        s_grad+=grad**2
        ada=np.sqrt(s_grad)
        Okraweight=Okraweight-lr*grad/ada
    #print(Kaleweight)
    
    finaly_predict = np.dot(numpyx_Okratest,Okraweight)
    erro = abs(((finaly_predict - numpyy_Okratest).sum())/finaly_predict.shape[0])
    print('Okra erro: ' + str(erro))
    plt.plot(finaly_predict)
    plt.plot(numpyy_Okratest)
    plt.show()
    plt.plot(numpyaxis,finaly_predict,'ro')
    plt.plot(numpyaxis,numpyy_Okratest,'bo')
    plt.show()
    
        

Okralinearregression(numpyx_Okratrain,Okraweight,numpyy_Okratrain)
        

x_Kaletrain = []
x_Kaletest = []
y_Kaletrain = []
y_Kaletest = []

Kaletrainlength = (len(avgpriceKalelist)*8)/10 

for i in range(len(avgpriceKalelist)):
    if (i+11) > len(avgpriceKalelist):
        break
    if (i+11) < Kaletrainlength:
        curpen = []
        for j in range(i,i+11):
            if j < (i+11-1):
                curpen.append(avgpriceKalelist[j])
            else:
                y_Kaletrain.append(avgpriceKalelist[j])
        x_Kaletrain.append(curpen)
    else:
        curpen = []
        for j in range(i,i+11):
             if j < (i+11-1):
                curpen.append(avgpriceKalelist[j])
             else:
                y_Kaletest.append(avgpriceKalelist[j])
        x_Kaletest.append(curpen)
        
numpyx_Kaletrain = np.array(x_Kaletrain )
numpyx_Kaletest = np.array(x_Kaletest)
numpyy_Kaletrain = np.array(y_Kaletrain )
numpyy_Kaletest = np.array(y_Kaletest )
Kaleweight = np.zeros((len(numpyx_Kaletrain[0])))

def Kalelinearregression(numpyx_Kaletrain,Kaleweight,numpyy_Kaletrain ):
    lr=10
    iteration=10000   #迭代10000次
    s_grad=np.zeros(len(numpyx_Kaletrain[0]))
    for i in range(iteration):
        tem=np.dot(numpyx_Kaletrain,Kaleweight)
        loss = numpyy_Kaletrain - tem 
        grad=np.dot(numpyx_Kaletrain.transpose(),loss)*(-2)
        s_grad+=grad**2
        ada=np.sqrt(s_grad)
        Kaleweight=Kaleweight-lr*grad/ada
    #print(Kaleweight)
    
    finaly_predict = np.dot(numpyx_Kaletest,Kaleweight)
    erro = abs(((finaly_predict - numpyy_Kaletest).sum())/finaly_predict.shape[0])
    print('Kale erro: ' + str(erro))
    plt.plot(finaly_predict)
    plt.plot(numpyy_Kaletest)
    plt.show()
    plt.plot(numpyaxis,finaly_predict,'ro')
    plt.plot(numpyaxis,numpyy_Kaletest,'bo')
    plt.show()
    
        

Kalelinearregression(numpyx_Kaletrain, Kaleweight,numpyy_Kaletrain)

        
        
x_Loofahtrain = []
x_Loofahtest = []
y_Loofahtrain = []
y_Loofahtest = []

totalx_Loofah =[]
totaly_Loofah = []


for i in range(len(avgpriceLoofahlist)):
    if (i+11) > len(avgpriceLoofahlist):
        break
    curpen = []
    for j in range(i,i+11):
        if j < (i+11-1):
            curpen.append(avgpriceLoofahlist[j])
        else:
            totaly_Loofah.append(avgpriceLoofahlist[j])
    totalx_Loofah.append(curpen)
numpytotalx_Loofah = np.array(totalx_Loofah)
numpytotaly_Loofah = np.array(totaly_Loofah)

Loofahtrainlength = (len(avgpriceLoofahlist)*8)/10 

for i in range(len(avgpriceLoofahlist)):
    if (i+11) > len(avgpriceLoofahlist):
        break
    if (i+11) < Loofahtrainlength:
        curpen = []
        for j in range(i,i+11):
            if j < (i+11-1):
                curpen.append(avgpriceLoofahlist[j])
            else:
                y_Loofahtrain.append(avgpriceLoofahlist[j])
        x_Loofahtrain.append(curpen)
    else:
        curpen = []
        for j in range(i,i+11):
             if j < (i+11-1):
                curpen.append(avgpriceLoofahlist[j])
             else:
                y_Loofahtest.append(avgpriceLoofahlist[j])
        x_Loofahtest.append(curpen)           

numpyx_Loofahtrain = np.array(x_Loofahtrain )
numpyx_Loofahtest = np.array(x_Loofahtest)
numpyy_Loofahtrain = np.array(y_Loofahtrain )
numpyy_Loofahtest = np.array(y_Loofahtest )
Loofahweight = np.zeros((len(numpyx_Loofahtrain[0])))

#print(numpyx_Loofahtrain[0])



def Loofahlinearregression(numpyx_Loofahtrain,Loofahweight,numpyy_Loofahtrain ):
    lr=0.1
    iteration=100000   #迭代100000次
    s_grad=np.zeros(len(numpyx_Loofahtrain[0]))
    for i in range(iteration):
        tem=np.dot(numpyx_Loofahtrain,Loofahweight)
        loss = numpyy_Loofahtrain - tem 
        grad=np.dot(numpyx_Loofahtrain.transpose(),loss)*(-2)
        s_grad+=grad**2
        ada=np.sqrt(s_grad)
        Loofahweight=Loofahweight-lr*grad/ada
    #print(Loofahweight)
    
    finaly_predict = np.dot(numpyx_Loofahtest,Loofahweight)
    erro = abs(((finaly_predict - numpyy_Loofahtest).sum())/finaly_predict.shape[0])
    print('Loofah erro: ' +str(erro))
    #print(finaly_predict.shape[0])
    plt.plot(finaly_predict)
    plt.plot(numpyy_Loofahtest)
    plt.show()
        
    plt.plot(numpyaxis,finaly_predict,'ro')
    plt.plot(numpyaxis,numpyy_Loofahtest,'bo')
    plt.show()
    
    finaly_outpredict = np.dot(numpytotalx_Loofah,Loofahweight)
    df = pd.DataFrame() 
    df['predict'] = finaly_outpredict
    df.to_csv('C:\\xampp\\htdocs\\Loofahlinearpredict.csv',index = 0)

Loofahlinearregression(numpyx_Loofahtrain,Loofahweight,numpyy_Loofahtrain )






    

    

