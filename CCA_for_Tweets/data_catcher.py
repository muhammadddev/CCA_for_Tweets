import re
import json
import tweepy

<<<<<<< HEAD
from config import *
=======
access_token = "XXX"
access_token_secret = "XXX"
consumer_key = "XXX"
consumer_secret = "XXX"
>>>>>>> f79104ba48336c7bc0957eb7be8cf4bd8ccc49cb

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
