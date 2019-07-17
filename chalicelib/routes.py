from chalice import Blueprint
from chalicelib.user import User

root = Blueprint(__name__)

@root.route('/user/{key}')
def return_user(key):
	current_user = User(key, '1361379284')

	return ({'User':current_user.nome})