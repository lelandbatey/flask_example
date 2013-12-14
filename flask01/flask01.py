from flask import Flask

# Standard boilerplate 
app = Flask(__name__)

@app.route('/')
def root():
    return "Whoo, first page!"

# __name__ will only be '__main__' if this python script is the main script
# being run. If it were imported from somewhere else, this check would fail
if __name__ == '__main__':
    app.run() # Makes this thing run (by default only on localhost on port 5000)

# Access here: http://localhost:5000/
