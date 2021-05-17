
import csv
import tweepy
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# Oauth keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update these for the tweet you want to process replies to 'name' = the account username and you can find the tweet id within the tweet URL
name = 'Narendra Modi'
user_id = '1075'

replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(2):
    if hasattr(tweet, 'in_reply_to_user_id_str'):
        if (tweet.in_reply_to_user_id_str==user_id):
            replies.append(tweet)
    print(tweet)

with open('replies_clean.csv', 'w') as f:
    csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
    csv_writer.writeheader()
    for tweet in replies:
        row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
        csv_writer.writerow(row)
