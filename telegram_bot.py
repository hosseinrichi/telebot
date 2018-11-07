from telegram.ext import Updater, CommandHandler,Job
import logging
import datetime
import re,requests
from bs4 import BeautifulSoup
import random
updater = Updater("615355678:AAE28GPdyfnO0S2CfccdacaljACYGFe-tUw")
jobqueue = updater.job_queue
def myfirst_job(bot,update):
    time = datetime.datetime.now().strftime("%Y - %m - %d ---%H - %M - %S     %h")
    bot.sendMessage(chat_id="@aaasssdddwww", text= "farda shod "+str(time))


def positive_message(bot, update):
    c = requests.get("https://1stwebdesigner.com/motivational-quote-of-the-day/")
    soup = BeautifulSoup(c.text, "html.parser")
    ccc = soup.find_all('p')
    f = {}
    i = 1
    for item in ccc:
        f[i] = (item.text)
        i += 1
    hh = {}
    n = 1
    for item in f.values():
        if item is not "":
            hh[n] = (item)
            n += 1

    ffff = []
    tex = random.choice(range(1,109))
    if tex not  in ffff:
        texti = hh[tex]
        ffff.append([tex])

    time = datetime.datetime.now().strftime("%m-%d ____%H-%M")
    bot.sendMessage(chat_id="@aaasssdddwww",text= "the time is {}   🕛 :) y rooze dg ham gozasht  <<hossein>> omidvaram rooze bad k  payame  badio mibini\
                                                  az roozet mofid tarin estefade ro karde bashi. taslim nasho ❤. movafaqyat vase toe pesr :)".format(time) +"\n \n \n{}".format(texti))



myfirstjob = jobqueue.run_repeating(positive_message ,interval=10.0,first=0  )
#logging.basicConfig(level=logging.DEBUG,
 #                   format=("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))


updater.start_polling()
updater.idle()