import schedule
import time
from send_email import send_email

schedule.every().day.at("01:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60) #wait one minute
