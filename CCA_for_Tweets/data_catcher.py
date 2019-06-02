import re
import json
import tweepy

access_token = "1046123176718200834-01QvgXnitZowONQtdpGqtzfFwUOjpg"
access_token_secret = "FUyh1HsKxEd5SDxpq9VyJ40Ol6sP4IQMZPoDV5Rem7dDL"
consumer_key = "7FVAVemGmTiJtDf4y2n4BFmeo"
consumer_secret = "FNOMlByIjbYi7tD4nFQUzsJ8FRirXPAamKBRHX455A0YdeuRyO"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_home_timeline = api.user_timeline("muhammadddev")

def save(date):
	dates = open("dates.txt", "a+", encoding="utf-8") 
	dates.write(str(date) + "\n")

for status in tweepy.Cursor(api.user_timeline).items():
	# print(status.created_at)
	save(status.created_at)