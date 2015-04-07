#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe onde estao instanciadas as cenas e outras informacoes relativas a primeira parte do jogo

"""
from Cena import *

class PrimeiroAno(object):

	def __init__(self):

		self.inicializaCenas()
		self.inicializaTextos()
		self.inicializaFilhos()

	def inicializaCenas(self):
		self.intro = ""
		self.cena1 = Cena("",None)
		self.cena1a = Cena("", self.cena1)
		self.cena1b = Cena("", self.cena1)
		self.cena1aa = Cena("", self.cena1a)
		self.cena1ab = Cena("", self.cena1a)
		self.cena1ba = Cena("", self.cena1b)
		self.cena1bb = Cena("", self.cena1b)
		self.cena1aaa = Cena("", self.cena1aa)
		self.cena1aab = Cena("", self.cena1aa)
		self.cena1aba = Cena("", self.cena1ab)
		self.cena1abb = Cena("", self.cena1ab)
		self.cena1baa = Cena("", self.cena1ba)
		self.cena1bab = Cena("", self.cena1ba)
		self.cena1bba = Cena("", self.cena1bb)
		self.cena1bbb = Cena("", self.cena1bb)
		self.cena1abba = Cena("", self.cena1abb)
		self.cena1abbb = Cena("", self.cena1abb)
		self.cena1baba = Cena("", self.cena1bab)
		self.cena1babb = Cena("", self.cena1bab)	


	def inicializaTextos(self):

		self.intro = "Segunda-feira, 3 de fevereiro de 2025, 3:25 a.m.\n\n	Tudo pronto. Do primeiro chip à ultima linha de código de máquina, todo o equipamento estava finalizado. Em poucos instantes, o mundo científico conheceria um novo paradigma. Após séculos, finalmente os diversos campos do conhecimento humano se reuniriam novamente. Matemática, física, bioquímica, psicologia, engenharia, história, neurologia, medicina, tudo estava ali. Um mosaico composto por um obstinado cientista com um único objetivo: encontrar respostas. Entender as consequências de causas que nunca aconteceram. Conhecer as respostas de perguntas que se perderam no tempo, investigar os limites do tempo e do destino. Sim, o mundo nunca mais seria o mesmo. Isto é, se ele conseguisse voltar...\n	Jamais esqueceria aquela cena alguém que pudesse tê-la presenciado. Por todos os lados, monitores cuspiam informações de maneira frenética em um laboratório sombrio e visceralmente silencioso, com exceção de eventuais ruídos dos eletrônicos que começavam a dar sinais do desgaste de horas a fio de processamento. E, comandando aquela orquestra tecno-gótica, um único homem, emagrecido e enfraquecido pelas pouquíssimas horas de sono, ainda se sustentando graças a sua vontade firme e pelos remédios que havia tomado regularmente desde que deu início à sua preparação.\n	Equipamento ligado, funções vitais estáveis. Só faltava injetar a última substância, posicionar os eletrodos, e com um comando de voz dar início o software.\n\n	- Iniciar procedimento.\n\n	E assim não faltava mais nada...\n"
		self.cena1.setTexto("Segunda-feira, 3 de fevereiro de 2003, 7:15 a.m.\n\n	Levou algum tempo até você perceber que o que incomodava seus olhos fechados era a luz de um sol que acabava de nascer. Havia funcionado. Você estava novamente deitado no sofá-cama que ficava no meio do seu antigo quarto. Tudo exatamente igual a forma como era quando você ainda morava na casa dos seus pais aos 15 anos. Tudo igual, incluindo você. E, com tanta exatidão, certamente você novamente estava atrasado para a aula.\n	Era o primeiro dia de aula do primeiro ano do ensino médio. Difícil se acostumar naquela nova escola, mesmo para você que estava ali pela segunda vez. Durante o intervalo, você ficou sentado num banco em um canto isolado no pátio, vendo os outros alunos conversando alegremente. Você sente a fome apertar. O que você faz?\n\n	a) Continua sentado, porque a preguiça é maior do que a fome\n	b) Vai até a cantina ver o que tem para comer")
		self.cena1a.setTexto("	Enquanto tentava se distrair lendo uma história em quadrinhos que tinha levado na mochila para ler durante o recreio, viu que do outro lado do pátio estava uma menina muito bonita. Mas não era só isso: era ela. Não tinha como ser outra menina, pois não se vê por aí olhos azuis iguais aos dela. Você olhou em volta, mas ela parecia estar sozinha. O que você faz?\n\n	a) Mesmo um pouco inseguro, caminha o mais naturalmente possível para perto dela\n	b) Volta a ler os quadrinhos, petrificado com a idéia de ir falar com a menina.")
		self.cena1b.setTexto("	Você se levanta para ir até a cantina, mas enquanto caminhava percebeu que sentada em um banco um pouco afastado estava sentada uma menina. Não uma menina qualquer, e sim A menina. Mesmo de longe, você tinha certeza que era ela. Mas, a distração que aquela visão causou fez com que você esbarrasse em um rapaz que vinha andando na sua direção e não fez muita questão de desviar. 'Olha por onde anda, cara!' disse ele, parecendo esperar uma resposta. O que você responde?\n\n	a) Ué, você que entrou na minha frente!\n	b) Desculpa, foi sem querer!")
		self.cena1aa.setTexto("	Totalmente sem jeito, você se aproxima, e sem nada melhor para dizer, você simplesmente espera estar perto o suficiente para dizer um 'Oi!' com a voz desafinada pelo nervoso. A menina olha para você um pouco surpresa, e te responde com um 'Oi!' meio sem graça. Pela primeira vez na vida seu cérebro trabalhou rápido e você disse 'Sabe, é que eu sou novo na escola, e ainda não conheço ninguém por aqui!'. 'Ahh, entendi! É, minha mãe disse que esse ano iam entrar alunos novos' disse a menina, parecendo mais a vontade. 'Sua mãe é daqui?' você perguntou. 'Sim, é professora da escola!'. 'Ah, legal! Eu sou Isaque!' você disse. 'Patrícia!' respondeu a menina, 'Mas todo mundo me chama de...'\n	'E aí, Pati!' disse um rapaz alto que de repente tinha aparecido e vinha na direção de vocês. A menina abriu um largo sorriso quando viu o rapaz chegando. 'Oi Eryck! To aqui fazendo amizade com o aluno novo! Isaque, esse é o Eryck!' disse Patrícia. 'E aí, cara!' falou Eryck, e com um gesto rápido vocês apertaram as mãos.\n	'Gente, tá na hora da aula!' disse Patrícia. 'Infelizmente!' disse Eryck com um suspiro. 'Isaque, você vem com a gente?' disse a menina, com aquele sorriso simpático que você já conhecia. O que você responde?\n\n	a) Sim, vamos!\n	b) Daqui a pouco, vou só comprar um salgado aqui e já vou!")
		self.cena1ab.setTexto("	Depois que percebeu que a visão daquela menina o tinha desconcentrado totalmente da leitura, você arriscou uma nova olhada, mas a menina não estava mais lá. E no mesmo instante em que você terminava de pronunciar um sonoro 'Ué?' sem perceber que estava pensando alto, uma voz vindo detrás de você te assustou. 'Oi! Você é aluno novo?' A menina estava bem ali, e falando com você! O que você responde?\n\n	a) 'Sou! E você, é nova por aqui também?'\n	b) 'Quem, eu?'")
		self.cena1ba.setTexto("	'Qual é, tá querendo arrumar problema comigo, rapá?' disse o cara, indo na sua direção. 'O que que houve, Eryck?' perguntou uma voz, que naquele momento tenso soou muito familiar. Subitamente, a mesma menina que você admirava instantes antes estava ali, tentando separar a discussão. 'Esse moleque tá tirando onda comigo!' disse o rapaz que agora você sabia se chamar Eryck. 'Deixa isso pra lá, Eryck, ele é novo aqui!' disse a menina. 'Tu teve sorte dessa vez, hein!' foi o que Eryck disse, antes de sair andando e esbravejando sozinho.\n	'Relaxa, ele é assim com todo mundo!' disse a menina pra você, parecendo mais calma agora. O que você responde?\n\n\n\n	a) 'Ele deve ter me estranhado porque eu sou novo aqui. Você é aluna nova também?'\n	b) 'Você já conhecia ele antes?'")
		self.cena1bb.setTexto("	'Hahaha, qual é, tá com medo de apanhar é? Eu hein, moleque!' disse o cara, saindo e rindo sozinho. Qual não foi a sua surpresa quando, refazendo-se do susto, viu que aquela menina tão bonita estava vindo na sua direção! 'Relaxa, ele é assim com todo mundo, não precisa ficar nervoso.' Disse, enquanto se aproximava. 'Qual é o seu nome?' ela perguntou. O que você responde?\n\n	a) 'Isaque, e o seu?'\n	b) 'Isaque!'")
		self.cena1aaa.setTexto("	Vocês três foram andando em direção a sala e enquanto Eryck e Patrícia falavam de alguma coisa qualquer, cheios de risinhos e implicações. A experiência parecia ter dado muito certo. Eram os mesmos Eryck e Patrícia de antes. Talvez você estivesse mesmo no caminho certo para encontrar as respostas das perguntas que nunca foram feitas. E no caminho, mais gente se juntou a vocês, pessoas que você também se lembrava, pois conviveram juntos nos três anos de ensino médio. Patrícia ia apresentando você a cada um deles, enquanto Eryck pareceu bem indiferente. E assim você foi conhecendo novamente os seus companheiros de classe, e aos poucos a sua ficha foi caindo de que finalmente você havia reencontrado a menina de quem você jamais devia ter se separado.")
		self.cena1aab.setTexto("	Vocês três foram andando em direção a sala e enquanto Eryck e Patrícia falavam de alguma coisa qualquer, cheios de risinhos e implicações. A experiência parecia ter dado muito certo. Eram os mesmos Eryck e Patrícia de antes. Talvez você estivesse mesmo no caminho certo para encontrar as respostas das perguntas que nunca foram feitas. E no caminho, mais gente se juntou a vocês, pessoas que você também se lembrava, pois conviveram juntos nos três anos de ensino médio. Patrícia ia apresentando você a cada um deles, enquanto Eryck pareceu bem indiferente. E assim você foi conhecendo novamente os seus companheiros de classe, e aos poucos a sua ficha foi caindo de que finalmente você havia reencontrado a menina de quem você jamais devia ter se separado.")
		self.cena1aba.setTexto("	'Não, hahaha! To nesse colégio desde o maternal! Mas daqui a três anos acaba, finalmente! Melhor a gente ir pra sala agora! Eu sou Patrícia, e você?' 'Isaque...' você respondeu, meio chateado por ela não se lembrar de você, mesmo sabendo que isso era impossível, já que essa foi precisamente a época em que vocês se conheceram. 'Prazer, Isaque! Vem, eu te apresento a galera que anda comigo!' disse ela, te apresentando a todos os amigos que você já tinha conhecido antes, só que não dessa forma. E enquanto subiam, foi caindo a sua ficha de que depois de todos esses anos, ali estava Patrícia, novamente.")
		self.cena1abb.setTexto("	'Sim, você!'. A menina deu um sorriso. 'Minha mãe é professora daqui, ela me disse que ia entrar muita gente nova esse ano. Qual é o seu nome?'\n\n	a) 'Isaque, e o seu'?\n	b) 'Isaque!'")
		self.cena1baa.setTexto("	'Não, hahaha! To nesse colégio desde o maternal! Mas daqui a três anos acaba, finalmente! Melhor a gente ir pra sala agora! Eu sou Patrícia, e você?' 'Isaque...' você respondeu, meio chateado por ela não se lembrar de você, mesmo sabendo que isso era impossível, já que essa foi precisamente a época em que vocês se conheceram. 'Prazer, Isaque! Vem, eu te apresento a galera que anda comigo!' disse ela, te apresentando a todos os amigos que você já tinha conhecido antes, só que não dessa forma. E enquanto subiam, foi caindo a sua ficha de que depois de todos esses anos, ali estava Patrícia, novamente.")
		self.cena1bab.setTexto("	'Já! Na verdade ele é um cara muito legal quando está entre amigos.' disse ela, fazendo uma leve pausa. 'Bom, eu vou subir que já tá na hora!' Ela disse. O que você responde?\n\n	a) Ah, eu vou também!\n	b) Tá... a gente se vê!")
		self.cena1bba.setTexto("	'Patrícia, mas todo mundo me chama de Pati!'. Um grupinho de meninas começou a chamá-la do outro lado do pátio, no mesmo lugar onde você a tinha visto antes. 'Já vou!' disse Patrícia para as meninas. 'Depois a gente se fala, Isaque!'. E dizendo isso, ia andando em direção às amigas, naquele ritmo rápido tão próprio das meninas na adolescência. Finalmente, depois de todos esses anos, lá estava ela novamente. Patrícia, a menina que com um sorriso foi capaz de conquistar um coração.")
		self.cena1bbb.setTexto("	'Patrícia! Prazer! É bom ter gente nova na sala de vez em quando!' disse ela, mas você já a conhecia suficientemente para saber que ela estava sendo simpática, do jeito que só ela conseguia ser. Embora você não se lembre de nenhuma outra vez que a viu sendo assim com outras pessoas. 'Melhor a gente subir, já tá na hora!' ela disse, e com isso se afastou e foi andando em direção às suas amigas que vinham do mesmo lugar onde você a viu antes, e juntas iam subindo as escadas. Finalmente, depois de todos esses anos, lá estava ela novamente. Patrícia, a menina que com um sorriso foi capaz de conquistar um coração.")
		self.cena1abba.setTexto("	'Patrícia, mas todo mundo me chama de Pati!'. Um grupinho de meninas começou a chamá-la do outro lado do pátio, no mesmo lugar onde você a tinha visto antes. 'Já vou!' disse Patrícia para as meninas. 'Depois a gente se fala, Isaque!'. E dizendo isso, ia andando em direção às amigas, naquele ritmo rápido tão próprio das meninas na adolescência. Finalmente, depois de todos esses anos, lá estava ela novamente. Patrícia, a menina que com um sorriso foi capaz de conquistar um coração.")
		self.cena1abbb.setTexto("	'Patrícia! Prazer! É bom ter gente nova na sala de vez em quando!' disse ela, mas você já a conhecia suficientemente para saber que ela estava sendo simpática, do jeito que só ela conseguia ser. Embora você não se lembre de nenhuma outra vez que a viu sendo assim com outras pessoas. 'Melhor a gente subir, já tá na hora!' ela disse, e com isso se afastou e foi andando em direção às suas amigas que vinham do mesmo lugar onde você a viu antes, e juntas iam subindo as escadas. Finalmente, depois de todos esses anos, lá estava ela novamente. Patrícia, a menina que com um sorriso foi capaz de conquistar um coração.")
		self.cena1baba.setTexto("	Vocês foram subindo as escadas da escola, e assim como da primeira vez (mas não exatamente do mesmo jeito) você sentiu como se já conhecesse aquela menina há muito tempo. Bom, ao menos dessa vez essa impressão era fundamentada. Quando lembraram de se apresentar um ao outro, ela disse se chamar Patrícia. E como era bom ouvir esse nome novamente.")
		self.cena1babb.setTexto("	Ela sorriu e com um pequeno aceno se virou e foi subindo as escadas, rapidamente para acompanhar um pequeno grupo de alunos que falava alto e ria muito. Aparentemente a experiência estava dando certo: você agora estava acessando uma nova linha temporal, uma cadeia de eventos inédita. Tudo o que restava agora era torcer para que você encontrasse as respostas certas, enquanto houvesse tempo.")
		
	def inicializaFilhos(self):

		self.cena1.setCenaFilhaA(self.cena1a)
		self.cena1.setCenaFilhaB(self.cena1b)

		self.cena1a.setCenaFilhaA(self.cena1aa)
		self.cena1a.setCenaFilhaB(self.cena1ab)

		self.cena1b.setCenaFilhaA(self.cena1ba)
		self.cena1b.setCenaFilhaB(self.cena1bb)

		self.cena1aa.setCenaFilhaA(self.cena1aaa)
		self.cena1aa.setCenaFilhaB(self.cena1aab)

		self.cena1ab.setCenaFilhaA(self.cena1aba)
		self.cena1ab.setCenaFilhaB(self.cena1abb)

		self.cena1ba.setCenaFilhaA(self.cena1baa)
		self.cena1ba.setCenaFilhaB(self.cena1bab)

		self.cena1bb.setCenaFilhaA(self.cena1bba)
		self.cena1bb.setCenaFilhaB(self.cena1bbb)

		self.cena1abb.setCenaFilhaA(self.cena1abba)
		self.cena1abb.setCenaFilhaB(self.cena1abbb)

		self.cena1bab.setCenaFilhaA(self.cena1baba)
		self.cena1bab.setCenaFilhaB(self.cena1babb)

	def getIntro(self):
		return self.intro

	def getCena1(self):
		return self.cena1

	def getCena1a(self):
		return self.cena1a

	def getCena1b(self):
		return self.cena1b

	def getCena1aa(self):
		return self.cena1aa

	def getCena1ab(self):
		return self.cena1ab

	def getCena1ba(self):
		return self.cena1ba

	def getCena1bb(self):
		return self.cena1bb

	def getCena1aaa(self):
		return self.cena1aaa

	def getCena1aab(self):
		return self.cena1aab

	def getCena1aba(self):
		return self.cena1aba

	def getCena1abb(self):
		return self.cena1abb

	def getCena1baa(self):
		return self.cena1baa

	def getCena1bab(self):
		return self.cena1bab

	def getCena1bba(self):
		return self.cena1bba

	def getCena1bbb(self):
		return self.cena1bbb

	def getCena1abba(self):
		return self.cena1abba

	def getCena1abbb(self):
		return self.cena1abbb

	def getCena1baba(self):
		return self.cena1baba

	def getCena1babb(self):
		return self.cena1babb
