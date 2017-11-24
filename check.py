import re
from bs4 import BeautifulSoup
from sms import notifier
import time
import mechanize

a = True
while a:

    br = mechanize.Browser()
    html = br.open("http://www.gtu.ac.in/result.aspx",timeout=100).read()
    soup = BeautifulSoup(html,'html5lib')
    msg = ''
    columns = soup.findAll(text=re.compile('BE SEM 5'))

    print columns
    if len(columns) > 0:
        #print "IF LOOP"
        for index in range(len(columns)):
	          txt = columns[index]
	          msg = msg + txt + '  Declared'
        #print 'hieee'
        msg = ' '.join(msg.split())
        notifier(msg)
    print msg
    print time.ctime()
    a = False
    #time.sleep(600)
