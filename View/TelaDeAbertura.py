import os

def clearScreen():
	try:
		os.system('cls')
	except e:
		print "Sistema Operacional Linux"
	else:
		os.system('clear')

def abertura():
	clearScreen()
	print "O jogo comecou! Quer jogar?"
	print "a) Sim"
	print "b) Nao"
	resposta = raw_input("")
	return resposta

