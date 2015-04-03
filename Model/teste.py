"""
Script para testes gerais

"""

from Cena import *
from PrimeiroAno import *

primeiro_ano = PrimeiroAno()
cena_atual = primeiro_ano.getCena1()

while((cena_atual.getCenaFilhaA() != None) or (cena_atual.getCenaFilhaB() != None)):
	escolha = raw_input(cena_atual.getTexto())
	if (escolha == 'a'):
		cena_atual = cena_atual.getCenaFilhaA()
	elif (escolha == 'b'):
		cena_atual = cena_atual.getCenaFilhaB()
	else:
		print "Escolha apenas uma das opcoes disponiveis.\n"
print cena_atual.getTexto()
