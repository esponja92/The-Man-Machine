#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Model import *
from View2 import *
from pygame.locals import *
import pygame as pg

primeiro_ano = PrimeiroAno.PrimeiroAno()
segundo_ano = SegundoAno.SegundoAno()
formatura = Formatura.Formatura()
final = Final.Final()

nfrases = 7

#hashmap para identificacao dos finais
finais = {"1aaaa":"final1", "1aaab":"final2", "1aab":"final1", "1baa":"final2", "1bab":"final1", "1bba":"final1", "1bbb":"final2"}

#cor da letra
yellow = (255, 255, 0)

#dimensao da tela
dimen = (640, 480)

#tamanho da fonte
tfonte = 35

pg.init()

screen = pg.display.set_mode(dimen, FULLSCREEN)
pg.display.set_caption("The Man Machine")
myfont = pg.font.SysFont("Computer Pixel-7", tfonte)

def cenaDecisao(cena_atual, pontos, MUSIC_ON):
	if((cena_atual.getMusica() != None)and(MUSIC_ON == False)):
		MUSIC_ON = True
		io.play_music(pg, cena_atual.getMusica())
	io.escreve(cena_atual.getTexto(),pg, myfont, screen, yellow, nfrases)
	resposta = io.esperaTeclaPressionada(pg)
	if (resposta in range(256)):
		resposta = chr(resposta)
		if (resposta == "a"):
			cena_atual = cena_atual.getCenaFilhaA()
			pontos = pontos - 1
		elif (resposta == "b"):
			cena_atual = cena_atual.getCenaFilhaB()
			pontos = pontos - 1
		elif ((resposta == "c")and(cena_atual.getCenaMae() != None)):
			cena_atual = cena_atual.getCenaMae()
			pontos = pontos - 1
		return cena_atual, pontos
	io.escreve("Opção indisponível.\n",pg, myfont, screen, yellow, nfrases)
	io.delay(pg, myfont, screen, yellow)
	return cena_atual, pontos


def iniciaCena(fase):
	io.escreve(fase.getIntro(),pg, myfont, screen, yellow, nfrases)
	io.delay(pg, myfont, screen, yellow)
	return fase.getCena1()

def decideFinal(cena_atual):
	nome_final = finais[cena_atual.getNome()]
	if(nome_final == "final1"):
		io.escreve(final.getFinal1(),pg, myfont, screen, yellow, nfrases)
		io.play_music(pg, final.getMusicaF1())
	else:
		io.escreve(final.getFinal2(),pg, myfont, screen, yellow, nfrases)
		io.play_music(pg, final.getMusicaF2())

def loopPrincipal():

	#Inicializa as variaveis para o inicio do jogo
	FIM_DA_FASE_1 = False
	FIM_DA_FASE_2 = False
	FIM_DA_FASE_3 = False
	FIM_DO_JOGO = False

	MUSIC_ON = False

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
			cena_atual,pontos = cenaDecisao(cena_atual, pontos, MUSIC_ON)

		#testa se o personagem morreu
		if(pontos == 0):
			io.stop_music(pg)
			io.escreve(final.getFinal3(),pg, myfont, screen, yellow, nfrases)
			io.play_music(pg, final.getMusicaF3())
			io.delay(pg, myfont, screen, yellow)

			#Todos os booleanos devem indicar o fim do jogo
			FIM_DA_FASE_1 = True
			FIM_DA_FASE_2 = True
			FIM_DA_FASE_3 = True
			FIM_DO_JOGO = True

		#O ultimo paragrafo da fase
		else:
			io.escreve(cena_atual.getTexto(),pg, myfont, screen, yellow, nfrases)
			io.delay(pg, myfont, screen, yellow)
			
			#Ajusta o booleano indicando o final da fase
			if(not(FIM_DA_FASE_1)):
				FIM_DA_FASE_1 = True
				io.stop_music(pg)
				MUSIC_ON = False
			elif(not(FIM_DA_FASE_2)):
				FIM_DA_FASE_2 = True
				io.stop_music(pg)
				MUSIC_ON = False
			elif(not(FIM_DA_FASE_3)):
				FIM_DA_FASE_3 = True
				io.stop_music(pg)
				MUSIC_ON = False
				#Se a fase 3 acabou, o jogo tambem
				FIM_DO_JOGO = True
				decideFinal(cena_atual)

#Chama tela de abertura do View, que deve retornar com a opcao do jogador
opcao = ""
while(not(opcao in range(256))):
	io.play_music(pg, "Musicas/Kraftwerk - The Man Machine - 8 Bit.mp3")
	opcao = TelaDeAbertura.abertura(pg, myfont, screen)
opcao = chr(opcao)
while(opcao != "b"):
	if (opcao == "a"):
		loopPrincipal()
	#Chama tela de abertura do View de novo
	while(not(opcao in range(256))):
		opcao = TelaDeAbertura.abertura(pg, myfont, screen)
	opcao = chr(opcao)