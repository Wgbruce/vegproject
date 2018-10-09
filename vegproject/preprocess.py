import pymysql
from datetime import datetime
import os
import pymysql
pymysql . install_as_MySQLdb ()

class Okra(): #黃秋葵
    def __init__(self,thing):
        self.date = thing[0]
        self.item = thing[1].strip()
        self.avgprice = thing[2]

class Loofah(): #絲瓜
    def __init__(self,thing):
        self.date = thing[0]
        self.item = thing[1].strip()
        self.avgprice = thing[2]
        
class Kale(): #芥藍菜
    def __init__(self,thing):
        self.date = thing[0]
        self.item = thing[1].strip()
        self.avgprice = thing[2]


db = pymysql.Connect(
        host = '127.0.0.1',
        user = 'bruce',
        passwd = '123',
        db = 'vegtable',
        charset='utf8')
            
cur = db.cursor ()
sql =  "SELECT `date`,`item`,`avgprice` from price " 
cur.execute (sql)
db.commit()
db.close()


list = cur.fetchall() #回傳一個tuple

tempOkralist = []
tempLoofahlist = []
tempKalelist = []



for i in range(len(list)):
    
    if list[i][1].strip() == 'FA1 黃秋葵':
        tempOkralist.append(Okra(list[i]))
        
    if list[i][1].strip() == 'FF1 絲瓜':
        tempLoofahlist.append(Loofah(list[i]))
        
    if list[i][1].strip() == 'LK2 芥藍菜':
        tempKalelist.append(Kale(list[i]))
        
        
Okralist = []
Loofahlist = []
Kalelist = []

for i in range(len(tempOkralist)):
    check = False
    for j in range(i):
        if (tempOkralist[i].date == tempOkralist[j].date) and (tempOkralist[i].item == tempOkralist[j].item) and (tempOkralist[i].avgprice == tempOkralist[j].avgprice):
            check = True
    
    if(check == False):
        Okralist.append(tempOkralist[i])


           
for i in range(len(tempLoofahlist)):
    check = False
    for j in range(i):
        if (tempLoofahlist[i].date == tempLoofahlist[j].date) and (tempLoofahlist[i].item == tempLoofahlist[j].item) and (tempLoofahlist[i].avgprice == tempLoofahlist[j].avgprice):
            check = True
    
    if(check == False):
        Loofahlist.append(tempLoofahlist[i])



           
for i in range(len(tempKalelist)):
    check = False
    for j in range(i):
        if (tempKalelist[i].date == tempKalelist[j].date) and (tempKalelist[i].item == tempKalelist[j].item) and (tempKalelist[i].avgprice == tempKalelist[j].avgprice):
            check = True
    
    if(check == False):
        Kalelist.append(tempKalelist[i])

now = datetime.now().strftime("%Y-%m-%d")
curdate = now.split("-")
curmonth = int(curdate[1])
curday = int(curdate[2])
curyear = int(curdate[0])
cut = False

month = ['01','02','03','04','05','06','07','08','09','10','11','12']
day = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']

finalOkralist = []
finalLoofahlist = []
finalKalelist = []

for i in range(len(month)):
    if cut == True:
        break
    for j in range(len(day)):
        if cut == True:
            break
        if (i+1) == 2 and (j+1)>28:
            break
        if ((i+1) ==2 or (i+1) ==4 or (i+1) ==6 or (i+1) ==9 or (i+1) == 11) and (j+1) > 30 :
            break
        
        check = False; #用來找有沒有符合的日期，不然就是空值
        for k in range(len(Kalelist)):
            kalelistmonth = int((Kalelist[k].date).split('/')[1])
            kalelistday = int((Kalelist[k].date).split('/')[2])
            
            if (i+1) == kalelistmonth and (j+1) == kalelistday:
                check = True
                finalKalelist.append(Kalelist[k]) 
                break
            
        if check == False:
            check2 =False
            maxl = -1
            maxday = 1
            for l in range(len(Kalelist)):
                kalelistyear = int((Kalelist[l].date).split('/')[0])
                kalelistmonth = int((Kalelist[l].date).split('/')[1])
                kalelistday = int((Kalelist[l].date).split('/')[2])
                if (l>maxl):
                    maxyear =  kalelistyear
                    maxday =  kalelistday
                    maxl =  l
                    if kalelistday > (j+1) and kalelistmonth == (i+1):
                        datestring =""
                        if (i+1)>9 and (j+1) >9 :
                            check2 = True
                            datestring += str(kalelistyear) + "/"+str(i+1) + "/"+str(j+1)
                            finalKalelist.append(Kale((datestring,Kalelist[l].item,Kalelist[l].avgprice)))
                            break
                        if (i+1)<10 and (j+1) >9 :
                            check2 = True
                            datestring += str(kalelistyear) + "/0"+str(i+1) + "/"+str(j+1)
                            finalKalelist.append(Kale((datestring,Kalelist[l].item,Kalelist[l].avgprice)))
                            break
                        if (i+1)>9 and (j+1) <10 :
                            check2 = True
                            datestring += str(kalelistyear) + "/"+str(i+1) + "/0"+str(j+1)
                            finalKalelist.append(Kale((datestring,Kalelist[l].item,Kalelist[l].avgprice)))
                            break
                        if (i+1)<10 and (j+1) <10 :
                            check2 = True
                            datestring += str(kalelistyear) + "/0"+str(i+1) + "/0"+str(j+1)
                            finalKalelist.append(Kale((datestring,Kalelist[l].item,Kalelist[l].avgprice)))
                            break
                        
            if check2 == False:
                if (i+1)>9 and (j+1) >9 :
                    datestring =""
                    datestring += (str(maxyear) + "/"+str(i+1) + "/"+str(j+1))
                    finalKalelist.append(Kale((datestring,Kalelist[maxl].item,Kalelist[maxl].avgprice)))
                if (i+1)<10 and (j+1) >9 :
                    datestring =""
                    datestring += (str(maxyear) + "/0"+str(i+1) + "/"+str(j+1))
                    finalKalelist.append(Kale((datestring,Kalelist[maxl].item,Kalelist[maxl].avgprice)))            
                        
        if (i+1) == curmonth and (j+1) == curday:
            cut = True
                    
