# Import Tweepy library
import tweepy
import authentication # Import the authentication keys from the authentication.py file.


client = tweepy.Client(consumer_key= authentication.consumer_key,
                       consumer_secret= authentication.consumer_secret,
                         access_token= authentication.access_token ,
                          access_token_secret= authentication.access_token_secret)


# Creating a Tweet
response_CreateTweet = client.create_tweet(text= 'Tweeting with Tweepy')
print(response_CreateTweet)

# Get the Tweet ID
tweet_ID = response_CreateTweet.data['id']
print(f"Tweet ID: {tweet_ID}")
