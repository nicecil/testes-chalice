import json


class User:

	def __init__(self, nome, cpf=None, email=None, endereco=None, telefone=None):
		self.nome = nome
		self.cpf = cpf
		self.email = email
		self.endereco = endereco
		self.telefone = telefone


	def user_to_json(self):
		dict_user = {'nome':self.nome,
					  'cpf':self.cpf,
					  'email':self.email,
					  'endereco':self.endereco,
					  'telefone':self.telefone}
		return dict_user
	