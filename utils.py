
import hackmud_chat
import os
import time
import datetime

PATH = os.getcwd()

def debug(msg):
    with open(os.path.join(PATH, 'debug.log'), 'a', encoding='utf-8') as file:
        now = datetime.datetime.now()
        time = now.strftime("[%Y-%m-%d %H:%M:%S]")
        file.write(time + ' - ' + str(msg) + '\n')
        file.close()

def send(func):
    user, channel, msg = func()
    if isinstance(channel, list):
        for c in channel:
            user.say(c, msg)
    else:
        user.say(channel, msg)
    

def init():
    acct = hackmud_chat.Account(token='YourToken')
    user = acct.get_user('YourUsername')
    return acct, user
