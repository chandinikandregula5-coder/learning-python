'''
SMTP(simple mail transfer protocol.:
this is used to send emails from server to another...
note:
1.SMTP SSL PORT
---------------
465
2.SMTP TLS port
587
import smtplib
email message class
-------------------
msg["subject"] = 'SMTP ON MAIL'
msg ["from"] ='sender@mail.com'
msg['TO'] =
 
import smtplib
from email.message import EmailMessage
sender ='chandinikandregula5@gmail.com'
password =' maqblqwiuuuwimzk'
msg = EmailMessage()

msg["subject"] = "welcome mail"
msg['from']  =  sender
msg["TO"] ='saranyasiri2005@gmail.com'

msg.set_content("hello")
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login(sender,password)
server.send_message(msg)
server.quit()
'''
import smtplib
from email.message import EmailMessage
sender = 'chandinikandregula5@gmail.com'
password = 'ncnbflktiyzssezh'
receiver_= ['saranyasiri2005@gmail.com','bhavanajoseph84392@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server. login(sender,password)
msg = EmailMessage()
for email in receiver_:
    msg = EmailMessage()
    msg['Subject'] ='welcome mail'
    msg['From'] = sender
    msg['TO'] = email
    msg.set_content('PICHI')
    server.send_message(msg)
server.quit()  



    
