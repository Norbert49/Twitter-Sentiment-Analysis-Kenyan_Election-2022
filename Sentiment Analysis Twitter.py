from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd
import tweepy
import re

# Text Cleansing Function
def my_preprocessor(mytext):
    #Convert to lower case
    mytext = mytext.lower()
    #Convert www.* or https?://* to URL
    mytext = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',mytext) 
    #Convert @username to AT_USER
    mytext = re.sub('@[^\s]+','AT_USER',mytext)
    #Remove additional white spaces
    mytext = re.sub('[\s]+', ' ', mytext)
    #Replace #word with word
    mytext = re.sub(r'#([^\s]+)', r'\1',mytext)
    #trim
    mytext = mytext.strip('\'"')
    return mytext

#Polarity marker
def polarity_check(x):
    if x > 0:
        return "Positif"
    elif x < 0:
        return "Negatif"
    else:
        return "Netral"
#Crawling
consumer_key = "CPZ6BgwCbHFFawlk1DpdJEycZ"
consumer_secret = "KRKoz9uTfvMDszqqKapOQgmP3xfaiJe9WIHAg0Pa5uYsKPiiSz"
access_token = "3289735469-UnGyjreVxlbet5mgHQj5OCoBLnITbAthGqwiSvR"
access_token_secret = "fsshFokH4VBmMn7deQr7H5Xt4kMcI0Dj9A9weeoX5lEKy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

tweetan=[]
nairobi=[]
teks=[]
Id=[]
sn=[]
source=[]
rtc=[]

for tweet in tweepy.Cursor(api.search_tweets, q = ["ugali"],
                           count = 200,
                           lang = "id").items():
    if not tweet : 
        print('tweet habis')
        break
    if (not tweet.retweeted) and ('RT @' not in tweet.text):
        print(tweet.created_at, tweet.text)
        tweetan.append(tweet)
        nairobi.append(tweet.created_at) 
        teks.append(tweet.text)
        Id.append(tweet.id)
        sn.append(tweet.user.screen_name)
        source.append(tweet.source)
        rtc.append(tweet.retweet_count)
data = pd.DataFrame()
data['Date'] = nairobi
data['Tweets'] = teks
data['ID'] = Id
data['Screen Name'] = sn
data['Number of Retweets'] = rtc
data['Source'] = source