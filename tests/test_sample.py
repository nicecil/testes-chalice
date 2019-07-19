from chalicelib.domain.user import User
from chalicelib import routes
import pytest
import json
from app import app

def test_user_data(user_data):
	assert user_data.cidade == 'Rio de Janeiro'

def test_cartela(cartela):
	assert cartela.jogos[0]["Flamengo"] == 0
	assert cartela.jogos[1]["Bahia"] == 2

def test_user(user, user_data, cartela):
	assert user.get_cartela().jogos[0]["Flamengo"] == 0
	assert user.get_cartela().jogos[1]["Bahia"] == 2
"""	
def test_user_cartela():
	return

def test_user():
	nome = 'nickolas'
	user = User(nome)
	assert user.nome == 'nickolas'
	
def test_userreturn():
	nome = 'nickolas'
	route_return = routes.return_user(nome)
	assert ( route_return == {'User':'nickolas'} )

"""