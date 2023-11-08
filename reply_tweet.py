# Import Tweepy library
import tweepy

# Authorization Keys
client = tweepy.Client(consumer_key= 'QJ08ZoceKo5BZ1dahHeI10aVz',
                       consumer_secret= 'ePO98fE3vaSRQRwF9JOcHe1YnkglfRFqUaXhoFYyZJCs6uGwpQ',
                         access_token= '126623839-B8RS3sniP9mhah9GZEtsSVB0Yru0BsLeMDwYmHJF' ,
                          access_token_secret= 'VYaBthG4PzaL8c4pBNn6rSULWW9MM8OtMGaMwUyI2MvKt')


tweet_ID = 'insert_tweet_id'

# Replying to a Tweet
response_ReplyTweet = client.create_tweet(text= "It feels like i'm talking to myself", in_reply_to_tweet_id= tweet_ID)
print(response_ReplyTweet)
tweet_ID = response_ReplyTweet.data['id']
print(tweet_ID)
