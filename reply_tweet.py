# Import Tweepy library
import tweepy
import authentication # Import the authentication keys from the authentication.py file.

# Authorization Keys
client = tweepy.Client(consumer_key= authentication.consumer_key,
                       consumer_secret= authentication.consumer_secret,
                         access_token= authentication.access_token ,
                          access_token_secret= authentication.access_token_secret)

# Insert the Tweet ID
tweet_ID = 'Insert_tweet_id_here'

# Replying to a Tweet
response_ReplyTweet = client.create_tweet(text= "It feels like i'm talking to myself", in_reply_to_tweet_id= tweet_ID)
print(response_ReplyTweet)

# Get the id of the reply tweet
tweet_ID = response_ReplyTweet.data['id']
print(tweet_ID)
