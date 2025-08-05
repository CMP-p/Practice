#Timeline for user, Revers chronological order.

### WARNING This uses OAuth 1.0 Flow, which is offcially sunset and depricated from X. But still works at this 
### endpoint, as well as a few other endpoints. This code may need to be altered to follow OAuth 2.0 with PKCE flow
import requests
from requests_oauthlib import OAuth1
import json

baseurl = 'https://api.x.com'
userID = None

# Your key and secret
client_key = input('input client_key...\n') 
client_secret = input('input client_key...\n')

# This block is unnecessary if UserID is defined in the code.
while True:
    try:
        userID = int(input('input user/resource owner ID...\n\n'))
        break
    except: 
        print('Error. User ID must be intergers only.\n')

# The user authenticated key and secret you previously obtained
resource_owner_key = input('input resource_owner_key...\n')
resource_owner_secret = input('input resource_owner_secret...\n')
print('Fetching Data...\n\n')

url = baseurl + '/2/users/{userID}/timelines/reverse_chronological'
headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')
r = requests.get(url, auth=headeroauth, params={'max_results':5})
data = json.loads(r.content)
print(json.dumps(data, indent=3))

r.close()
print('\nTask finished. Closing Program...\n')

