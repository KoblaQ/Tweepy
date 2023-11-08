# Import Tweepy library
import tweepy

# Authorization with API Keys
bearer_token = 'AAAAAAAAAAAAAAAAAAAAADKKqwEAAAAAdgpiqNtxTJDVhtGZPWSxPVhzIV8%3DwLVAjTbOPPYBkYrIOAo6YtKjPBGx0I7pyVm9uIJ78UC8iiTLTa'
consumer_key = 'QJ08ZoceKo5BZ1dahHeI10aVz'
consumer_secret = 'ePO98fE3vaSRQRwF9JOcHe1YnkglfRFqUaXhoFYyZJCs6uGwpQ'
access_token = '126623839-B8RS3sniP9mhah9GZEtsSVB0Yru0BsLeMDwYmHJF'
access_token_secret= 'VYaBthG4PzaL8c4pBNn6rSULWW9MM8OtMGaMwUyI2MvKt'

# Auth 1.0
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Auth 2.0
client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)

# Upload the tweet using the media_upload endpoint
#media_id = api.media_upload(filename= "C://Users//edemq//OneDrive - Hämeen ammattikorkeakoulu//Työpöytä//PythonHamk//Tweepy//twython1.png").media_id_string
media_id = api.media_upload(filename= "C://Users//edemq//OneDrive - Hämeen ammattikorkeakoulu//Työpöytä//PythonHamk//Tweepy//twython1.png").media_id_string
print(f"Media ID: {media_id}") # Print the media ID

# Text to tweet with the media
text = "Publishing media in a tweet using Tweepy"

#Upload tweet and image using 2.0
response_image_tweet = client.create_tweet(text=text, media_ids=[media_id]) # EXTRA: Try to reply to a specific tweet (in_reply_to_tweet_id=)

# Debugging
print("Published successfully")
print(response_image_tweet) # Print the details of the tweet
print(f"Tweet ID: {response_image_tweet.data.id}")
