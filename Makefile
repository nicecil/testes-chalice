.PHONY: deploy tests

deploy:
	chalice deploy
tests:
	@python pytest testes

local:
	chalice local