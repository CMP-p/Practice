#Extra temporary
import requests
from requests_oauthlib import OAuth1

url = 'https://api.x.com/1/account/settings.json'

# Your key and secret
client_key = '...' 
client_secret = '...'
# The user authenticated key and secret you previously obtained
resource_owner_key = '...'
resource_owner_secret = '...'

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')
r = requests.get(url, auth=headeroauth)

