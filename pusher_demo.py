import pusher

pusher.app_id = '123'
pusher.key = 'xxx'
pusher.secret = 'yyy'
username = "User"

def reload():
	p = pusher.Pusher()
	p['simon'].trigger('reload', {'some': 'data'})

	
def update(message):
	p = pusher.Pusher()
	p['simon'].trigger('event', {'message': message, "uname" : username})
