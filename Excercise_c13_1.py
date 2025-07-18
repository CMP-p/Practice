# This is an alternate I created to replace the excercise on this chapter, because google now requires API keys, which
# link to payment. Which is fine because it's still free but the $300 credit expires in 90 days, so I didn't create an
# account just yet. It's a mixture of being cheap, resourceful, and engaging in growth oriented challenge.
''''''
import json
import urllib.parse, urllib.error, urllib.request
''''''

apiurl = 'https://nominatim.openstreetmap.org/search?'
failed_attempt = 0

while True: 
    address = input('Enter location dawg: ')
    if len(address) < 1: break
    
    #url enconding with query and params
    url = apiurl + urllib.parse.urlencode({'format':'json',
                                               'q':address
                                               })

    print('Retrieving', url)
    urlHand = urllib.request.urlopen(url)
    data = urlHand.read().decode()
    js = json.loads(data) #converts inbound Json data to Python

    if len(js) == False:
        print('Error: Not a valid query')
        failed_attempt += 1
        if failed_attempt > 3: 
            print('To many failed attempts, please try again later.')
            break
        continue
    else: 
        print(len(data), 'charachters to process')

    #find lat, lang and location
    print('Results: \n', json.dumps(js, indent=4))

    lat, lon, loc = (float(js[0]['lat']),
                     float(js[0]['lon']),
                     js[0]['display_name'])
    print ('lat:',lat,
           'lon:', lon, 
           'loc:', loc)
    urlHand.close()
    break



