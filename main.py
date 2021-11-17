import json
import os
import time
import requests
from dotenv import load_dotenv

from requests_oauthlib import OAuth1

load_dotenv()

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
method = "GET"

oauth_consumer_key = os.getenv("API_KEY")
oauth_token = os.getenv("ACCESS_TOKEN")
api_secret = os.getenv("SECRET")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = OAuth1(oauth_consumer_key, api_secret, oauth_token, access_token_secret)

payload = {"tweet_mode": "extended"}
response = requests.get(url, auth=auth, params=payload)

# with open("test.txt", "w") as outfile:
#    json.dump(json.loads(response.text), outfile)

for tweet in json.loads(response.text):
    print("User : " + tweet["user"]["name"])
    print("Name : " + tweet["user"]["screen_name"])
    print("Text : " + tweet["full_text"])
    print("Likes : " + str(tweet["favorite_count"]))
    print("Retweets : " + str(tweet["retweet_count"]))
    medias = tweet['entities'].get("media")
    if medias:
        for index, medium in enumerate(medias):
            print("Photo " + str(index) + " : " + medium['media_url'])
    print("-------------------------------------------")


class Test:

    def __init__(self):
        self.Id = "1234"


test = Test()
print(vars(test))
