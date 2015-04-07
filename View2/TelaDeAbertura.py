from io import *

yellow = (255, 255, 0)

def abertura(pg, myfont, screen):

	fundo = pg.image.load("View2/abertura.png")
	screen.blit(fundo, (0,0))
	pg.display.flip()

	resposta = esperaTeclaPressionada(pg)
	return resposta