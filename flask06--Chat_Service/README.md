Flask-Chat
==========

While the prior examples are extremely simple, this project has a much higher degree of complexity. This document exists to outline my thoughts as I write this, in an effort to help those who want to learn from it.


## Url Scheme

	http://sitename/random-room-id/

## API

The site is composed of a collection of rooms, each with a randomly generated `roomid` and a user-generated `roomalias`. The `roomalias` is entered by the user who creates it when it is created, but cannot be changed once the room is created.

### Users and Authentication

To send a message in a room, a user must first log-in. If the user doesn't have an account, then they must create one. To create an account, they must enter a username, then enter the same password twice. Once that password's been entered, they must then log-in.

It should be noted that users exist on a per-room basis, not carrying over from one room to another. That is to say, if "Tom" creates an account "tom1" in `Room A` then goes to `Room B`, the user "tom1" will not exist in `Room B`.

#### User Creation

The double password verification step happens on the client side in javascript, then the final message is sent like so:

	URL:
		http://sitename/random-room-id/register
	
	Data:
		{
			"username": "name typed in by user",
			"password": "plaintext password here"
		}
	
	Response:
	
		If successful:
			{
				"succeeded": true,
				"explanation": null
			}

		If unsuccessful:
			{
				"succeeded": false,
				"explanation": "explanation of why user couldn't be created"
			}

The field "explanation" is intended to be shown to the user.


#### Logging In

The login step consists of the `username` and password being gathered on the client side, then sent to the server in a format like so:

	URL:
		http://sitename/random-room-id/login
	
	Data:
		{
			"username": "name typed in by user",
			"password": "plaintext password here"
		} 
	
	Response:

		If successful:
			{
				"succeeded": true,
				"token": "token value"
			}

		If unsuccessful:
			{
				"succeeded": false,
				"token": null
			}

The `token` variable is the hash of the users password, and is sent with every message to verify that the user is logged in.


### Getting the Conversation

Gets the last 50 messages of the conversation in that room. What it looks like:

	URL:
		http://sitename/random-room-id/get_conversation
	
	Data:
		None, is a GET request

	Response:
		[
			"14-07-12 13:22:30 <usernameA> what's going on?",
			"14-07-12 13:22:35 <usernameB> Not much, things are good."
		]

### Sending a Message

Format of a message for a user:

	URL:
		http://sitename/random-room-id/message

	Data:
		{
			"username": "name of user",
			"token" : "token value",
			"message": "escaped message contents"
		}

	Response:

		If successful:
			{
				"succeeded": true,
				"explanation": null
			}

		If unsuccessful:
			{
				"succeeded": false,
				"explanation": "explanation of why a message couldn't be processed"
			}

The field "explanation" is intended to be shown to the user.


### Creating a Room

Creating a room is very simple. The user enters the room-alias they'd like to have created, then sends that message to the server. Example message:

	URL:
		http://sitename/createroom
	
	Data:
		{
			"alias": "desired room alias"
		}

	Response:
		{
			"roomid": "roomid"
		}

It should be noted, there is no "success" or "failure" clause when creating a room. Since the actual `roomid` is randomly generated to be (nearly) unique, and rooms do not interfere with one another, a room can always be created.

## Backend Structure

On the backend, there's a single dictionary holding all the all the data this application will be using. In an application that's not just a toy, you'd probably use a database to persist data across restarts, but I leave that as an exercise for the reader : ).

Here's what the structure looks like:

	{
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



## Implementation Notes

Something I've tried to do here is to structure this so that the backend of the server never has to know what the root URL is that it's running under. Because of this, things like page-redirects for users need to be handled inside Javascript. 

For example, lets say a user creates a room to chat in. The server only responds with a `roomid`, not the url where that room can be found at. The Javascript on that page is going to have to construct that url then redirect the user there by itself.

