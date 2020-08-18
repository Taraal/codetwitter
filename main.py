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


response = requests.get(url, auth=auth)

with open("test.txt", "w") as outfile:
    json.dump(json.loads(response.text), outfile)

print("\u00c9")