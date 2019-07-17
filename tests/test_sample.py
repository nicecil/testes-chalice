from chalicelib.user import User
from chalicelib import routes
import pytest
import json
from app import app

"""
@pytest.fixture
def gateway_factory():
	from chalice.config import Config
	from chalice.local import LocalGateway

	def create_gateway(config=None):
		if config is None:
			config = Config()
		return LocalGateway(app, config)
	return create_gateway

def test_index(gateway_factory):
	nome = 'nickolas'
	gateway = gateway_factory()
	response = gateway.handle_request(method='GET', path='/user/{nome}',headers={}, body='')
	#assert response['statusCode'] == 200
	assert json.loads(response['body']) == dict([('user', nome)])
"""

def test_user():
	nome = 'nickolas'
	user = User(nome)
	assert user.nome == 'nickolas'
	
def test_userreturn():
	nome = 'nickolas'
	route_return = routes.return_user(nome)
	assert ( route_return == {'User':'nickolas'} )

