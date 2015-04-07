#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.locals import *
import pygame as pg
import io

pg.init()

yellow = (255, 255, 0)

screen = pg.display.set_mode((640, 480))
pg.display.set_caption("Text adventures with Pygame")
myfont = pg.font.SysFont("Computer Pixel-7", 40)

########### IMPORTANTE: O DISPLAY COMPORTA 40 CARACTERES POR LINHA!!!!!!!!!!!!!!!!!!!!!!!
linha = "	Totalmente sem jeito, você se aproxima, e sem nada melhor para dizer, você simplesmente espera estar perto o suficiente para dizer um 'Oi!' com a voz desafinada pelo nervoso. A menina olha para você um pouco surpresa, e te responde com um 'Oi!' meio sem graça. Pela primeira vez na vida seu cérebro trabalhou rápido e você disse 'Sabe, é que eu sou novo na escola, e ainda não conheço ninguém por aqui!'. 'Ahh, entendi! É, minha mãe disse que esse ano iam entrar alunos novos' disse a menina, parecendo mais a vontade. 'Sua mãe é daqui?' você perguntou. 'Sim, é professora da escola!'. 'Ah, legal! Eu sou Isaque!' você disse. 'Patrícia!' respondeu a menina, 'Mas todo mundo me chama de...'\n	'E aí, Pati!' disse um rapaz alto que de repente tinha aparecido e vinha na direção de vocês. A menina abriu um largo sorriso quando viu o rapaz chegando. 'Oi Eryck! To aqui fazendo amizade com o aluno novo! Isaque, esse é o Eryck!' disse Patrícia. 'E aí, cara!' falou Eryck, e com um gesto rápido vocês apertaram as mãos.\n	'Gente, tá na hora da aula!' disse Patrícia. 'Infelizmente!' disse Eryck com um suspiro. 'Isaque, você vem com a gente?' disse a menina, com aquele sorriso simpático que você já conhecia. O que você responde?\n\n	a) Sim, vamos!\n	b) Daqui a pouco, vou só comprar um salgado aqui e já vou!"
io.escreve(linha, pg, myfont, screen, yellow, 5)

# event loop
while True:
    for event in pg.event.get():
        # exit conditions --> windows titlebar x click
        if event.type == pg.QUIT:
        	raise SystemExit