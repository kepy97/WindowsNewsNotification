import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendmail(i,result):
    #fromaddr = "hellohi8878@gmail.com"
    fromaddr = "keyul.kepy@gmail.com"
    toaddr = "keyul31@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Result Declared Just Now"
 
    body = result + ' ' + str(i)
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "hellohi8878")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print('Mail Sent')
    server.quit()


