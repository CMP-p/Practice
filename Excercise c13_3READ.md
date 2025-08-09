''''''
(this document was written and can be saved as a .py file, and may be easier to read that way)
''''''
#Excercise c13_3
'''
I'm starting this document just to track the education. This section became even more difficult than when we were back in 
sockets and get requests. This one 'chapter' that utilizes Google maps API and Twitter API is VERY challenging, in comparison
to the rest of what I've been learning to this point. and does NOT feel like it's for everybody. However, since I'm pursuing
beyond the 'everybody' component, I'm looking into interacting with these api's organically. Teaching myself beyond the lesson.
Which should be fine, since that too, is a part of being a programmer. 

This specific set of instructions is dedicated to comprehending all the components in the X api required to pull and present
data from the `Reverse Chronological Home Timeline` The specific goal of THIS portion of this excercise is to print out my
timeline.
'''
'''
So far, I've learned that there are 3 portions involved in the X API regarding User Timeline, and the one I want, which follows
closest to what this lesson provides is called reverse chronological home timeline. And within there are a few components 
that I'll need to understand before I can properly code what the instructor has coded. I'm actually on day 2 or 3 of learning
this specific excercise. Now that I understand how to access twitters `developer console` "developer.x.com" for free, I'm
now learning about *what* Oauth is, and how to incorporate it into the program. I understand Oauth sends users to the targeted
apps authentication page, so that the developer can access content on behalf of the user, w/o need of their genuine creds.
'''
"""
I've moved further in my understanding on oauth, and it's library. It would seem that a Leah Culver created the oauth module 
when she was 25, right after getting her CS degree. But that was in 2007, and is actually outdated, especially because it 
relied on cgi, which was phased out in python 3.13. A new library, thats more modern and flowy is requests oauthlib, 
which I have now installed with pip, after uninstalling the oath. It would seem that building the URL request will be easier 
now. I know that there are 7 values that I need to deliver to the X API in order to properly authenticate a request. And 
that I have all 7 values. I just need to figure how to put them into the oauth module to construct the headers for me, to 
make the valid request. After which, I can move onto part 2/3 of this specific excercise
"""
'''
I'm deepening my understanding of the oauth libraries. It would seem that the way to go is indeed `requests_oauthlib` but
you must use it with the `requests` library, meaning, you cannot use urllib reliably, since this new library actually 
EXCPECTS the requests objects. Effectively making `requests` a dependency. Which is fine, since it's actually more user-friendly
and used commercially. establishing parameters are easier. If you REALLY want to, you could install legacy cgi, use regular
`oauth` library, but it'll be a legacy model you'll be following. Which isn't exactly great for understanding modern worklfows.

I also 'implemented' dr. Chucks `twurl` module, and commented/dissected on all of what it does in the temp.py file, so that
I know exactly what his code was doing, so that I can recreate similar results using `requests` and `requests_oauthlib`.

I also visited the documentation for `requests_oauthlib` to find out how to properly construct the requests. I copied in
all of the sections of code using the oauth1 helper, since it's supposedly more complicated, for more learning experience. 
'''
"""
Didn't have much time today, but I began to tear into the code I copied over and make it my own. compare the commits to see
what's changed. I also got a better understanding of class constructors.
"""
'''
I was reading through my previous documentation above, and noticed the twurl comments. While I do recall tearing that code
up to see what it all does, I now don't know where I put the commented version of it, if that exists. It's likely it was in
a previous temp.py commit that I've since overwritten. 

The past few attempts at understanding the oauth workflow has proven to be more cumbersome than a 4 hour once over for a
novice such as myself. 
'''
"""
I've now put in a solid 4-5 more hours (accerlated by copilot) into understanding these final parts of the code. 
I thought I was close, but I was so far. I've since found the Twurl that dr.chuck created. I added more comments, and 
separated it out into it's own file. Although, I've learned a lot today, and feel a little exauhsted, so I'm not sure my
comments are exactly easy to read. 

I've disected the final portion of the oauth cycle, and now have a fairly good understanding of how it works, back and forth
between X. Heres the simpleton breakdown: There are 3 parties- App, X, User. App ask X for special tokens, by showings its 
special tokens to X. (showing consumer key and secret in excahnge for a temporary, unverified key and secret). App then 
gives key to User, to go verify with X. User brings Key to X and shows X it's Key and Secret (usn and pass), and X gives
back a verifier token. User returns with token to App, and gives App the token. App takes verfier token, temporary 
unverified token and secret to X saying [Trust]. X says [Bet] after verifiying the verifier, and gives back a verified 
key and secret, which lets you act on users behalf. Now, App has verified tokens from X with users approval, and must use 
them with Apps own Key and Secret, to ask X for any informatino it wants from User, without User being present. App or User
can revoke permission at any time. If App resets their own Key and Secret, App will need to redo this process. App should 
store User Verified key and secret somewhere else.

I have also, today, after a couple more hours, gotten this to a point where I am able to work ONE endpoint. After all 
of this work, I was fortuneate to discover that the OAuth1.0 work flow is effectively being phased out altogether at X and
any endpoints that use V2.0 o must use OAuth 2.0, which is practically all of them. :,)
"""
'''
For some reason, the reverse chronological timeline DOES work with OAuth1.0 flow. Perhaps theres still some support for it,
but it has, seemingly, been officially sunset. I've named this file 'Extra Temporary' For now. I'll fix it up later, and 
the temp.py file will be transferred into a new file named somthine like 'Oauth 1.0 Floe for X enpoints' But less words.
'''
"""
For the past few days I've been trying to get the followers/followings endpoint to work, since the friendslist endpoint 
seems non-existant or restricted in some way. But according to this doc {https://docs.x.com/changelog#removal-of-follows-endpoints-from-basic-and-pro-tiers}
the endpoint has been restricted to Enterprise accounts ONLY. There is this endpoint {https://api.x.com/1.1/friends/list.json}
but I'm uncertain as it's a v1.1 endpoint and seems to have same or similar restrictions. ALSO I've noted that my monthly 
post cap is 100, where as all the documentation {https://docs.x.com/x-api/fundamentals/post-cap, https://docs.x.com/fundamentals/projects}
says you can consume up to 1,500 tweets. The discrepency is unfortunate, but just beware of your 100 read limit on Free accsounts.
That being said, this concludes my quest on this excercise. Hope it helps future learners!
"""
