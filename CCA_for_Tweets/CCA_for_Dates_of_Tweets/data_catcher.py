import re
import json
import tweepy

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_home_timeline = api.user_timeline("username")

def save(date, filename):
	dates = open(filename, "a+", encoding="utf-8")
	dates.write(str(date) + "\n")

# for status in tweepy.Cursor(api.user_timeline).items():
# 	# print(status.created_at)
# 	save(status.created_at, filename="dates.txt")

for status in tweepy.Cursor(api.user_timeline).items():
	save(status.text, filename="texts.txt")
