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
linha = "Ela sorriu e com um pequeno aceno se virou e foi subindo as escadas, rapidamente para acompanhar um pequeno grupo de alunos que falava alto e ria muito. Aparentemente a experiência estava dando certo: você agora estava acessando uma nova linha temporal, uma cadeia de eventos inédita. Tudo o que restava agora era torcer para que você encontrasse as respostas certas, enquanto houvesse tempo.".decode("utf-8").encode("latin1")
io.escreve(linha, pg, myfont, screen, yellow, 5)

# event loop
while True:
    for event in pg.event.get():
        # exit conditions --> windows titlebar x click
        if event.type == pg.QUIT:
        	raise SystemExit