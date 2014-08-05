from flask import Flask
import urllib2

app = Flask(__name__)

# Super-simple Proxy

# Here we use the flexibility of routes in Flask to create a super simple proxy.
# It isn't a totally complete proxy, but it gets the basic idea correct and
# shows the power of flexible routes.


# Example:
# http://localhost:5000/https://news.ycombinator.com/
@app.route('/<path:requestPath>') # To make sure slashes are interpreted correctly, we define this route variable as being of the type "path".
def proxy(requestPath):
    print requestPath
    data = urllib2.urlopen(requestPath).read()
    return data

@app.route('/')
def root():
    return "Enter a url above to proxy it through."


if __name__ == '__main__':
    app.run(host= '0.0.0.0')
