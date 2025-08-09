# Testing X API endpoints (see choices)

### WARNING This uses OAuth 1.0 Flow, which is offcially sunset and depricated from X. But still works at this 
### endpoint, as well as a few other endpoints. This code may need to be altered to follow OAuth 2.0 with PKCE flow
import requests
from requests_oauthlib import OAuth1
import json

baseurl = 'https://api.x.com'
userID = None
r = None

# Authentication Layer
# Your key and secret
client_key = input('input client_key...\n') 
client_secret = input('input client_secret...\n')

# This block is unnecessary if UserID is defined in the code.
while True:
    try:
        userID = str(int(input('input user/resource owner ID...\n\n')))
        break
    except: 
        print('Error. User ID must be intergers only.\n')
        continue

# The user authenticated key and secret you previously obtained
resource_owner_key = input('input resource_owner_key...\n')
resource_owner_secret = input('input resource_owner_secret...\n')
print('Fetching Authentication...\n\n')

# url = baseurl + f'/2/users/{userID}/timelines/reverse_chronological'
headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')

''''''''''''
# Endpoint Layer
params = None

while True:
    choices = {'1':'/1.1/account/verify_credentials.json',
               '2':'1/account/settings.json',
               '3':f'/2/users/{userID}/timelines/reverse_chronological',
               '4':f'/2/users/{userID}/following',
               '5': '/1.1/friends/list.json',
               'q':'\nTask finished. Closing Program...\n'}
    choice = input('Enter 1 for credential validation, 2 for settings-(requires OAuth2.0), 3 for timeline, 4 for followings (requires Enterprise), 5 for friendslist.\nEnter Q to quit\n').lower()
    if choice not in choices:
        print('Invalid entry. Please try again.','\n'*3)
    elif choice == 'q':
        print("Closing Program...") 
        r.close()
        quit()
    elif choice == '3' or '4':
        params = {'max_results':1}
    elif choice == '5':
        params = {'count':'1',
                   'user_id':userID}        

    protected_url = baseurl + choices.get(choice)
    print(f'Fetching {protected_url}... \n...\n') #debug line
    try:
        r = requests.get(url=protected_url, auth=headeroauth, params=params)
    except requests.RequestException as e:
        print('bad dog!!! \n',e,'\n')
        continue
    
    js  = json.loads(r.content.decode())
    print('Requested content:','\n',json.dumps(js, indent = 3), '\n'*2) 
    print('-'*25)#sep
    #heads = json.loads((r.headers.decode()))
    print(json.dumps(dict(r.headers), indent= 3), '\n\n')

# [x] collect the other endpoints from the excercise, - friends list (doesn't exist anymore, using following list)
# [x] test them, 
# [x] finish merging these two codes, 
# [x] upload the oauth as it's own file,
# [x] print headers
# [] organize directory