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
	#	1) separar os \n e transformar os pedacos em uma lista de string
	texto = linha.split("\n")

	#	2) tratar cada string para que tenha no maximo 40 caracteres.
	contador = 0
	tamanho = len(texto)
	n = 40
	i = 0

	for i in texto:
		if(len(i) > n):
			
			if (i[n] == " "):
				elemento = i[0:n]
				sobra = i[n+1:len(i)]
			else:
				elemento = i[0:n] + "-"
				sobra = i[n:len(i)]
			texto[contador] = elemento
			texto.insert(contador + 1, sobra)
		contador = contador + 1

	return texto

def escreve_linha(linha, pg, myfont, screen, cor, posi_texto):
	char = ""
	for j in linha:
		sleep(0.05)
		print char.encode("utf-8")
		char = char + j
		label = myfont.render(char, 1, cor)
		screen.blit(label, posi_texto)

		pg.display.flip()
	return

def apagaTela(pg, screen):
	screen.fill((0, 0, 0))
	pg.display.update()
	return

def delay(pg, myfont, screen, cor):
	escreve_linha("Pressione qualquer tecla para continuar...", pg, myfont, screen, cor, (10, 400))
	esperaTeclaPressionada(pg)
	apagaTela(pg, screen)

def escreve(linha, pg, myfont, screen, cor, nlinhas):
	#copia
	p = posi_texto

	texto = processa_texto(linha)
	
	conta_linhas = 0
	for i in texto:
		escreve_linha(i, pg, myfont, screen, cor, p)
		p = (p[0], p[1] + 25)
		conta_linhas = conta_linhas + 1
		if (conta_linhas == nlinhas):
			delay(pg, myfont, screen, cor)
			conta_linhas = 0
			p = posi_texto
	return