'''for i in range(len(Kalelist)):
    print(Kalelist[i].date,Kalelist[i].item,Kalelist[i].avgprice)
print(len(Kalelist))'''

'''for i in range(len(finalKalelist)):
    print(finalKalelist[i].date,finalKalelist[i].item,finalKalelist[i].avgprice)
print(len(finalKalelist))'''


cut = False

for i in range(len(month)):
    if cut == True:
        break
    for j in range(len(day)):
        if cut == True:
            break
        if (i+1) == 2 and (j+1)>28:
            break
        if ((i+1) ==2 or (i+1) ==4 or (i+1) ==6 or (i+1) ==9 or (i+1) == 11) and (j+1) > 30 :
            break
        
        check = False; #用來找有沒有符合的日期，不然就是空值
        
        for k in range(len(Okralist)):
            Okralistmonth = int((Okralist[k].date).split('/')[1])
            Okralistday = int((Okralist[k].date).split('/')[2])
            
            if (i+1) == Okralistmonth and (j+1) == Okralistday:
                check = True
                finalOkralist.append(Okralist[k])
                break
            
        if check == False:
            check2 = False
            maxl = -1
            maxday = 1
            for l in range(len(Okralist)):
                Okralistyear = int((Okralist[l].date).split('/')[0])
                Okralistmonth = int((Okralist[l].date).split('/')[1])
                Okralistday = int((Okralist[l].date).split('/')[2])
                if (l>maxl):
                    maxyear = Okralistyear
                    maxday = Okralistday
                    maxl =  l
                if Okralistday > (j+1) and Okralistmonth == (i+1):
                    datestring =""
                    if (i+1)>9 and (j+1) >9 :
                        check2 = True
                        datestring += str(Okralistyear) + "/"+str(i+1) + "/"+str(j+1)
                        finalOkralist.append(Okra((datestring,Okralist[l].item,Okralist[l].avgprice)))
                        break
                    if (i+1)<10 and (j+1) >9 :
                        check2 = True
                        datestring += str(Okralistyear) + "/0"+str(i+1) + "/"+str(j+1)
                        finalOkralist.append(Okra((datestring,Okralist[l].item,Okralist[l].avgprice)))
                        break
                    if (i+1)>9 and (j+1) <10 :
                        check2 = True
                        datestring += str(Okralistyear) + "/"+str(i+1) + "/0"+str(j+1)
                        finalOkralist.append(Okra((datestring,Okralist[l].item,Okralist[l].avgprice)))
                        break
                    if (i+1)<10 and (j+1) <10 :
                        check2 = True
                        datestring += str(Okralistyear) + "/0"+str(i+1) + "/0"+str(j+1)
                        finalOkralist.append(Okra((datestring,Okralist[l].item,Okralist[l].avgprice)))
                        break
            if check2 == False:
                if (i+1)>9 and (j+1) >9 :
                    #print(str(i+1),str(j+1))
                    datestring =""
                    datestring += (str(maxyear) + "/"+str(i+1) + "/"+str(j+1))
                    finalOkralist.append(Okra((datestring,Okralist[maxl].item,Okralist[maxl].avgprice)))
                if (i+1)<10 and (j+1) >9 :
                   # print(str(i+1),str(j+1))
                    datestring =""
                    datestring += (str(maxyear) + "/"+str(i+1) + "/"+str(j+1))
                    finalOkralist.append(Okra((datestring,Okralist[maxl].item,Okralist[maxl].avgprice)))
        if (i+1) == curmonth and (j+1) == curday:
            cut = True
                    

'''for i in range(len(finalOkralist)):
    print(finalOkralist[i].date,finalOkralist[i].item,finalOkralist[i].avgprice)
print(len(finalOkralist))'''



