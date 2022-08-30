mob_num='7022698832'
from time import time
import requests
import schedule
import time
def send_mess():
    resp=requests.post('https://textbelt.com/text',{
        'phone':mob_num,
        'message':"hi how are you",
        'key':'textbelt'
    })
    print(resp.json())

#schedule.every().day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_mess)
while True:
    schedule.run_pending()
    time.sleep(1)