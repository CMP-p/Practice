''''''
import json
import oauthlib
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