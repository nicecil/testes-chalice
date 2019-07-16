from chalice import Blueprint


root = Blueprint(__name__)

@root.route('/user/{key}')
def return_user(key):
	return ({'User':key})