#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe onde estao instanciadas as cenas e outras informacoes relativas a segunda parte do jogo

"""
from Cena import *

class SegundoAno(object):

	def __init__(self):

		self.inicializaCenas()
		self.inicializaTextos()
		self.inicializaFilhos()

	def inicializaCenas(self):
		self.intro = ""
		self.cena1 = Cena("",None)
		self.cena1.setMusica("Musicas/The Cure - Friday I'm In Love [8-BIT].mp3")
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
		self.cena1abaa = Cena("", self.cena1aba)
		self.cena1abab = Cena("", self.cena1aba)	


	def inicializaTextos(self):

		self.intro = "[	Sexta-feira, 13 de agosto de 2004, 5:45 p.m.]\n\n	Você não sabia dizer se era devido a uma falha no software que assumira o controle do seu ritmo neural, ou se era apenas a impressão normal da vida, mas o fato era que o tempo parecia estar passando rápido demais. Em pouco mais de um ano você havia reencontrado Patrícia e todos os outros amigos que tornaram mais alegre a sua vivência naquela escola, que agora voltava a parecer simpática, do jeito como você se lembrava. E além disso, graças a um maravilhoso incentivo dos seus pais, você estava cada vez mais perto de conquistar aquela que talvez seria (ou havia sido?) a oportunidade da sua vida: uma bolsa para cursar uma graduação em outro país. Mas dessa vez seria diferente. Você já sabia como um caminho terminava; restava saber do outros.\n	Mas isso parecia importar menos agora. Pela segunda vez na sua vida, você havia tomado coragem suficiente para convidar Patrícia para sair. Mas, já que vocês dois tinham se tornado grandes amigos, parece que ela entendeu como um simples programa de amigos. Você não sabia se isso era bom ou ruim, mas de qualquer forma estava acontecendo."
		self.cena1.setTexto("	No cinema, vocês chegaram um pouco atrasados em relação ao que tinham planejado, e ainda não haviam decidido qual filme iriam ver, e ambos estavam prestes a começar! 'Ok, você convidou, você tem o direito de escolher o filme! Vai, rápido!' disse Patrícia, com seu habitual ar de implicância. Qual filme você escolhe para assistir?\n\n	a) Homem Aranha 2\n	b) Shrek 2")
		self.cena1a.setTexto("	Entrando na sala do cinema, havia poucos lugares vazios, mas graças aos longos trailers de filmes vocês conseguiram chegar a tempo. 'Isaque, já que o filme ainda não começou, eu quero te contar uma coisa!' disse Patrícia. Deus sabe como seu coração disparou naquele momento. Você olhou para ela, e ela estava sorrindo! Devia ser uma coisa boa! O que podia ser? 'Pode falar...' você disse, se esforçando para pronunciar cada palavra. Mas nesse mesmo instante, enfim, o filme ia começar. 'Ah, agora o filme começou! Depois eu conto!' disse a menina, voltando a olhar para frente. O que você faz?\n\n	a) Aparenta normalidade e desinteresse, espera alguns momentos, até que insiste em saber o que ela queria dizer\n	b) Só assiste o filme")
		self.cena1b.setTexto("	Entrando na sala do cinema, havia poucos lugares vazios, mas graças aos longos trailers de filmes vocês conseguiram chegar a tempo. 'Patrícia, já que o filme ainda não começou, eu queria te dizer uma coisa.' você disse. Deus sabe como seu coração disparou naquele momento. Você devia estar louco! Ia mesmo revelar a ela os seus sentimentos assim? Você olhou para ela, e ela estava sorrindo! Devia ser uma coisa boa! O que podia ser? 'Pode falar...' ela disse. Mas nesse mesmo instante, enfim, o filme ia começar. Talvez fosse um sinal de que aquele não era o melhor momento. 'Ah, agora o filme começou! Depois eu conto!' você disse, voltando a olhar para frente. O que você faz?\n\n	a) Aparenta normalidade e desinteresse, espera alguns momentos, até fazer uma nova tentativa\n	b) Só assiste o filme")
		self.cena1aa.setTexto("	SHHHHHH! foi o que as pessoas disseram, já que você não conseguia manter um tom de voz muito baixo. Foi aí que você começou a calcular o quão patético você deveria estar parecendo. 'Ai, que curioso! Tá, eu conto, mas depois eu explico! Eu e o Eryck estamos namorando!'. Quando a frase terminou, você sentiu que seu coração estava quinze toneladas mais pesado. NAMORANDO! Patrícia e Eryck, o valentão da escola, estavam namorando! E você ainda pensando que ela ia dizer que... nossa, você estava se sentindo péssimo. O que você faz?\n\n	a) Pede licença, e vai ao banheiro tentar refrescar um pouco a cabeça\n	b) Diz um 'Ok' e continua assistindo o filme")
		self.cena1ab.setTexto("	Obviamente você não conseguiu mais prestar atenção em filme nenhum. Na verdade, você mal sabia como estava conseguindo aguentar o baque. Tudo o que você pensava era que as respostas começavam a aparecer, e certas coisas agora pareciam fazer sentido. De qualquer forma, se havia algum momento para tentar coisas inusitadas, esse parecia ser o melhor! Bem, talvez nem tanto. Mesmo sendo uma simulação, os problemas envolvendo paradoxos temporais ainda não estavam resolvidos no nível mental. Melhor seria ser cauteloso e evitar ações que saíssem muito do curso original, pois as consequências de toda essa carga de informações para a sua mente ainda eram totalmente desconhecidas.")
		self.cena1ba.setTexto("	Você não sabe exatamente quanto tempo esperou. Só sabe que já havia passado provavelmente metade do filme, quando você voltou ao assunto sutilmente, e foi quando você reparou que Patrícia estava meio sem jeito. Esse é o grande momento! O que você diz?\n\n	a) Então... você... hã... eu queria saber se... de repente... você...\n	b) Na verdade, eu só queria dizer o quanto você está bonita hoje!")
		self.cena1bb.setTexto("	Mesmo com o coração acelerado, e sem saber exatamente se você estava ou não em um encontro, até que o filme foi legal, e tudo transcorreu da forma mais normal possível. O filme terminou por volta das 8:00 p.m., e segundo o seu plano original, essa era a hora que você convidava a moça para ir comer alguma coisa. Ou vocês simplesmente podiam se despedir. O que você diz?\n\n	a) 'Bom, eu tô morrendo de fome, quer ir comer alguma coisa?'\n	b) 'É, o filme foi legal, mas agora talvez esteja ficando um pouco tarde... '")
		self.cena1aaa.setTexto("	Você abre a torneira e joga água no rosto, antes até de tirar os óculos, de tão desorientado que ficou. Aquilo definitivamente não estava nos planos. Você agora já não tinha mais cabeça pra filme nenhum. E o interessante é que você não sabia que eles começaram a namorar desde essa época. Que belo papel você deve ter feito! Mas, de qualquer forma, você tinha que voltar, e parecer o menos abalado possível. Seria ainda pior se ela descobrisse agora que você esteve apaixonado por ela durante todo esse tempo. Mas ruim mesmo ia ser conviver todos os dias próximo a Patrícia e Eryck.")
		self.cena1aab.setTexto("	Obviamente você não conseguiu mais prestar atenção em filme nenhum. Na verdade, você mal sabia como estava conseguindo aguentar o baque. Tudo o que você pensava era que as respostas começavam a aparecer, e certas coisas agora pareciam fazer sentido. De qualquer forma, se havia algum momento para tentar coisas inusitadas, esse parecia ser o melhor! Bem, talvez nem tanto. Mesmo sendo uma simulação, os problemas envolvendo paradoxos temporais ainda não estavam resolvidos no nível mental. Melhor seria ser cauteloso e evitar ações que saíssem muito do curso original, pois as consequências de toda essa carga de informações para a sua mente ainda eram totalmente desconhecidas.")
		self.cena1aba.setTexto("	'Ah, não sei se vai dar tempo, tinha marcado de encontrar umas amigas depois do cinema!'. Esse com certeza foi o momento mais constrangedor pelo qual você já passou. Ela não foi no shopping só por sua causa, ela foi no cinema aproveitando que ia encontrar com as amigas! Na verdade foi o segundo, exatamente igual à forma como tudo aconteceu da primeira vez. Estranho, pois você devia se lembrar disso. Talvez você estivesse passando tempo demais na máquina, e sua consciência estivesse diminuindo. E por isso você não se lembrava qual a resposta que deu da primeira vez.\n\n	a) 'Ah, então tá... acho que eu vou indo então... valeu!'\n	b) 'Mas e aquela coisa que você disse que ia me contar?'")
		self.cena1abb.setTexto("	'Bom, eu marquei de encontrar minha mãe e minha irmã na saída do cinema. Elas vieram resolver umas coisas, aí eu aproveito e volto com elas.' Ou o software tinha entrado em um modo de operação alternativo e tinha apagado tudo do seu cérebro, ou você REALMENTE não sabia o que dizer. Essa talvez fosse a primeira sugestão da lista 'piores formas de descobrir que seu pseudo-encontro não passou nem perto de um encontro.' Você deve ter ficado tempo suficiente sem dizer nada, ao que Patrícia perguntou '...você quer carona a gente?' 'Não, tudo bem, eu me viro sozinho!'. Breves despedidas, e vocês seguiram seus caminhos. Mas, antes que vocês se afastassem muito, você arriscou uma última olhada, e não entendeu o que viu: um rapaz alto, com cabelos levemente despenteados, aparentemente encontrando com Patrícia. Eles se abraçaram e... deram um beijo. Você sentiu a mente confusa. Em parte porque até onde você sabia Patrícia não tinha nenhum namorado. Em parte porque o software estabilizador de emoções acabava de ser ativado naquele momento, para que aquela descarga de adrenalina no seu sangue não levasse à uma pane no software regulava o seu nível consciencial.")
		self.cena1baa.setTexto("	'Isaque, você pode ir comprar mais pipocas? As minhas acabaram!' disse Patrícia, cortando a sua fala. Totalmente sem jeito, você apenas foi. Durante todo o restante do filme, você não arriscou falar mais nada, torcendo para que passasse de uma vez o leve clima estranho que ficou. Cara, onde você tava com a cabeça? Era melhor ter ficado na sua, certo? Porque agora você já não sabia se ela sabia que você gostava dela, ou se ela não tinha entendido nada, ou se estava fingindo que não tinha entendido, enfim, você não sabia mais de NADA! Quando o filme terminou, você estava confuso. Um pouco mais confuso do que você esperava estar, na verdade você estava até um pouco tonto. Veio então uma preocupação que fez você travar a respiração: havia algo de errado com o software que regulava as lembranças. Aquilo tudo era um conjunto de dados totalmente inédito, e talvez o programa estivesse respondendo mal a um número tão grande de informações novas simultâneamete. Ao menos, depois do filme, o clima estranho passou e você e Patrícia voltaram a conversar novamente. Mas por via das dúvidas, você achou melhor alegar que estava se sentindo mal, e acabou voltando para casa sozinho e de ônibus, exatamente como da primeira vez. Coinciência ou não, o mal estar passou no momento em que você subiu no mesmo ônibus, revivendo em parte a história como aconteceu da primeira vez.")
		self.cena1bab.setTexto("	No decorrer da experiência, algumas informações novas eram coletadas e juntadas ao seu conjunto de lembranças, e nesse momento uma nova lembrança era registrada: você nunca tinha visto Patrícia sorrindo do jeito que ela sorriu naquele momento. 'Ai, pra quê tanto mistério só por isso! Mas brigada, viu?' ela disse, e vocês voltaram a assistir o filme. Ok, não foi uma declaração como você havia achado que seria, mas a julgar por aquele sorriso, essa foi provavelmente a coisa mais acertada que você já disse.")
		self.cena1bba.setTexto("	'Poxa, eu até que aceitaria, mas tô com medo de ficar um pouco tarde. E também eu marquei de encontrar com a minha mãe e com a minha irmã na saída do cinema, para aproveitar a carona delas. Fica pra próxima, tá?' ela disse, com aquele sorriso que você já conhecia, que indicava que ela estava sendo mais simpática do que sincera. 'Tá, tudo bem! Bom, eu vou indo então!'. Vocês se despediram e você se foi. Bom, não era um encontro afinal. Antes de entrar no ônibus, você arriscou uma última olhada, e viu ela, a mãe e a irmã conversando bastante animadas. O medo de que elas estivessem comentando qualquer coisa sobre você afetou mais o seu estômago do que a fome que você estava sentindo.")
		self.cena1bbb.setTexto("	'É, eu também acho...' disse Patrícia. E, um pouco sem jeito, vocês se despediram. Mas antes de ir, você ouviu Patrícia te chamando. 'Você não vai dizer o que ia me contar naquela hora?' ela disse, desviando levemente os olhos dos seus. 'Não.' você respondeu. 'Nada que eu dissesse poderia fazer explicar... o quanto eu gosto de você!'. Pela primeira vez na vida, você agora estava nervoso depois de ter falado. Muito nervoso, por sinal! Patrícia, que estava com os olhos baixos, olhou para você num misto de surpresa e timidez. 'Você gosta de mim, Isaque?' ela perguntou. Nesse momento, o nervosismo atingiu níveis muito altos, e você perdeu um pouco o fôlego. Na verdade, tudo ao redor começou a perder um pouco do brilho, ou das formas, ou qualquer outra coisa estava acontecendo, mas você começou a se sentir bastante confuso, e precisou se sentar num banco próximo de onde você estava. 'Isaque, você está se sentindo bem? Isaque, acorda! Você gosta de mim, Isaque?' foram as perguntas que você ouvia se repetindo indefinidamente, enquanto tudo escurecia de vez. Mas logo depois, você estava novamente em pé, no mesmo local de antes. 'Você não vai dizer o que ia me contar naquela hora?' disse Patrícia. Você apenas fingiu não ter ouvido. Embora você não guardasse consciência disso, mas naquele momento o software estabilizador de emoções acabava de ser iniciado. Era melhor não testar o quão bem você o havia programado.")
		self.cena1abaa.setTexto("	Vocês se despediram, e cada um foi para um lado. Fazendo um balanço da situação, você começa a se perguntar por que você teve essa idéia. Acabou não dando em nada. De novo. Na verdade deu: você voltou bem mais cedo para casa. Seria bom se você fosse um pouco menos tímido de vez em quando, só para variar. Bom, talvez não fosse de todo ruim, afinal, ainda dava para aproveitar o restante da noite para estudar para a prova de segunda-feira. Cada nota alta era um passo na direção daquela bolsa de intercâmbio, que agora estava mais próxima do que nunca.")
		self.cena1abab.setTexto("	'Ah é, quase esqueci!' ela disse, e você notou que ela ficou instantaneamente com o rosto avermelhado. 'Mas você tem que guardar segredo... eu e o Eryck estamos namorando!' A sua cara de decepção deve ter sido ótima. 'Vocês dois?' você disse, aumentando um pouco mais a voz do que você gostaria. 'Bom, na verdade a gente não tá namorando, a gente tá só saindo de vez em quando... sei lá! E na verdade, eu falei que ia encontrar com umas amigas, mas vou encontrar com ele!' 'E por que você não falou a verdade?' Patrícia começou a desviar os olhos dos seus. 'Ah, sei lá... acho que fiquei com vergonha! Você... ficou chateado?' ela disse, provavelmente percebendo o seu baixo astral. 'Não, tá tudo bem. A gente se vê então... tchau!' você disse, e lá foi você andando em direção à saída do shopping. E foi até bom, porque Eryck tinha chegado naquele momento. Ver eles dois juntos talvez fosse emoção demais para você, e de qualquer forma, você não sabia direito quais seriam os efeitos de uma carga muito alta de emoções no decorrer da experiência.")
		
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

		self.cena1aba.setCenaFilhaA(self.cena1abaa)
		self.cena1aba.setCenaFilhaB(self.cena1abab)
		

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

	def getCena1abaa(self):
		return self.cena1abaa

	def getCena1abab(self):
		return self.cena1abab
