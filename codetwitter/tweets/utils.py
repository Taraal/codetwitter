import json
import os
import requests
from dotenv import load_dotenv

from requests_oauthlib import OAuth1

load_dotenv()


def get_timeline():
    url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

    oauth_consumer_key = os.getenv("API_KEY")
    oauth_token = os.getenv("ACCESS_TOKEN")
    api_secret = os.getenv("SECRET")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = OAuth1(oauth_consumer_key, api_secret, oauth_token, access_token_secret)

    payload = {"tweet_mode": "extended"}
    response = requests.get(url, auth=auth, params=payload)

    tweets = []
    for tweet in json.loads(response.text):
        tweet_dict = {
            "User": tweet["user"]["name"],
            "Name": tweet["user"]["screen_name"],
            "Text": tweet["full_text"],
            "Likes": str(tweet["favorite_count"]),
            "Retweets": str(tweet["retweet_count"]),
            "Medias": []
        }
        medias = tweet['entities'].get("media")
        if medias:
            for medium in medias:
                tweet_dict["Medias"].append(medium['media_url'])
        tweets.append(tweet_dict)

    return tweets
