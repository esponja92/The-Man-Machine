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
	print "============= The Man Machine ============="
	print "Escrito e programado por Hugo Dantas\n"
	print "Gostaria de iniciar um novo jogo?"
	print "	a) Sim"
	print "	b) Nao"
	resposta = raw_input("")
	return resposta

