#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from pygame.locals import *

posi_texto = (10, 165)

def esperaTeclaPressionada(pg):
    while True:
    	for event in pg.event.get():
    		if event.type == KEYUP:
    			return event.key

def processa_texto(linha):
	#ESSA FUNCAO PRECISA RECEBER UMA STRING LONGA, CHEIA DE \n E FAZER O SEGUINTE:
	#	1) separar os \n e transformar os pedacos em uma lista de string (e tirar as malditas strings nulas do final)
	texto = linha.split("\n")
	#if (texto[-1] == ""):
	#	texto.pop()

	#metodo para retirar todas as strings nulas
	texto = filter(lambda a: a != "", texto)

	#	2) tratar cada string para que tenha no maximo n = 40 caracteres.
	contador = 0
	tamanho = len(texto)
	i = 0

	for i in texto:
		n = 48
		if(len(i) > n):
			while(i[n] != " "):
				n = n - 1
			elemento = i[0:n]
			sobra = i[n+1:len(i)]
			texto[contador] = elemento
			texto.insert(contador + 1, sobra)
		contador = contador + 1

	return texto

def escreve_linha(linha, pg, myfont, screen, cor, posi_texto):
	char = ""
	label = ""
	velocidade_do_texto = 0.001
	for j in linha:
		sleep(velocidade_do_texto)
		char = char + j
		label = myfont.render(char, 1, cor)
		screen.blit(label, posi_texto)

		pg.display.flip()
	return label

def apagaTela(pg, screen):
	screen.fill((0, 0, 0))
	pg.display.update()
	return

def delay(pg, myfont, screen, cor):
	label = escreve_linha("Pressione qualquer tecla para continuar...", pg, myfont, screen, cor, (10, 440))
	esperaTeclaPressionada(pg)
	apagaTela(pg, screen)

def escreve(linha, pg, myfont, screen, cor, nlinhas):
	apagaTela(pg, screen)
	#encoding
	linha = linha.decode("utf-8").encode("latin1")
	#copia
	p = posi_texto

	texto = processa_texto(linha)
	print texto
	
	conta_linhas = 0
	for i in texto:
		#se for a hora de listar as opcoes, quero obrigar a rotina a gerar uma nova tela
		if ((len(i))and("	a)" in i)):
			delay(pg, myfont, screen, cor)
			conta_linhas = 0
			p = posi_texto
		escreve_linha(i, pg, myfont, screen, cor, p)
		p = (p[0], p[1] + 25)
		conta_linhas = conta_linhas + 1
		if ((conta_linhas == nlinhas)and(i != texto[-1])):
			delay(pg, myfont, screen, cor)
			conta_linhas = 0
			p = posi_texto
	return