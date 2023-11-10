# Import Tweepy library
import tweepy
import authentication # Import the authentication keys from the authentication.py file.

# Authorization with API Keys
bearer_token = authentication.bearer_token
consumer_key = authentication.consumer_key
consumer_secret = authentication.consumer_secret
access_token = authentication.access_token
access_token_secret= authentication.access_token_secret

# Auth 1.0
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Auth 2.0
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# Upload the tweet using the media_upload endpoint
media_id = api.media_upload(filename= "twython1.png").media_id_string

print(f"Media ID: {media_id}") # Print the media ID

# Text to tweet with the media
text = "Publishing media in a tweet using Tweepy"

#Upload tweet and image using 2.0
response_image_tweet = client.create_tweet(text=text, media_ids=[media_id]) # EXTRA: Try to reply to a specific tweet (in_reply_to_tweet_id=)

# Debugging
print("Published successfully")
print(response_image_tweet) # Print the details of the tweet
print(f"Tweet ID: {response_image_tweet.data.id}")
