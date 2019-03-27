from twilio.rest import Client
account_sid = 'ACb91f79cdba2d7bf2cf85f8cb71fc3d2e'
auth_token='c6575d2a5c5cf2bb47fd58925d7dd43d'

def textmyself(message):
	twilioCli = Client(account_sid,auth_token)
	twilioCli.messages.create(
				body = message,
				from_='+19012455374',
				to='+19018969073'	
			)
