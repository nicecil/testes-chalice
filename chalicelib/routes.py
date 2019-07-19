from chalice import Blueprint
from chalicelib.domain.user import User
import json

root = Blueprint(__name__)

OBJECTS = {
}

@root.route('/user', methods=['PUT','POST'])
def post_user():
	from app import app
	request = app.current_request
	body = request.json_body
	key = body['email']
	
	if request.method == 'POST':
		if key in OBJECTS.keys():
			return {'Usuario ja cadastrado':200}
		else:
			user = User(body['nome'],
						body['cpf'],
						body['email'],
						body['endereco'],
						body['telefone'])
			OBJECTS[key] = user
			return {"OBJECT SUCCESSFULLY ADDED":key}
	

@root.route('/user/{email}', methods=['GET'])
def get_user(email):
	if email in OBJECTS.keys():
		return {email: OBJECTS[email].user_to_json()}
	else:
		return {'Usuario nao encontrado':email}


@root.route('/user', methods=['GET'])
def get_all():
	user_list = []
	for email in OBJECTS.keys():
		user_list.append( {email: OBJECTS[email].user_to_json()} )

	return user_list

"""def return_all():
	return OBJECTS"""
"""
@root.route('/user/{key}')
def return_user(key):
	current_user = User(key, '1361379284')

	return ({'User':current_user.nome})
"""



