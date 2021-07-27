import os
from internetspeedtwitterbot import internetSpeedTwitterBot
PROMISED_UP = 200
PROMISED_DOWN = 200
CRHOME_DRIVE_PATH ="/Applications/chromedriver"
TWITTER_EMAIL = os.environ["TWIT_EMAIL"]
TWITTER_PASS = os.environ['TWIT_PASS']
TWITTER_USER = os.environ['TWIT_USER']

twitBot = internetSpeedTwitterBot(CRHOME_DRIVE_PATH)
speeds = twitBot.getInternetProvider()
if speeds[0]<PROMISED_DOWN or speeds[1]<PROMISED_UP:
    message=""
    if speeds[0] < PROMISED_DOWN and speeds[1] < PROMISED_UP:
        message = f" Dear ISP , why am I getting {speeds[0]}mbps Download Speed and {speeds[1]}mbps Upload speed instead of {PROMISED_DOWN}mbps downlaod speed and {PROMISED_UP}mbps upload speed."
    elif speeds[0]<PROMISED_DOWN:
        message = f" Dear ISP , why am I getting {speeds[0]}mbps Download Speed instead of {PROMISED_DOWN}mbps."
    else:
        message = f" Dear ISP , why am I getting {speeds[1]}mbps Upload Speed instead of {PROMISED_UP}mbps."

    twitBot.tweetAtProvider(TWITTER_EMAIL,TWITTER_USER,TWITTER_PASS,message)