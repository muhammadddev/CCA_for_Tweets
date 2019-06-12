import re
import json
import tweepy
import pandas as pd

from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user_home_timeline = api.user_timeline("muhammadddev", tweet_mode="extended")

status_texts = []
# statuses = tweepy.Cursor(api.user_timeline).
for status in tweepy.Cursor(api.user_timeline, tweet_mode='extended').items():
	status_texts.append(status.full_text)

dataframe = pd.DataFrame(status_texts, columns=['raw_texts'])

dataframe.to_csv("/home/muhammad/Envs/tweet/code/CCA_for_Tweets/CCA_for_Texts_of_Tweets/created_datas/text_data.csv", encoding="utf-8")
