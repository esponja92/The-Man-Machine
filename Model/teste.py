"""
Script para testes gerais

"""
from Cena import *
from PrimeiroAno import *
from SegundoAno import *
from Formatura import *
from Final import *

def gameloop(cena_atual):
	while((cena_atual.getCenaFilhaA() != None) or (cena_atual.getCenaFilhaB() != None)):
		escolha = raw_input(cena_atual.getTexto())
		if (escolha == 'a'):
			cena_atual = cena_atual.getCenaFilhaA()
		elif (escolha == 'b'):
			cena_atual = cena_atual.getCenaFilhaB()
		elif ((escolha == 'c') and (cena_atual.getCenaMae() != None)):
			cena_atual = cena_atual.getCenaMae()
		else:
			print "Escolha apenas uma das opcoes disponiveis.\n"
	print cena_atual.getTexto()

primeiro = PrimeiroAno()
segundo = SegundoAno()
formatura = Formatura()
finais = Final()

cena_atual = primeiro.getCena1()
print primeiro.getIntro()
raw_input("Pressione Enter para continuar...")
gameloop(cena_atual)

raw_input("Pressione Enter para continuar...")

cena_atual = segundo.getCena1()
print segundo.getIntro()
raw_input("Pressione Enter para continuar...")
gameloop(cena_atual)

raw_input("Pressione Enter para continuar...")

cena_atual = formatura.getCena1()
print formatura.getIntro()
raw_input("Pressione Enter para continuar...")
gameloop(cena_atual)

raw_input("Pressione Enter para continuar...")

