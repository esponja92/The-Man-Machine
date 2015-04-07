#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Classe para auxiliar nas informacoes relativas aos finais alternativos

"""
class Final(object):

	def __init__(self):

		self.inicializaTextos()

	def inicializaTextos(self):

		self.final1 = "	Uma grande sensação de fraqueza e abatimento se fazia presente por todo o seu corpo. Ao fundo, uma sequência ritmada de sons lentamente ficava mais nítida. Sons que lembravam algum tipo de monitoramento, se você não estava enganado. Quando pode abrir os olhos, menos embaraçado mentalmente você se sentia, mas ainda assim não conseguia reconhecer onde estava. Até que finalmente você parece ter recuperado toda a consciência, e reconhecido que estava em um hospital. Nesse exato momento, uma porta se abriu, e um homem vestido de branco, provavelmente médico ou enfermeiro, entrou no seu quarto.\n\n	(Médico)	- Bom dia, Doutor Isaque!\n(Isaque)	- Onde eu estou?\n(Médico)	- Em um hospital. E graças a Deus você está aqui de novo. Achávamos que você nunca mais conseguiria.\n(Isaque)	- Conseguiria o que? Onde está todo mundo? Patrícia, Eryck, a professora...\n(Médico)	- Calma meu amigo, você acabou de acordar. Pelos documentos que encontramos, percebemos que você estaria sonhando por todo esse tempo. Mas mesmo assim não force demais a sua cabeça, e descanse mais um pouco. Vou pedir para a enfermeira trazer sua refeição.\n\n	Tudo agora estava nítido para você. A máquina, a experiência, os sonhos. No fim, você sobreviveu. Foi bom enquanto durou. Antes que o médico saísse, você perguntou:\n\n(Isaque)	- Doutor! Por quanto tempo eu dormi?\n(Médico)	- A sua jornada durou quinze anos. Espero que tenha encontrado o que procurava. Mas agora descanse, Doutor Isaque, você vai precisar.\n\n	E dizendo isso, o médico fechou a porta.\n"
		self.final2 = "	Certamente era indescritível a sensação que se apoderou de você naquele momento. Uma grande bagunça de imagens descoordenadas de diversos momentos da sua vida e sons, muitos sons. Era impossível dizer quanto tempo aquilo durou, mas enquanto durou pareceu uma verdadeira eternidade. Quando finalmente as coisas começaram a tomar forma e sentido, um grande silêncio pesou em seus ouvidos. Ao mesmo tempo, um pequeno ruído ia se fazendo ouvir cada vez mais, um som que era algo familiar, um som... de soluços. Alguém estava chorando um pranto um tanto ou quanto amargo. Mas o pranto encontrou seu fim no momento em que você abriu os olhos. Você estava deitado em uma cama, em algum lugar que devia ser um hospital, como você acabava de se lembrar. A experiência havia sido bem-sucedida: você havia sobrevivido ao passado, e estava novamente no presente. E ao seu lado, segurando a sua mão, uma mulher de meia idade olhava para você fixamente, com o rosto ainda húmido pelas lágrimas. Você ainda se sentia um pouco desnorteado, mas jamais confundiria o que estava vendo. Não tinha como ser outra pessoa, pois não se vê por aí olhos azuis iguais aos dela. 'Isaque?' ela perguntou sussurando cuidadosamente, como se temesse que o som o pudesse afetar. 'É bom te ver de novo, Patrícia!' você disse. E assim vocês permaneceram por algum tempo, apenas olhando um para o outro. Ela, a menina por quem você era secretamente apaixonado. E você, a pessoa que ela percebeu que não poderia viver sem.\n	Em um canto da sala, uma pilha de jornais. Durante quinze anos, você foi a estrela do mundo científico. 'CIENTISTA ENTRA EM COMA APÓS EXPERIÊNCIA DE REGRESSÃO', 'BUSCA PELO PASSADO JÁ COMPLETA DUAS DÉCADAS' eram algumas das manchetes. Mas a manchete do dia seguinte não seria outra: 'APÓS VINTE ANOS, CIENTISTA ACORDA DE COMA APÓS EXPERIÊNCIA - edição número 1,  Domingo, 3 de fevereiro de 2030.'\n"
		self.final3 = "	Algo estranho acontece. Enquanto tomava suas decisões, cada vez menos você guardava consciência do que estava em curso, e menos você se lembrava da experiência. Os limites entre o sonho e a realidade foram ficando mais tênues à medida em que você transitava entre as camadas temporais, até o ponto em que você se perdeu no emaranhado das suas próprias lembranças. No mundo real, aqueles que chegaram ao laboratório pela manhã, na esperança de o impedirem de testar a máquina em si próprio, encontraram apenas um corpo inerte, em coma, em meio aos equipamentos que mantinham vivo um cérebro dissociado de uma mente. Você jamais voltou a acordar.\n"

	def getFinal1(self):
		return self.final1

	def getFinal2(self):
		return self.final2

	def getFinal3(self):
		return self.final3

