import re
import requests
from bs4 import BeautifulSoup
import sms as w
from mail import sendmail
import time
import pymssql

sem8rem = True
sem7reg = True
sem7rem = True
sem7regd = True
sem7remd = True
conn = pymssql.connect(host='localhost', user='sa', password='contact', database='Gtu_Student')
cursor = conn.cursor()
print("Started")
a = True
while a:
    try:
        html = requests.get("http://www.gtu.ac.in/result.aspx")
        soup = BeautifulSoup(html.content,'html5lib')
        msg = ''
        columns = soup.findAll(text=re.compile('BE SEM'))
        print(columns)
        if len(columns) > 0:
            
            for index in range(len(columns)):
                      txt = columns[index]
                      msg = msg + txt + '  Declared'
            #print 'hieee'
            msg = ' '.join(msg.split())
            
            if "BE SEM 8 - Regular (DEC 2017)" in msg and sem8rem:
                send = "Result of BE SEM 8 - Regular (DEC 2017) Exam Declared. Check Here--> http://bit.ly/GtuResult                       All The Best From : KePy"
                header = "Result Declared"
                
                try:
                    sql=("select emailid from studentdetails where semester = 8")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    
                    for row in data:
                        print(row[0])
                        sendmail (send,row[0],header)
                
                except Exception as e:
                    print("Exception In send MAIL" +str(e))
                
                try:
                    sql=("select mobile from studentdetails where semester = 8")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    q=w.sms()
                    for row in data:
                        q.send(row[0],send)
                        n=q.msgSentToday()
                        print("Sms Sent" +row[0])

                except Exception:
                    print("Exception In SMS")
                
                
                sem8rem = False
				
            if "BE SEM 7 - Remedial (NOV 2017)" in msg and sem7rem:
                send = "Result of BE SEM 7 - Remedial (NOV 2017) Exam Declared. Check Here--> http://bit.ly/GtuResult                       All The Best From : KePy"
                header = "Result Declared"
                
                try:
                    sql=("select emailid from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    
                    for row in data:
                        print(row[0])
                        sendmail (send,row[0],header)
                
                except Exception as e:
                    print("Exception In send MAIL" +str(e))
                
                try:
                    sql=("select mobile from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    q=w.sms()
                    for row in data:
                        q.send(row[0],send)
                        n=q.msgSentToday()
                        print("Sms Sent" +row[0])

                except Exception:
                    print("Exception In SMS")
                
                
                sem7rem = False
				
            if "BE SEM 7 - Regular (NOV 2017)" in msg and sem7reg:
                send = "Result of BE SEM 7 - Regular (NOV 2017) Exam Declared. Check Here--> http://bit.ly/GtuResult                       All The Best From : KePy"
                header = "Result Declared"
                
                try:
                    sql=("select emailid from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    
                    for row in data:
                        print(row[0])
                        sendmail (send,row[0],header)
                
                except Exception as e:
                    print("Exception In send MAIL" +str(e))
                
                try:
                    sql=("select mobile from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    q=w.sms()
                    for row in data:
                        q.send(row[0],send)
                        n=q.msgSentToday()
                        print("Sms Sent" +row[0])

                except Exception:
                    print("Exception In SMS")
				
                sem7reg = False
				
            if "BE SEM 7 - Remedial (DEC 2017)" in msg and sem7remd:
                send = "Result of BE SEM 7 - Remedial (DEC 2017) Exam Declared. Check Here--> http://bit.ly/GtuResult                       All The Best From : KePy"
                header = "Result Declared"
                
                try:
                    sql=("select emailid from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    
                    for row in data:
                        print(row[0])
                        sendmail (send,row[0],header)
                
                except Exception as e:
                    print("Exception In send MAIL" +str(e))
                
                try:
                    sql=("select mobile from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    q=w.sms()
                    for row in data:
                        q.send(row[0],send)
                        n=q.msgSentToday()
                        print("Sms Sent" +row[0])

                except Exception:
                    print("Exception In SMS")
                
                
                sem7remd = False
				
            if "BE SEM 7 - Regular (DEC 2017)" in msg and sem7regd:
                send = "Result of BE SEM 7 - Regular (DEC 2017) Exam Declared. Check Here--> http://bit.ly/GtuResult                       All The Best From : KePy"
                header = "Result Declared"
                
                try:
                    sql=("select emailid from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    
                    for row in data:
                        print(row[0])
                        sendmail (send,row[0],header)
                
                except Exception as e:
                    print("Exception In send MAIL" +str(e))
                
                try:
                    sql=("select mobile from studentdetails where semester = 7")
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    q=w.sms()
                    for row in data:
                        q.send(row[0],send)
                        n=q.msgSentToday()
                        print("Sms Sent" +row[0])

                except Exception:
                    print("Exception In SMS")
                
                sem7regd = False
        print(time.ctime())
        time.sleep(300)
    except Exception as e:
        print("Exception Found" +str(e))
	
