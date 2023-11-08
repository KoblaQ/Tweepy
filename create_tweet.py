# Import Tweepy library
import tweepy 


client = tweepy.Client(consumer_key= 'QJ08ZoceKo5BZ1dahHeI10aVz',
                       consumer_secret= 'ePO98fE3vaSRQRwF9JOcHe1YnkglfRFqUaXhoFYyZJCs6uGwpQ',
                         access_token= '126623839-B8RS3sniP9mhah9GZEtsSVB0Yru0BsLeMDwYmHJF' ,
                          access_token_secret= 'VYaBthG4PzaL8c4pBNn6rSULWW9MM8OtMGaMwUyI2MvKt')


# Creating a Tweet
response_CreateTweet = client.create_tweet(text= 'Tweeting with Tweepy')
print(response_CreateTweet)
tweet_ID = response_CreateTweet.data['id']
print(f"Tweet ID: {tweet_ID}")