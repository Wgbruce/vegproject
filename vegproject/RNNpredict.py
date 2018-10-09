import pymysql
import numpy as np
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import LSTM,TimeDistributed,Dense
from keras.optimizers import Adam

from sklearn.preprocessing import scale

from keras import regularizers

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
    if (i+6) > len(avgpriceOkralist):
        break
    if (i+6) < Okratrainlength:
        curpen = []
        for j in range(i,i+6):
            if j < (i+6-1):
                curpen.append(avgpriceOkralist[j])
            else:
                y_Okratrain.append(avgpriceOkralist[j])
        x_Okratrain.append(curpen)
    else:
        curpen = []
        for j in range(i,i+6):
             if j < (i+6-1):
                curpen.append(avgpriceOkralist[j])
             else:
                y_Okratest.append(avgpriceOkralist[j])
        x_Okratest.append(curpen)
        


tempx = np.concatenate(( np.array(x_Okratrain ),np.array(x_Okratest)))
tempy = np.concatenate((np.array(y_Okratrain ),np.array(y_Okratest )))

s = np.arange(tempx.shape[0])
np.random.shuffle(s)

Okratrainlength = ((tempx.shape[0])*8)/10

listtrainx = []
listtrainy = []
listtestx = []
listtesty = []

#print(tempx.shape)

for i in range(tempx.shape[0]):
    if i <= Okratrainlength :
        listtrainx.append(tempx[s[i]].tolist())
        listtrainy.append(tempy[s[i]].tolist())
    else:         
        listtestx.append(tempx[s[i]].tolist())
        listtesty.append(tempy[s[i]].tolist())
        
numpyx_Okratrain = np.array(listtrainx)
numpyx_Okratest = np.array(listtestx)
numpyy_Okratrain = np.array(listtrainy )
numpyy_Okratest = np.array(listtesty )
print(numpyx_Okratrain.shape)
        
axiss = []
for i in range(numpyy_Okratrain.shape[0]):
    axiss.append(i+1)
numpyaxis = np.array(axiss)

axisss = []
for i in range(numpyy_Okratest.shape[0]):
    axisss.append(i+1)
numpyaxiss = np.array(axisss)


numpyx_Okratrain = np.reshape(numpyx_Okratrain,[numpyx_Okratrain.shape[0],5,1])
numpyx_Okratest =  np.reshape(numpyx_Okratest,[numpyx_Okratest.shape[0],5,1])



numpyy_Okratrain = np.reshape(numpyy_Okratrain,[numpyx_Okratrain.shape[0],1])
numpyy_Okratest =  np.reshape(numpyy_Okratest,[numpyx_Okratest.shape[0],1])

BATCH_START = 0
TIME_STEPS = 5
BATCH_SIZE = numpyx_Okratrain.shape[0]
INPUT_SIZE = 1
OUTPUT_SIZE = 1
CELL_SIZE = 80
LR = 0.005

model = Sequential()
model.add(LSTM(
        batch_input_shape=(None, TIME_STEPS, INPUT_SIZE),       # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
        output_dim=CELL_SIZE,
        return_sequences = False,
        #stateful = True,
        )	)
#model.add(Dense(40))
#model.add(Dense(30))
model.add(Dense(30,activation = 'relu'))
#model.add(Dense(20,activation = 'relu'))
model.add(Dense(10))
model.add(Dense(30,activation = 'relu'))
model.add(Dense(20,kernel_regularizer=regularizers.l2(0.01)))
#model.add(Dense(10))
model.add(Dense(30,activation = 'relu',kernel_regularizer=regularizers.l2(0.01)))
model.add(Dense(20,activation = 'relu'))
model.add(Dense(10))
model.add(Dense(OUTPUT_SIZE))
adam = Adam(LR)
model.compile(optimizer = adam,
              loss = 'mse',
              )


print('Training -------')
for step in range(2000):
    X_batch = numpyx_Okratrain[BATCH_START :BATCH_START + BATCH_SIZE]
    Y_batch = numpyy_Okratrain[BATCH_START :BATCH_START + BATCH_SIZE]
    BATCH_START = BATCH_START + BATCH_SIZE
    if (BATCH_START + BATCH_SIZE) >= numpyx_Okratrain.shape[0]:
        BATCH_START = 0
    prediction =  model.predict(X_batch,batch_size=X_batch.shape[0])
 
    cost = model.train_on_batch(X_batch,Y_batch)
    if step % 10 ==0:
        plt.plot(numpyaxis,Y_batch,'ro')
        plt.plot(numpyaxis,prediction,'bo')
        plt.show()
        print('train cost: ',cost)
prediction =  model.predict(numpyx_Okratest,batch_size=numpyy_Okratest.shape[0])
numpyy_Okratest = np.reshape(numpyy_Okratest,[-1,])
prediction = np.reshape(prediction,[-1,])
print("answer: ",numpyy_Okratest)
print("prediction: ",prediction)
erro = abs(((prediction - numpyy_Okratest).sum())/prediction[0])
#erro = 0
#for i in range(prediction.shape[0]):
   # erro += pow((prediction[i] - numpyy_Okratest[i]),2)
   # print(erro)
#erro = erro / prediction.shape[0]
print("erro: ",erro)
plt.plot(numpyy_Okratest)
plt.plot(prediction)
plt.show()

plt.plot(numpyaxiss,numpyy_Okratest,'ro')
plt.plot(numpyaxiss,prediction,'bo')
plt.show()



    

