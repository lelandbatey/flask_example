from flask import Flask, request, json, render_template
import hashlib
import random
import json
import time


app = Flask(__name__)


room_structure = {
	"roomid": 
		{
			"users":
				{
					"usernameA" : 
						{
							"token": "tokenVal"
						},
					"usernameB":
						{
							"token": "tokenVal"
						}
				},
			"messages": 
				[
					"14-07-12 13:22:30 <usernameA> what's going on?",
					"14-07-12 13:22:35 <usernameB> Not much, things are good."
				],
			"alias": "Bob and Al's Example Chat Room"
		}
}


def rand_str(length = 9): # returns nice 9 character strings
    ourStr = ""
    i = 0
    while i < length:
        if random.randint(0,1): # If we get a 1, we do letters
            ourStr += chr(random.randint(ord('a'),ord('z')))
        else: # we get a 0, we do a number
            ourStr += str(random.randint(1,9))
        i += 1
    return ourStr

def get_hashval(inStr):
	sha = hashlib.new('sha1')
	sha.update(inStr)
	return sha.hexdigest()

def new_room():
	return {"messages":[],"alias":"","users":{}}



@app.route('/')
def root():
	return render_template('frontpage.html')



@app.route('/createroom', methods=['POST'])
def create_room():
	roomid = rand_str()
	room_structure[roomid] = new_room()
	room = room_structure[roomid]

	data = json.loads(request.data)

	room['alias'] = data['alias']

	return json.dumps({'roomid':roomid})



@app.route('/<roomid>/')
def return_room(roomid):
	if roomid not in room_structure:
		return "Room does not exist."
	alias = room_structure[roomid]['alias']
	return render_template('default_room.html',alias=alias)



@app.route('/<roomid>/get_conversation')
def return_conversation(roomid):
	if roomid not in room_structure:
		return json.dumps([None])

	messages = room_structure[roomid]['messages']
	return json.dumps(messages)



@app.route('/<roomid>/message', methods=['POST'])
def create_message(roomid):
	data = request.get_json()

	room = room_structure[roomid]
	if ('username' not in data) or (data['username'] not in room['users']):
		return json.dumps({
			"succeeded":False,
			"explanation":"username not found"
		})

	uname = data['username']

	if ('token' not in data) or (room['users'][uname]['token'] != data['token']):
		return json.dumps({
			"succeeded":False,
			"explanation":"token not valid"
		})

	# At this point we know the user exists, and the token is correct. Now we
	# assemble the message from the user, giving it the proper format.

	msgString = ""

	timeStr = time.strftime('%y-%m-%d %H:%M:%S')
	nameStr = "<{}>".format(uname)
	msgString = ' '.join([timeStr,nameStr,data['message']])

	room['messages'].append(msgString)

	return json.dumps({'succeeded': True,"explanation":None})



@app.route('/<roomid>/login',methods=['POST'])
def login(roomid):
	data = request.get_json()
	room = room_structure[roomid]

	failResponse = json.dumps({"succeeded": False,"token": None})

	if ('username' not in data) or\
		(data['username'] not in room['users']) or\
		('password' not in data):
		return failResponse

	user = room['users'][data['username']]
	hashval = get_hashval(data['password'])

	if hashval == user['token']:
		return json.dumps({
			'succeeded': True,
			'token': hashval
		})
	else:
		return failResponse




@app.route('/<roomid>/register', methods=['POST'])
def register(roomid):
	data = request.get_json()
	room = room_structure[roomid]

	failResponse = {"succeeded": False,"explanation": None}

	if ('username' not in data) or\
		(data['username'] in room['users']):
		failResponse['explanation'] = 'The specified user is not valid'
		return json.dumps(failResponse)

	room['users'][data['username']] = {}
	user = room['users'][data['username']]

	user['token'] = get_hashval(data[password])
	
	return json.dumps({'succeeded':True,"explanation":None})



if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)




