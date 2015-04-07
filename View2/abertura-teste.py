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
linha = "	Certamente era indescritível a sensação que se apoderou de você naquele momento. Uma grande bagunça de imagens descoordenadas de diversos momentos da sua vida e sons, muitos sons. Era impossível dizer quanto tempo aquilo durou, mas enquanto durou pareceu uma verdadeira eternidade. Quando finalmente as coisas começaram a tomar forma e sentido, um grande silêncio pesou em seus ouvidos. Ao mesmo tempo, um pequeno ruído ia se fazendo ouvir cada vez mais, um som que era algo familiar, um som... de soluços. Alguém estava chorando um pranto um tanto ou quanto amargo. Mas o pranto encontrou seu fim no momento em que você abriu os olhos. Você estava deitado em uma cama, em algum lugar que devia ser um hospital, como você acabava de se lembrar. A experiência havia sido bem-sucedida: você havia sobrevivido ao passado, e estava novamente no presente. E ao seu lado, segurando a sua mão, uma mulher de meia idade olhava para você fixamente, com o rosto ainda húmido pelas lágrimas. Você ainda se sentia um pouco desnorteado, mas jamais confundiria o que estava vendo. Não tinha como ser outra pessoa, pois não se vê por aí olhos azuis iguais aos dela. 'Isaque?' ela perguntou sussurando cuidadosamente, como se temesse que o som o pudesse afetar. 'É bom te ver de novo, Patrícia!' você disse. E assim vocês permaneceram por algum tempo, apenas olhando um para o outro. Ela, a menina por quem você era secretamente apaixonado. E você, a pessoa que ela percebeu que não poderia viver sem.\n	Em um canto da sala, uma pilha de jornais. Durante quinze anos, você foi a estrela do mundo científico. 'CIENTISTA ENTRA EM COMA APÓS EXPERIÊNCIA DE REGRESSÃO', 'BUSCA PELO PASSADO JÁ COMPLETA DUAS DÉCADAS' eram algumas das manchetes. Mas a manchete do dia seguinte não seria outra: 'APÓS VINTE ANOS, CIENTISTA ACORDA DE COMA APÓS EXPERIÊNCIA - edição número 1,  Domingo, 3 de fevereiro de 2030.'\n"
io.escreve(linha, pg, myfont, screen, yellow, 5)

# event loop
while True:
    for event in pg.event.get():
        # exit conditions --> windows titlebar x click
        if event.type == pg.QUIT:
        	raise SystemExit