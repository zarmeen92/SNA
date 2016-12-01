
# coding: utf-8

# In[1]:

import tweepy
from tweepy import OAuthHandler
import json
import time
consumer_key =   #'YOUR-CONSUMER-KEY'
consumer_secret = #'YOUR-CONSUMER-SECRET'
access_token =  #'YOUR-ACCESS-TOKEN'
access_secret =  #'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)


api = tweepy.API(auth_handler=auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

q = "#racism OR #BLACKLIVESMATTER OR #saynotoracism OR #NOTRACIST OR #Racism OR #education OR #stemeducation OR #health OR #healthcare OR #poverty OR #endpoverty OR #worldfoodday OR #hunger OR #foodsecurity OR #biodiversity OR #nochildlabour OR #stophonorkillings OR #terrorism OR #unemployment OR #stopchildabuse OR #children OR #women OR #humanrights OR #immigration OR #refugees OR #refugeecrisis OR #climate OR #climatechange OR #genderequality OR #EqualPay"# URL encoded query

# Additional query parameters:
#   since: {date}
#   until: {date}
# Just add them to the 'q' variable: q+" since: 2014-01-01 until: 2014-01-02"
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('socialCausesTweets.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#racism','#BLACKLIVESMATTER','#saynotoracism','#NOTRACIST','#Racism','#education','#stemeducation','#health','#healthcare', '#poverty','#endpoverty','#worldfoodday','#hunger','#foodsecurity','#biodiversity','#nochildlabour','#stophonorkillings','#terrorism','#unemployment', '#stopchildabuse','#children','#women','#humanrights','#immigration','#refugees','#refugeecrisis','#climate','#climatechange','#genderequality','#EqualPay'])