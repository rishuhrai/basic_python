from email.message import EmailMessage
import ssl
import smtplib
em_sender='email'#sending email address
em_pass='122222'#enter the app key
email_rec='waxobif692@rxcay.com'
sub= "context of the  mail"
body="""this is the main sub"""
em=EmailMessage()
em['From']=em_sender
em['To']=email_rec
em['subject']=sub
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(em_sender,em_pass)
    smtp.sendmail(em_sender,email_rec,em.as_string())
