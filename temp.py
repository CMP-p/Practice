#import urllib.error, urllib.parse, urllib.request
# Foregoing urllib as it's incompatible with requests_oauthlib AND is legacy to `oauth` but requires legecy import of cgi
import requests
## Using OAuth1Session
# from requests_oauthlib import OAuth1Session #This route is easier, allegedly. I choose pain

# Using OAuth1 auth helper
from requests_oauthlib import OAuth1

# consumer == client in refernce here, obtained via app in dev portal on X
client_key = '...'
client_secret = '...'

# These are variables that come up later, predefined as None, but written here for your understanding
# These value will be retunred by the codeblock below as part of a query string. Whatever that is.
resource_owner_key = None 
resource_owner_secret = None 

#This is where you pass your api key & secret, and get tokens in place.
oauth = OAuth1(client_key=client_key, client_secret=client_secret)
r = requests.post(url="https://api.x.com/oauth/request_token", auth=oauth)
print(r.content.decode()) #debug line
from urllib.parse import parse_qs
credentials = parse_qs(r.content.decode()) #turns a qs into dict
print(credentials,type(credentials)) #debug line
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]
print (f'\n{resource_owner_key}', f'\n{resource_owner_secret}') #debug line

# constructing the url to redirect the app user to 'sign' and return a token so we can access other endpoints on 
# their behalf via cocatination.
authorize_url = 'https://api.x.com/oauth/authorize' + '?oauth_token='
authorize_url = authorize_url + resource_owner_key
print('Please go here and authorize,', authorize_url)
verifier = input('Please input the verifier')

'''
oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)
r = requests.post(url=access_token_url, auth=oauth)
r.content
"oauth_token=6253282-eWudHldSbIaelX7swmsiHImEL4KinwaGloHANdrY&oauth_token_secret=2EEfA6BG3ly3sR3RjE0IBSnlQu4ZrUzPiYKmrkVU"
credentials = parse_qs(r.content)
resource_owner_key = credentials.get('oauth_token')[0]
resource_owner_secret = credentials.get('oauth_token_secret')[0]

oauth = OAuth1(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret)
r = requests.get(url=protected_url, auth=oauth)

###
url = 'https://api.twitter.com/1/account/settings.json'

client_key = '...'
client_secret = '...'
resource_owner_key = '...'
resource_owner_secret = '...'

headeroauth = OAuth1(client_key, client_secret,
                     resource_owner_key, resource_owner_secret,
                     signature_type='auth_header')
r = requests.get(url, auth=headeroauth)
###

urllib.request.urlopen(url, auth=headeroauth)

#Below is Dr. Chucks 'Twurl' module, which implements the 2007 oauth library
#I'm deconstructing it to be able to implement the workflow into a working form of the x api using reques_oauthlib
def augment(url, parameters):
    # imported dict containing cosumer key, consumer secret, token key and token secret
    secrets = hidden.oauth()
    #giving oauth consumer(client) info
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    #giving oath token infor
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    # Calling oauth request module, implementing oauth consumer and token objects, and using parameters defined externally
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
                    token=token, http_method='GET', http_url=url,
                    parameters=parameters)
    # signing the request using X's required HMAC_SHA1 via oauths sign request method
    oauth_request.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),
                               consumer, token)
    return oauth_request.to_url()
#part of twurl vvvvvv
def test_me():
    print('* Calling Twitter...')
    #the dict below are the parameters for oauth requests for consumer and token method
    #the url is seemingly constructed with headers aswell.
    url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                  {'screen_name': 'drchuck', 'count': '2'})
    print(url)
    connection = urllib.request.urlopen(url)
    data = connection.read()
    print(data)
    # pulling headers returned from opening the url from a variable named connections, usually DR. chuck names this fhandle
    headers = dict(connection.getheaders())
    print(headers)
'''
