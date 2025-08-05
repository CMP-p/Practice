#import urllib.error, urllib.parse, urllib.request
# Foregoing urllib as it's incompatible with requests_oauthlib AND is legacy to `oauth` but requires legecy import of cgi
import requests
## Using OAuth1Session
# from requests_oauthlib import OAuth1Session # This route is easier, allegedly. I choose pain

# Using OAuth1 auth helper
from requests_oauthlib import OAuth1
import json #to be used


# consumer == client in refernce here, obtained via app in dev portal on X
client_key = input('Input client/consumer key: ')
client_secret = input('input client/consumer secret: ')
print('\n\n') # just cus


# These are variables that come up later, predefined as None, but written here for your(my) understanding
# These value will be retunred by the codeblock below this as part of a query string. Whatever that is.
resource_owner_key = None 
resource_owner_secret = None 


# This is where you pass your api key & secret, and get tokens in place.

oauth = OAuth1(client_key=client_key, client_secret=client_secret, callback_uri = 'oob')
r = None
try: 
    r = requests.post(url="https://api.x.com/oauth/request_token", auth=oauth)
except: 
    print(f'App failure \n Reason: \n{requests.RequestException()}')
    exit
"""REALLY IMPORTANT TO NOTE HERE. WHILE DOCUMENTATION DOES NOT METNION IT, YOU NEED TO DECODE THE CONTENT IN VARIABLE r
BEFORE PARSING. THE RETURNED STRING IS RAW BYTES OR USE THE .text METHOD"""
print(type(r.content), r.content, "NOT DECODED, RAW BYTES. NEEDS DECODING BEFORE PARSING (debug line)\n\n") #debug line
from urllib.parse import parse_qs
credentials = parse_qs(r.content.decode()) #turns a qs into dict
print('Debug line:\n:', credentials,type(credentials),'\n\n') #debug line
resource_owner_key = credentials.get('oauth_token')[0] #gets passed to user to be verfied
resource_owner_secret = credentials.get('oauth_token_secret')[0] # this too ^
print (f'Debug lines:\n{resource_owner_key}', f'\n{resource_owner_secret}\n\n') #debug line


# constructing the url to redirect the app user to 'sign' and return a token to access other endpoints on 
# their behalf.
authorize_url = 'https://api.x.com/oauth/authorize' + '?oauth_token='
authorize_url = authorize_url + resource_owner_key
print('Please go here and authorize: ', authorize_url)
verifier = input('Please input the verifier here when done: ')


# creating a new OAuth1 object instance with the newly obtained verfier and getting signed tokens returned
oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)
r = requests.post(url='https://api.x.com/oauth/access_token', auth=oauth)
print(type(r.content),r.content,'debug line: Needs to be decoded again \n\n') #debugging line, alternatively use r.text()
credentials = parse_qs(r.content.decode())
print('Credentials:', credentials, '\n\nDebug line') # Debug line DELETE THIS LINE BEFORE PUSHING, JERK
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]
print('\n','Record these for later use!', f'resource_owner_key, {resource_owner_key}, resource_owner_secret, {resource_owner_secret}')
print('\n'*2)
# Done with authenticating! Now we can visit any of the endpoints.
# Be sure to store the resource_owner_key and resource_owner_secret somewhere secure, they don't expire and can be reused
# without having to re-authenticate.


# This block is how you'll interact with any of the authentication-protected endpoints. 
'''
oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret
                   signature_type='auth_header') # X requires this
r = requests.get(url=protected_url, auth=oauth) #replace protected_url with the url endpoint you want to access
'''

oauth = OAuth1(client_key,
                client_secret=client_secret,
                resource_owner_key=resource_owner_key,
                resource_owner_secret=resource_owner_secret,
                signature_type='AUTH_HEADER')   # X requires header signature

while True:
    choices = {'1':'https://api.twitter.com/1.1/account/verify_credentials.json',
               '2':'https://api.x.com/1/account/settings.json',
               'q':'\nQuitting Program...\n'}
    choice = input('Enter 1 for credential validation. Enter 2 for settings-(requires OAuth2.0) \nEnter Q to quit\n').lower()
    if choice not in choices:
        print('Invalid entry. Please try again.','\n'*3)
        continue
    print(choices.get(choice),'\n'*2)
    if choice == 'q': quit()

    protected_url = choices.get(choice)
    try:
        r = requests.get(url=protected_url, auth=oauth)
    except requests.RequestException as e:
        print('bad dog!!! \n',e,'\n')
        continue

    print(r.content.decode(), '\n'*2) #!!!change this to Json and pretty print it

'''
Referenced sites:

https://requests-oauthlib.readthedocs.io/en/latest/oauth1_workflow.html
https://docs.x.com/fundamentals/authentication/oauth-1-0a/authorizing-a-request
https://docs.x.com/fundamentals/authentication/api-reference
https://docs.x.com/x-api/posts/timelines/quickstart/reverse-chron-quickstart
https://developer.x.com/apitools/api
https://www.youtube.com/watch?v=2c7YwhvpCro 
'''