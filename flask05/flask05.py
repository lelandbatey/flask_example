from flask import Flask, request, json, render_template
import random
from pprint import pprint

app = Flask(__name__)

baseHost = "http://localhost:5000/"
dataDict = {} # This dictionary will hold all of our data in a pretty 

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

# Given any data being sent via a post, stores that data and generates a shorturl to access it.
@app.route('/addText/', methods=['POST'])
def addText():
    shortUrl = randomString()
    dataDict[shortUrl] = request.data
    return baseHost+shortUrl

# Renders the "data" template with the appropriate text from our `dataDict` storage.
@app.route('/<shortUrl>')
def getData(shortUrl):
    return render_template("data.html",myData=dataDict[shortUrl])

# Just renders the vanilla page.
@app.route('/')
def root():
    return render_template('frontpage.html')

if __name__ == '__main__':
    app.debug = True
    app.run()


