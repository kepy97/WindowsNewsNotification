import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(result,tomail,header):
    fromaddr = "XXXXXXX@gmail.com"
    toaddr = tomail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = header
 
    body = result + ' '
    msg.attach(MIMEText(body, 'plain'))
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "XXXXX")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    print('Mail Sent')
    server.quit()
