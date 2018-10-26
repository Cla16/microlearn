import smtplib
from wikipedia_requests import parse_request
from datetime import datetime
from config.py import *

today = datetime.today()
day, month, year = today.day, today.month, today.year
date = str(day) + "/" + str(month) + "/" + str(year)
article = parse_request()

sent_from = user
to = "clarkevandenhoven@gmail.com"
subject = "Article for " + date + " : " +  article["title"]
body = article["summary"] + "\n\nRead more at: " + article["url"] + "\n\n" + article["image"]

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.ehlo()
server.login(user, password)
server.sendmail(sent_from, to, email_text.encode('utf-8'))
server.close()
