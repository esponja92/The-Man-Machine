#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe onde estao instanciadas as cenas e outras informacoes relativas a terceira parte do jogo

"""
from Cena import *

class Formatura(object):

	def __init__(self):

		self.inicializaCenas()
		self.inicializaTextos()
		self.inicializaFilhos()

	def inicializaCenas(self):
		self.intro = ""
		self.cena1 = Cena("",None)
		self.cena1.setMusica("Musicas/New Order - Bizarre Love Triangle.mp3")
		self.cena1a = Cena("", self.cena1)
		self.cena1b = Cena("", self.cena1)
		self.cena1aa = Cena("", self.cena1a)
		self.cena1ba = Cena("", self.cena1b)
		self.cena1bb = Cena("", self.cena1b)
		self.cena1aaa = Cena("", self.cena1aa)
		self.cena1aab = Cena("", self.cena1aa)
		self.cena1aab.setNome("1aab")
		self.cena1baa = Cena("", self.cena1ba)
		self.cena1baa.setNome("1baa")
		self.cena1bab = Cena("", self.cena1ba)
		self.cena1bab.setNome("1bab")
		self.cena1bba = Cena("", self.cena1bb)
		self.cena1bba.setNome("1bba")
		self.cena1bbb = Cena("", self.cena1bb)
		self.cena1bbb.setNome("1bbb")
		self.cena1aaaa = Cena("", self.cena1aaa)
		self.cena1aaaa.setNome("1aaaa")			 
		self.cena1aaab = Cena("", self.cena1aaa)
		self.cena1aaab.setNome("1aaab")

	def inicializaTextos(self):

		self.intro = "[	Sábado, 26 de novembro de 2005]\n\n	Você sempre ouviu falar que os três anos de ensino médio passam rápido. Talvez o final da adolescência seja mesmo a melhor época da vida. Mas no seu caso havia outro fator: você sabia que o tempo estava acabando. A ansiedade por este momento era cada vez maior, pois mesmo tendo se dedicado especialmente no módulo que o traria de volta para a realidade, nada o garantia de que tudo estava funcionando correatmente. Além disso, conforme o tempo passava, mais esforço você fazia para manter consciência do que estava em curso. Não era raro você confundir as datas, por exemplo. E isso definitivamente não devia estar acontecendo.\n"
		self.cena1.setTexto("	Havia chegado, porém, o dia da festa de formatura. Assim como da primeira vez, seus amigos o haviam convencido de ir a festa, e você acabou aceitando mesmo a contragosto. Não era muito do seu costume ir a festas, mas de alguma forma, a idéia de que Patrícia também iria o havia motivado. As coisas entre vocês dois haviam ficado um pouco estranhas desde o segundo ano, e até onde você sabia, Patrícia e Eryck estavam saindo juntos, mas por algum motivo qualquer não continuaram sua relação para um namoro.\n	A festa acabou sendo melhor do que você imaginava. A hora já estava avançada, quando você percebeu que Patrícia havia se afastado para pegar uma bebida. Finalmente ela estava sozinha! Essa seria uma boa chance de você finalmente encontrar as respostas que faltavam... ou não. O que você faz?\n\n	a) Caminha em direção a Patrícia, fingindo que também queria uma bebida\n	b) Continua observando")
		self.cena1a.setTexto("	Você cuida para que Patrícia não o veja enquanto se aproxima, exatamente como você sempre fez. 'Não sabia que você curtia esse tipo de bebida!' você disse, assustando a moça, ao que ela respondeu com um sorriso. 'Não gosto, mas é só isso o que tem pra beber' disse ela, tomando um gole do copo. 'E você? Soube que conseguiu aquela bolsa de estudos no exterior, seu nerd!' ela teve que gritar, porque a música da pista de dança havia ficado subitamente alta demais. 'É, acho que eu consegui!' você disse. 'E você vai mesmo... embora?' perguntou ela, parecendo levemente arrependida com a pergunta. O que você responde?\n\n	a) Sim, acho que isso pode me trazer boas oportunidades na minha carreira\n	b) Na verdade eu não sei, ainda preciso pensar sobre isso\n	c) Voltar a cena anterior")
		self.cena1b.setTexto("	A sensação de estar deixando a mesma oportunidade passar pela segunda vez não foi das melhores. Pela segunda vez ali estava você, vendo o tempo passar enquanto Patrícia curtia a festa. E como era esperado, naquele momento um rapaz alto, com um sorriso malandro, vinha se aproximando dela. Era Eryck, o mesmo Eryck de sempre. E que agora estava ali, falando com o rosto bem próximo ao ouvido de Patrícia, e devia ser alguma coisa engraçada, por que ela estava rindo bastante. 'De novo, não!' você pensa. O que você pretende fazer?\n\n	a) Nada, afinal, eles deviam estar se entendendo muito bem\n	b) Vai até lá e tenta entrar na conversa\n	c) Voltar a cena anterior")
		self.cena1aa.setTexto("	Você tentou dizer isso, mas obviamente nenhuma das suas palavras soou de forma convincente. Mais do que qualquer insegurança, a idéia de nunca mais voltar a ver Patrícia era o elemento principal dessa equação. 'Nossa, eu admiro você! No meu caso, eu ficaria super insegura. Nada te incomoda? Se afastar da sua família, dos seus amigos... nada?'. Essa é provavelmente a última noite que você estará com todos os seus amigos! Pense bem! O que você responde?\n	a) Na verdade, eu sentiria falta sim...\n	b) Bom, isso tudo é um pouco chato, mas são coisas que não tem jeito\n	c) Voltar a cena anterior")
		self.cena1ba.setTexto("	Parecia que sim, apesar dos seus esforços, tudo estava acontecendo novamente. Mesmo que você tivesse circulado um pouco pela festa, não conseguia desgrudar os olhos de Eryck e Patrícia, que agora conversavam em uma mesa um pouco mais reservada. Agora você podia vê-los bem. Quando uma balada mais lenta, típica do momento 'final-de-festa', você viu os dois indo para a pista de dança. Não era preciso ser um gênio para saber o que ia acontecer, mas você desviou os olhos, a lembrança de ter visto Eryck e Patrícia juntos naquela festa era uma das poucas que você jamais esqueceria. Nesse momento, porém, a mãe de Patrícia, professora que havia sido escolhida para ser paraninfo da turma, e que provavelmente havia percebido o que acontecia, veio até você puxando um assunto qualquer. Vocês conversaram por alguns minutos até que ela trouxe o assunto principal: sua bolsa de estudos. 'E aí Isaque, você já decidiu? Vai mesmo aceitar a bolsa de estudos?'. O que você responde?\n\n	a) Não, há coisas demais me prendendo aqui\n	b) Sim, é uma oportunidade única\n	c) Voltar a cena anterior")
		self.cena1bb.setTexto("	Vendo você se aproximar, Patrícia sorriu e o chamou. Essa reação da menina causou não só estranheza a você, mas também a Eryck, só que ele pareceu não ficar muito contente. 'Vem pra cá, Isaque! Sai daquele canto sozinho e fica aqui com a gente!' ela disse, dando um suave puxão no seu braço. 'Não sei, não quero atrapalhar nada!' você disse, em tom de brincadeira. Mas Eryck não parecia estar se divertindo. 'Pois é cara, melhor você pegar uma bebida, tem uma professora ali pra você bater um papo cabeça!' disse Eryck. 'Eryck!' repreendeu Patrícia. O que você responde?\n\n	a) Tá tranquilo Eryck, tô indo nessa\n	b) Qual é, cara? Foi a Patrícia quem me chamou!\n	c) Voltar a cena anterior")
		self.cena1aaa.setTexto("	Nesse momento Patrícia, que até então mantinha os olhos distantes, fixou os olhos azuis em você. Você também percebeu que o DJ estava tocando uma versão remixada de 'Bizarre Love Triangle', a mesma música que você tinha ouvido várias vezes durante toda aquela semana. Além disso, ou a luz do ambiente havia abaixado, ou você estava começando a ter dificuldade de enxergar as coisas. 'De que?' ela perguntou. O que você responde?\n\n	a) Da sua amizade\n	b) De você\n	c) Voltar a cena anterior")
		self.cena1aab.setTexto("	'Bom, que bom que você está bem então. De qualquer forma, eu vou sentir muito a sua falta, tá, seu bobão?' disse a moça, te dando um rápido abraço. Umas meninas histéricas estavam chamando Patrícia para dançar a balada que havia começado a tocar, ao que ela foi tão rápido quanto seu salto permitia-lhe andar. Quanto a você, apenas ficou no mesmo lugar, observando ela e as amigas dançando, felizes por todos os motivos, e ao mesmo tempo sem razão alguma. Por que não podia ser assim com você? Por que você sempre tinha que ficar preso, pela timidez, pelo tempo, pelas lembranças? É uma pena: mesmo depois de tanto esforço, você não descobriu a resposta para a pergunta que te trouxe até ali: O que teria acontecido se você tivesse agido de forma diferente? Nem mesmo uma viagem consciente pelas suas lembranças havia trazido essa resposta. E enquanto você refletia, as luzes iam ficando mais baixas e os sons mais abafados. Tranquilamente, você percebeu que havia chegado a hora de voltar.")
		self.cena1baa.setTexto("	Mesmo nos últimos instantes, um último resquício de coragem parecia ter brotado de você. A expressão da professora mostrou o quanto a sua resposta a deixou espantada. Afinal, você era a grande promessa de um futuro brilhante, como todos os professores costumavam dizer. Mas nem sempre viver pensando no futuro é algo bom; as vezes é preciso pensar no presente. Com você, entretanto, a coisa se dava mais com os tempos 'presente' e 'passado'. Tanto que naquele momento você pressentiu que era hora de embarcar na viagem que o traria de volta para o futuro. Um futuro que você já conhecia, e que agora lamentava ter que voltar.")
		self.cena1bab.setTexto("	Enfim, parecia que o destino, ou seja lá que outras formas de intervenção a vida possui, havia vencido. Não havia sido suficiente nem mesmo reviver o passado, ainda que essa experiência tenha sido provocada por uma máquina em um laboratório subterrâneo da universidade onde você trabalhou desde que concluiu a faculdade. Patrícia, Eryck, a faculdade no exterior, tudo estava ali, acontecendo novamente, exatamente igual como havia sido. Só que agora a viagem chegava ao fim. As imagens a sua frente começavam a desvanecer, e o seu corpo parecia ficar cada vez mais rígido. O útimo módulo, responsável pelo seu despertar, estava finalmente ativo.")
		self.cena1bba.setTexto("	'Eryck, hoje é a última festa que ele vai estar aqui com a gente, esqueceu?' disse Patrícia, com o rosto aborrecido. 'Relaxa, Pati, não quero problemas com ninguém!' e dizendo isso, você se afastou, mas ainda pode perceber que também Patrícia se afastou, o que fez com que Eryck olhasse furioso para você, mas acabou indo atrás da menina. 'Bem', você pensou, 'talvez seja assim que a história deva terminar, então.' A experiência estava sendo concluída com sucesso, mas de um jeito ruim. Muitas coisas se repetiram, a despeito dos seus esforços. Quem sabe essa coisa chamada 'destino' existia, mesmo. De qualquer forma, você já não conseguia pensar direito. A máquina o estava levando de volta ao seu próprio tempo.")
		self.cena1bbb.setTexto("	'Eu sei, e sou eu quem está te mandando embora!' disse Eryck, e levantando, te deu um empurrão. Normalmente um empurrão como aquele poderia no máximo fazer uma pessoa perder o equilíbrio. Mas naquele exato momento você começava a fraquejar, pois a experiência estava chegando ao fim, e a máquina já havia iniciado o módulo que o traria de volta. Você não só caiu, mas também sentiu o forte impacto da cabeça no chão, o que se seguiu de uma dor lancinante na região das têmporas. 'Isaque!' gritou Patrícia, e correndo veio ficar de joelhos ao seu lado. Você entretanto conseguia ver, ouvir e responder cada vez menos. 'Isaque, não!' 'Você gosta de mim, Isaque?' 'Isaque, você tá se sentindo bem?' 'Onde você está, Isaque!' eram frases que se repetiam na sua mente, entoadas pela voz de Patrícia, que segurando as suas mãos quando tudo escureceu.")
		self.cena1aaaa.setTexto("	'Ah, seu bobo, eu também vou morrer de saudade de você!' ela disse, te dando um abraço forte. Você retribuiu, mas reparou que o abraço demorou um pouco mais de tempo do que o normal... para dois amigos. Foi tudo muito rápido o que se seguiu a partir dali. Eryck tinha chegado naquele exato momento e havia entendido mal aquele abraço. 'Eu cansei de ver você dar em cima da minha namorada, cara! Cansei!' ele disse, te dando um empurrão. 'A gente não namora, Eryck!' Patrícia gritou, e àquela altura todos já estavam olhando para vocês três. 'Já que você tá indo embora do país, deixa eu te dar um presente de despedida!' disse Eryck, dando um soco no seu rosto. Estranhamente, aquele soco parecia ter sido mais forte do que o esperado, e você caiu no chão. A última coisa que você ouviu foi um grito de Patrícia. A última coisa... antes que você não visse mais nada.")
		self.cena1aaab.setTexto("	'...de mim?' ela perguntou, e sem querer esbarrou no copo que tinha apoiado em cima da mesa. No mesmo instante ela tentou pegar o copo caído, mas a sua mão encontrou a mão dela antes. Durante aquele simples um segundo, infinitas coisas passaram pela sua cabeça. Anos de trabalho naquele projeto que você manteve em segredo. Viajar no tempo talvez fosse impossível, mas uma viagem pelas suas lembranças parecia algo bem razoável. Os orientais haviam desenvolvido técnicas de sonhos conscientes, por que não inventar uma máquina que permitisse que você sonhasse com as suas lembranças?\n	Patrícia estava especialmente linda naquela noite. Seu vestido longo que parecia ter sido moldado para ela, sua maquiagem que fazia seus olhos brilharem ainda mais. Sem nada dizerem, você se inclinou vagarosamente na direção dela, pois sentia ser a coisa a ser feita, ao que você foi correspondido. Mas tão logo vocês se beijaram, uma dor terrivelmente aguda na sua cabeça fez você franzir o cenho, e sem poder reagir, seu corpo enfraqueceu e você caiu.\n	Tudo o que você podia ver eram vultos. As pessoas olhando para você de cima, o rosto apavorado de Patrícia, a visão cada vez mais turva, e a total impossibilidade de reação. 'Isaque, você tá se sentindo bem?' 'Isaque, acorda!' 'Você gosta de mim, Isaque?' você ouvia Patrícia repetindo. Aparentemente, o tempo havia se esgotado.")

	def inicializaFilhos(self):

		self.cena1.setCenaFilhaA(self.cena1a)
		self.cena1.setCenaFilhaB(self.cena1b)

		self.cena1a.setCenaFilhaA(self.cena1aa)
		self.cena1a.setCenaFilhaB(self.cena1aa)

		self.cena1b.setCenaFilhaA(self.cena1ba)
		self.cena1b.setCenaFilhaB(self.cena1bb)

		self.cena1aa.setCenaFilhaA(self.cena1aaa)
		self.cena1aa.setCenaFilhaB(self.cena1aab)

		self.cena1ba.setCenaFilhaA(self.cena1baa)
		self.cena1ba.setCenaFilhaB(self.cena1bab)

		self.cena1bb.setCenaFilhaA(self.cena1bba)
		self.cena1bb.setCenaFilhaB(self.cena1bbb)

		self.cena1aaa.setCenaFilhaA(self.cena1aaaa)
		self.cena1aaa.setCenaFilhaB(self.cena1aaab)
		

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

	def getCena1ba(self):
		return self.cena1ba

	def getCena1bb(self):
		return self.cena1bb

	def getCena1aaa(self):
		return self.cena1aaa

	def getCena1aab(self):
		return self.cena1aab

	def getCena1baa(self):
		return self.cena1baa

	def getCena1bab(self):
		return self.cena1bab

	def getCena1bba(self):
		return self.cena1bba

	def getCena1bbb(self):
		return self.cena1bbb

	def getCena1aaaa(self):
		return self.cena1aaaa

	def getCena1aaab(self):
		return self.cena1aaab
	
	def getFinal1(self):
		return self.final1

	def getFinal2(self):
		return self.final2

	def getFinal3(self):
		return self.final3
