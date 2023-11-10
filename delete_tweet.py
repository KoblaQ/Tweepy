# Import Tweepy library
import tweepy 
import authentication # Import the authentication keys from the authentication.py file.


client = tweepy.Client(consumer_key= authentication.consumer_key,
                       consumer_secret= authentication.consumer_secret,
                         access_token= authentication.access_token ,
                          access_token_secret= authentication.access_token_secret)

# Insert the Tweet ID
tweet_ID = 'Insert_ID'

# Deleting a tweet
response_DeleteTweet = client.delete_tweet(id= tweet_ID)
print(response_DeleteTweet)