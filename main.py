from Model import *
from View import *

primeiro_ano = PrimeiroAno.PrimeiroAno()
segundo_ano = SegundoAno.SegundoAno()
formatura = Formatura.Formatura()
final = Final.Final()

#Testando o plugin do GIT pro sublime

#booleanos para controle das fases
FIM_DO_JOGO = False
FIM_DA_FASE_1 = False
FIM_DA_FASE_2 = False
FIM_DA_FASE_3 = False

#hashmap para identificacao dos finais
finais = {"1aaaa":"final1", "1aaab":"final2", "1aab":"final1", "1baa":"final2", "1bab":"final1", "1bba":"final1", "1bbb":"final2"}

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


def iniciaCena(fase):
	OutIn.output(fase.getIntro())
	OutIn.delay()
	return fase.getCena1()

def decideFinal(cena_atual):
	nome_final = finais[cena_atual.getNome()]
	if(nome_final == "final1"):
		OutIn.output(final.getFinal1())
	else:
		OutIn.output(final.getFinal2())
	OutIn.delay()
	
#Chama tela de abertura do View, que deve retornar com a opcao do jogador
opcao = TelaDeAbertura.abertura()

while(opcao == 'a'):

	#Inicializa as variaveis para o inicio do jogo
	FIM_DA_FASE_1 = False
	FIM_DA_FASE_2 = False
	FIM_DA_FASE_3 = False
	FIM_DO_JOGO = False

	#pontos conscienciais iniciais
	pontos = 12

	#loop principal
	while(not(FIM_DO_JOGO)):
		if(not(FIM_DA_FASE_1)):
			cena_atual = iniciaCena(primeiro_ano)
		elif(not(FIM_DA_FASE_2)):
			cena_atual = iniciaCena(segundo_ano)
		elif(not(FIM_DA_FASE_3)):
			cena_atual = iniciaCena(formatura)
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

			#Todos os booleanos devem indicar o fim do jogo
			FIM_DA_FASE_1 = True
			FIM_DA_FASE_2 = True
			FIM_DA_FASE_3 = True
			FIM_DO_JOGO = True

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
				#Se a fase 3 acabou, o jogo tambem
				FIM_DO_JOGO = True
				decideFinal(cena_atual)
	#Chama tela de abertura do View de novo
	opcao = TelaDeAbertura.abertura()