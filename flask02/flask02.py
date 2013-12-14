from flask import Flask

app = Flask(__name__)

# -- Routes --
#
# Routes are how you define the URI's that can be accessed, as well as how you
# handle them.
#
# Examples:

# Root page:
# http://localhost:5000/
@app.route('/')
def root():
    return "This is the default page."


# Access here:
# http://localhost:5000/single_variable
@app.route('/<some_variable>')
def vars(some_variable):
    return "We've been given a variable:\n" + some_variable


# Access Here:
# http://localhost:5000/stuff/some_string1/another-string2
@app.route('/stuff/<var1>/<var2>')
def multi_vars(var1,var2):
    return "Variable #1: " + var1\
    +" Variable #2: "+ var2

if __name__ == '__main__':
    app.run()

