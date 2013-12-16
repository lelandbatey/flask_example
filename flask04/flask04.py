from flask import Flask, redirect
import random

app = Flask(__name__)


urlDict = {} # Will be used to store our shorturls and their cooresponding destinations
invUrlDict = {} # The inverse of urlDict. Since both shorturl and destination are supposed to be unique, we need this bi-directional lookup.

# urlDict example:
#     {
#         shortUrl : destination
#     }

# inUrlDict example:
#     {
#         destination: shortUrl
#     }

baseHost = "http://localhost:5000/" # The default hostname to access this app. Assumes running on localhost by default.

def randomString(): # returns nice 9 character strings
    ourStr = ""
    i = 0
    while i < 9:
        if random.randint(0,1): # If we get a 1, we do letters
            ourStr += chr(random.randint(ord('a'),ord('z')))
        else: # we get a 0, we do a number
            ourStr += str(random.randint(1,9))
        i += 1
    return ourStr


## Basic Url-shortner
# Add a redirect using http://localhost:5000/(some_url_here). For example:
#
#    http://localhost:5000/a/https://www.google.com/
#
# Then visit the given shorturl to be automatically redirected:
#
#    http://localhost:5000/6s14n5obf
#    /* Redirects to google.com (at least for me) */
#

@app.route('/a/<path:destination>')
def addUrl(destination):
    print destination

    if destination in invUrlDict: # If the destination already has a short url, return that.
        return baseHost+invUrlDict[destination]
    else: # Else, create new shortUrl, store it, and return the shortUrl.
        shortUrl = randomString()
        urlDict[shortUrl] = destination
        invUrlDict[destination] = shortUrl
        return baseHost+shortUrl

@app.route('/<shortUrl>')
def urlRedirect(shortUrl):
    if shortUrl in urlDict:
        return redirect(urlDict[shortUrl], code=302)
    else:
        return "Error, not valid shorturl", 404

if __name__ == '__main__':
    app.run()


