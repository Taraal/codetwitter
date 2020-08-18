import base64
from hashlib import sha1
import hmac
import os
import re
import time


from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
method = "GET"

encoded_url = quote(url, safe='')
pattern = re.compile('[\W_]+')

oauth_consumer_key = os.getenv("API_KEY")
oauth_nonce = pattern.sub('', str(base64.b64encode(os.urandom(32))))

oauth_signature_method = "HMAC-SHA1"
oauht_timestamp = time.time()
oauth_version = "1.0"
oauth_token = os.getenv("ACCESS_TOKEN")
api_secret = os.getenv("SECRET") 
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

print(oauth_consumer_key)
print(oauht_timestamp)
print(oauth_nonce)
print(oauth_token)
print(encoded_url)

parameter_string = f"""oauth_consumer_key={oauth_consumer_key}&oauth_nonce={oauth_nonce}
                    &oauth_signature_method={oauth_signature_method}&oauth_token={oauth_token}
                    &oauth_version={oauth_version}&"""

base_string = method + "&" + encoded_url + "&" + parameter_string

signing_key = os.getenv("SECRET") + os.getenv("ACCESS_TOKEN_SECRET")

hashed = hmac.new(signing_key, base_string, sha1)