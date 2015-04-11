"""
Estrutura de dados utilizada no jogo. O storyline 'e estruturado em forma de a'rvore, onde cada cena representa um no'
Para facilitar o loop principal do jogo, estou antevendo que cada cena sabe quem sao suas cenas filhas e sua cena mae

"""

class Cena(object):

	def __init__(self, texto, cena_mae):
		self.musica = None
		self.texto = texto
		self.cena_mae = cena_mae
		self.cena_filha_a = None
		self.cena_filha_b = None

		#identificador da cena (uso facultativo)
		self.nome = ""

	def setMusica(self, musica):
		self.musica = musica

	def getMusica(self):
		return self.musica

	def setCenaFilhaA(self, cena_filha_a):
		self.cena_filha_a = cena_filha_a

	def getCenaFilhaA(self):
		return self.cena_filha_a

	def setCenaFilhaB(self, cena_filha_b):
		self.cena_filha_b = cena_filha_b

	def getCenaFilhaB(self):
		return self.cena_filha_b

	def getCenaMae(self):
		return self.cena_mae

	def getTexto(self):
		return self.texto

	def setTexto(self, texto):
		self.texto = texto
		
	def setNome(self, nome):
		self.nome = nome

	def getNome(self):
		return self.nome
