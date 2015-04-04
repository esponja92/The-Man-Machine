from Model import *
from View import *

def cenaDecisao(cena_atual, pontos):
	OutIn.output(cena_atual.getTexto())
	OutIn.output("	c) Voltar a cena anterior\n")
	resposta = OutIn.input()
	if (resposta == "a"):
		cena_atual = cena_atual.getCenaFilhaA()
		pontos = pontos - 1
	elif (resposta == "b"):
		cena_atual = cena_atual.getCenaFilhaB()
		pontos = pontos - 1
	elif ((resposta == "c")and(cena_atual.getCenaMae() != None)):
		cena_atual = cena_atual.getCenaMae()
		pontos = pontos - 1
	else:
		OutIn.opcaoInvalida()
	return cena_atual, pontos

primeiro_ano = PrimeiroAno.PrimeiroAno()
segundo_ano = SegundoAno.SegundoAno()
formatura = Formatura.Formatura()
final = Final.Final()

#pontos conscienciais
pontos = 12
FIM_DO_JOGO = False
FIM_DA_FASE_1 = False
FIM_DA_FASE_2 = False
FIM_DA_FASE_3 = False

#Chama tela de abertura do View, que deve retornar com a opcao do jogador
opcao = TelaDeAbertura.abertura()

#Se a opcao for comecar o jogo, o codigo nem entra no loop principal
if (opcao == 'b'):
	FIM_DO_JOGO = True

#loop principal
while(not(FIM_DO_JOGO)):
	if(not(FIM_DA_FASE_1)):
		cena_atual = primeiro_ano.getCena1()
		OutIn.output(primeiro_ano.getIntro())
		OutIn.delay()
	elif(not(FIM_DA_FASE_2)):
		cena_atual = segundo_ano.getCena1()
		OutIn.output(segundo_ano.getIntro())
		OutIn.delay()
	elif(not(FIM_DA_FASE_3)):
		cena_atual = formatura.getCena1()
		OutIn.output(formatura.getIntro())
		OutIn.delay()
	#Se o codigo entrar aqui, significa que o jogo acabou
	else:
		cena_atual = Cena.Cena("", None)

	#Condicao para encerrar a fase
	while(((cena_atual.getCenaFilhaA() != None)or(cena_atual.getCenaFilhaB() != None))and(pontos > 0)):
		cena_atual,pontos = cenaDecisao(cena_atual, pontos)

	#testa se o personagem morreu
	if(pontos == 0):																		
		OutIn.output(final.getFinal3())
		OutIn.delay()

	#O ultimo paragrafo da fase
	else:
		OutIn.output(cena_atual.getTexto())
		OutIn.delay()
		
		#Ajusta o booleano indicando o final da fase
		if(not(FIM_DA_FASE_1)):
			FIM_DA_FASE_1 = True
		elif(not(FIM_DA_FASE_2)):
			FIM_DA_FASE_2 = True
		elif(not(FIM_DA_FASE_3)):
			FIM_DA_FASE_3 = True

		#Fim do jogo
		else:
			FIM_DO_JOGO = True			

