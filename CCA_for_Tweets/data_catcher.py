import re
import json
import tweepy

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_home_timeline = api.user_timeline("username")

def save(date):
	dates = open("dates.txt", "a+", encoding="utf-8")
	dates.write(str(date) + "\n")

for status in tweepy.Cursor(api.user_timeline).items():
	# print(status.created_at)
	save(status.created_at)
