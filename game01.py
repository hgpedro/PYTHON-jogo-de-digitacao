import time
import random

def saudações():
    print("""
---------------------------------------------------------------
<<<<<>>>>>         > Jogo de Digitação <             <<<<<>>>>>
                     >  Bem - Vindo  <
<<<<<>>>>>           >  Multijogador <               <<<<<>>>>>                      
---------------------------------------------------------------
""")

saudações()

palavras= ["verde","amarelo ","vermelho","azul","vermelho","carro","branco","preto","taco","pedra","papel","tesoura","peixe","cachorro","tatu","terra","sapato","luta","jogo","aula"]
modo = 1
j = 2
while True:
    menu = int(input("""
-------------
  > MENU <
 > 1- Jogar
 > 2- Opções
 > 3- Intruções
 > 4- Sair
-------------
 > Digite a Opção: """))
    if menu == 1:
        if modo == 1:
            while True:
                jogador = []
                podium = []
                for j in range(2):
                    nome = input(" > Digite o nome do jogador 1: ")
                    jogador.append(nome) 
                    n= 0
                while True:
                    for j in range(2) :
                        tempototal = 0
                        input(" > {} pressione Enter para começar...".format(jogador[n]))
                        n = n - 1
                        k = 0
                        while k < 10:
                            number= random.randint(10, 60)
                            tempo= time.time()
                            rnumber= int(input(" > ({}) : ".format(number)))
                            tempofinal= time.time()
                            if number == rnumber:
                                k= k + 1 
                                intervalo = tempofinal - tempo
                                tempototal= tempototal + intervalo                     
                            else:
                                continue
                        podium.append(tempototal)
                    tempoprimeirolugar= min(podium)
                    primeirolugar= podium.index(tempoprimeirolugar)
                    temposegundolugar= max(podium)
                    segundolugar= podium.index(temposegundolugar)
                    print("""
-------------------------------------------------------------------------

> Primeiro lugar: {} com o tempo de {} segundos!
> Segundo lugar: {} com o tempo de {} segundos!

-------------------------------------------------------------------------""".format(jogador[primeirolugar],tempoprimeirolugar,jogador[segundolugar],temposegundolugar))
                    break
                break 
        else:
            while True:
                jogador = []
                podium = []
                for j in range(2):
                    nome = input(" > Digite o nome do jogador 1: ")
                    jogador.append(nome)
                    n= 0 
                while True:
                    for j in range(2) :
                        tempototal = 0
                        input(" > {} pressione Enter para começar...".format(jogador[n]))
                        n = n - 1
                        k = 0
                        while k < 10:
                            simbolr= random.choice(palavras)
                            tempo= time.time()
                            simbolra= str(input(" > ({}) : ".format(simbolr)))
                            tempofinal= time.time()
                            if simbolr == simbolra:
                                k= k + 1 
                                intervalo = tempofinal - tempo
                                tempototal= tempototal + intervalo                     
                            else:
                                continue
                        podium.append(tempototal)
                    tempoprimeirolugar= min(podium)
                    primeirolugar= podium.index(tempoprimeirolugar)
                    temposegundolugar= max(podium)
                    segundolugar= podium.index(tempoprimeirolugar)
                    print("""
-------------------------------------------------------------------------

Primeiro lugar: {} com o tempo de {} segundos!
Segundo lugar: {} com o tempo de {} segundos!

-------------------------------------------------------------------------""".format(jogador[primeirolugar],tempoprimeirolugar,jogador[segundolugar],temposegundolugar))
                    break
                break   
    elif menu == 2:
        while True:
            opcoes = int(input("""
  > Opções
 > 1- Mudar de números para palavras
 > 2- Voltar ao menu
 > Digite a Opção: """))
            if opcoes == 1:
                modo+= 2
                break
            elif opcoes == 2:
                break
            else:
                print(""" > Não é uma opção!""")    
    elif menu == 3:
        input("""
  > Intruções <
 > Se quiser mudar o modo vá em opções(2);
 > Após entrar na opção jogar coloque os nomes;
 > Começando o jogo ele irá mandar o jogador digitar algo, tente ser rápido!;
 > Não tem problema errar, pois o jogo sorteia outro número ou palavra;
 > Lembrando que cada jogador tem sua vez;
 > No final do jogo aparece o podium com cada tempo e cada colocação;
 > Aperte Enter para voltar ao menu... """)
    elif menu == 4:
        break
    else:
        print(""" > Não é uma opção!""")