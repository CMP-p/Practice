
#Below is Dr. Chucks 'Twurl' module, which implements the 2007 oauth library
#I'm deconstructing it to be able to implement the workflow into a working form of the x api using reques_oauthlib
import urllib.request, urllib.error, urllib.parse
import oauth
import legacy_cgi
import hidden

def augment(url, parameters):
    # imported dict containing cosumer key, consumer secret, token key and token secret. You don't need the hidden file
    # if you're just locally testing. These keys and tokens are found on your X app dev dashboard in API section.
    secrets = hidden.oauth()
    #giving oauth consumer(client/app) info
    consumer = oauth.OAuthConsumer(secrets['consumer_key'],
                                   secrets['consumer_secret'])
    #giving oath your personal token info
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])

    # Calling oauth request module, implementing oauth consumer and token objects, and using this functions variables
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
