# Import Tweepy library
import tweepy 

client = tweepy.Client(consumer_key= 'QJ08ZoceKo5BZ1dahHeI10aVz',
                       consumer_secret= 'ePO98fE3vaSRQRwF9JOcHe1YnkglfRFqUaXhoFYyZJCs6uGwpQ',
                         access_token= '126623839-B8RS3sniP9mhah9GZEtsSVB0Yru0BsLeMDwYmHJF' ,
                          access_token_secret= 'VYaBthG4PzaL8c4pBNn6rSULWW9MM8OtMGaMwUyI2MvKt')
tweet_ID = 'insert_id_here'

# Deleting a tweet
response_DeleteTweet = client.delete_tweet(id= tweet_ID)
print(response_DeleteTweet)