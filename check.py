import re
from bs4 import BeautifulSoup
from sms import notifier
from mail import sendmail
import time
import mechanize
import pymysql

sem4rem = True
conn = pymysql.connect(host='localhost', user='root', passwd='root', db='gtudatabase')
cursor = conn.cursor()

a = True
while a:

    br = mechanize.Browser()
    html = br.open("http://www.gtu.ac.in/result.aspx",timeout=100).read()
    soup = BeautifulSoup(html,'html5lib')
    msg = ''
    columns = soup.findAll(text=re.compile('BE SEM'))

    print columns
    if len(columns) > 0:
        #print "IF LOOP"
        for index in range(len(columns)):
	          txt = columns[index]
	          msg = msg + txt + '  Declared'
        #print 'hieee'
        msg = ' '.join(msg.split())
        print msg
        if "BE SEM 6 - Regular (MAY 2017)" in msg and sem4rem:
            send = "Result of BE SEM 6 - Regular (MAY 2017) Exam Declared                      From :- KePy"


            sql=("select emailid from studentdetails where semester = 7")
            cursor.execute(sql)
            data=cursor.fetchall()
            print data
            for row in data:
                print row[0]
                sendmail(send,row[0])

            sql=("select mobile from studentdetails where semester = 7")
            cursor.execute(sql)
            data=cursor.fetchall()
            print data
            for row in data:
                print row[0]
                notifier(send,"7016141096")


            print "Done"
            sem4rem = False
    print time.ctime()
