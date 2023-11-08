# Import Tweepy library
import tweepy

# Authorization with API Keys
client = tweepy.Client(consumer_key= 'QJ08ZoceKo5BZ1dahHeI10aVz',
                       consumer_secret= 'ePO98fE3vaSRQRwF9JOcHe1YnkglfRFqUaXhoFYyZJCs6uGwpQ',
                         access_token= '126623839-B8RS3sniP9mhah9GZEtsSVB0Yru0BsLeMDwYmHJF' ,
                          access_token_secret= 'VYaBthG4PzaL8c4pBNn6rSULWW9MM8OtMGaMwUyI2MvKt')


response = client.get_me()

# Print the retrieved details
print(response)
print(f"ID: {response.data.id}")
print(f"Name: {response.data.name}")
print(f"Username: {response.data.username}")