cut = False

for i in range(len(month)):
    if cut == True:
        break
    for j in range(len(day)):
        #print(str(i+1)+"/"+str(j+1))
        if cut == True:
            break
        if (i+1) == 2 and (j+1)>28:
            break
        if ((i+1) ==2 or (i+1) ==4 or (i+1) ==6 or (i+1) ==9 or (i+1) == 11) and (j+1) > 30 :
            break
        
        check = False; #用來找有沒有符合的日期，不然就是空值
        
        for k in range(len(Loofahlist)):
            Loofahlistmonth = int((Loofahlist[k].date).split('/')[1])
            Loofahlistday = int((Loofahlist[k].date).split('/')[2])
            
            if (i+1) == Loofahlistmonth and (j+1) == Loofahlistday:
                #print(str(i+1) + " " +str(j+1))
                check = True
                finalLoofahlist.append(Loofahlist[k])
                #print("haha")
                break
            
        if check == False:
            check2 = False
            maxl = -1
            maxday = 1
            for l in range(len(Loofahlist)):
                Loofahlistyear = int((Loofahlist[l].date).split('/')[0])
                Loofahlistmonth = int((Loofahlist[l].date).split('/')[1])
                Loofahlistday = int((Loofahlist[l].date).split('/')[2])
                
                if (l>maxl):
                    maxyear = Loofahlistyear
                    maxday = Loofahlistday
                    maxl =  l
                    if Loofahlistday > (j+1) and Loofahlistmonth == (i+1):
                        #print("Loofahlistday: "+str(Loofahlistday) +" j: " + str(j+1))
                    
                        datestring =""
                        if (i+1)>9 and (j+1) >9 :
                            #print("aa")
                            check2 = True
                            datestring += str(Loofahlistyear) + "/"+str(i+1) + "/"+str(j+1)
                            #print(datestring)
                            finalLoofahlist.append(Loofah((datestring,Loofahlist[l].item,Loofahlist[l].avgprice)))
                            break
                        if (i+1)<10 and (j+1) >9 :
                            #print("bb")
                            check2 = True
                            datestring += str(Loofahlistyear) + "/0"+str(i+1) + "/"+str(j+1)
                            #print(datestring)
                            finalLoofahlist.append(Loofah((datestring,Loofahlist[l].item,Loofahlist[l].avgprice)))
                            break
                        if (i+1)>9 and (j+1) <10 :
                            #print("cc")
                            check2 = True
                            datestring += str(Loofahlistyear) + "/"+str(i+1) + "/0"+str(j+1)
                            # print(datestring)
                            finalLoofahlist.append(Loofah((datestring,Loofahlist[l].item,Loofahlist[l].avgprice)))
                            break
                        if (i+1)<10 and (j+1) <10 :
                            #print("dd")
                            check2 = True
                            datestring += str(Loofahlistyear) + "/0"+str(i+1) + "/0"+str(j+1)
                            #print(datestring)
                            finalLoofahlist.append(Loofah((datestring,Loofahlist[l].item,Loofahlist[l].avgprice)))
                            break
            if check2 == False:
                if (i+1)>9 and (j+1) >9 :
                    datestring =""
                    datestring += (str(maxyear) + "/"+str(i+1) + "/"+str(j+1))
                    finalLoofahlist.append(Loofah((datestring,Loofahlist[maxl].item,Loofahlist[maxl].avgprice)))
                if (i+1)<10 and (j+1) >9 :
                    datestring =""
                    datestring += (str(maxyear) + "/0"+str(i+1) + "/"+str(j+1))
                    finalLoofahlist.append(Loofah((datestring,Loofahlist[maxl].item,Loofahlist[maxl].avgprice)))
        if (i+1) == curmonth and (j+1) == curday:
            cut = True
         

'''print("after: ")
for i in range(len(finalLoofahlist)):
    print(finalLoofahlist[i].date,finalLoofahlist[i].item,finalLoofahlist[i].avgprice)
print(len(finalLoofahlist))'''

db = pymysql.Connect(
                    host = '127.0.0.1',
                    user = 'bruce',
                    passwd = '123',
                    db = 'vegtable',
                    charset='utf8')

for i in range(len(finalLoofahlist)):                
    cur = db.cursor ()
    sql =  "INSERT IGNORE INTO formalprice (`date`,`item`,`avgprice`)values('%s','%s','%f')" 
    parameter = (finalLoofahlist[i].date,finalLoofahlist[i].item,float(finalLoofahlist[i].avgprice))
    cur.execute (sql % parameter)
    db.commit()
    parameter = (finalOkralist[i].date,finalOkralist[i].item,float(finalOkralist[i].avgprice))
    cur.execute (sql % parameter)
    db.commit()
    parameter = (finalKalelist[i].date,finalKalelist[i].item,float(finalKalelist[i].avgprice))
    cur.execute (sql % parameter)
    db.commit()
    
db.close()

print(type(finalKalelist[i].item))
                
        
        
          
          
            
    






            
           