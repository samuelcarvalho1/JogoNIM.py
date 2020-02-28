#CAMPEONATO
def campeonato():
    rodadas = 1
    rodadas_faltantes = 2
    while rodadas <= 3:
        print()
        print(" **** Rodada", rodadas,"de 3", "falta(m) mais", rodadas_faltantes, "****")
        print()
        partida()
        rodadas += 1
        rodadas_faltantes -= 1
    print()
    print('Placar: Você 0 X 3 Computador')
#USUÁRIO ESCOLHE JOGADA
def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        usuario_remove = int(input("Quantas peças você gostaria de tirar? "))
        if usuario_remove > m or usuario_remove < 1:
            print()
            print("Oops! Jogada inválida! Tente novamente")
            print()
        else:
            jogada_valida = True
    return usuario_remove

#COMPUTADOR ESCOLHE JOGADA
def computador_escolhe_jogada(n, m):
    computador_remove = 1
    while computador_remove != m:
        if (n - computador_remove) % (m+1) == 0:
            return computador_remove
        else:
            computador_remove += 1
    return computador_remove
    
#DEFINIÇÃO DA PARTIDA
def partida():
    n=1
    m=2
    computador_comeca = False
    while m >= n:
        n = int(input("Quantas peças teremos no jogo? "))
        m = int(input("Qual o limite de peças retiradas por jogada?"))
        if m >= n:
            print()
            print("o número de peças por jogada deve ser menor do que o número total de peças")
            print()
            return(n, m)
        
#ESTRATÉGIA VENCEDORA
    if (n % (m+1)) == 0:
        print()
        print("Por favor, começe!")
        print("Lembre-se: ganha quem tirar a última peça do jogo")
        print()
    else:
            print()
            print("O computador... ou melhor: EUUU vou começar!!!")
            print("Lembre-se: ganha quem tirar a última peça do jogo")
            print()
            computador_comeca = True
                        
    while n > 0:
            if computador_comeca:
                computador_remove = computador_escolhe_jogada(n, m)
                n -= computador_remove 
                print()
                if computador_remove == 1:
                    print("O computador tirou uma peça")
                    if n > 0:
                        print("Agora restarm", n, "peças")
                        print()
                    else:
                        print("Agora restarm Zero peças e você perdeu, porque não há mais peças para tirar")
                                       
                else:
                    print("O computador tirou", computador_remove, "peças")
                    if n > 0:
                        print("Agora restarm", n, "peças")
                        print()
                    else:
                        print("Agora restarm Zero peças e você perdeu porque não há mais peças para tirar")      
                computador_comeca = False
            else:
                usuario_remove = usuario_escolhe_jogada(n, m)
                n -= usuario_remove 
                print()
                if usuario_remove == 1:
                    print("Você tirou uma peça")
                    print("Agora restarm", n, "peças")
                else:
                    print("Você tirou", usuario_remove, "peças")
                    if n > 0:
                        print("Agora restarm", n, "peças")
                    else:
                        print("Agora restarm Zero peças e você ganhou")                               
                computador_comeca = True         

#BOAS VINDAS E INÍCIO
print("Bem vindo ao jogo do NIM!")
print()
print("GANHA QUEM TIRAR A ÚLTIMA PEÇA DO JOGO")
print()
print("ESCOLHA:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
print()
tipodejogo = int(input("Você escolhe 1 ou 2? "))
while tipodejogo != 1 and tipodejogo !=2:
    print()
    tipodejogo = int(input("Você escolhe 1 ou 2? "))
if tipodejogo == 1:
    print()
    print("Você escolheu jogar uma partida isolada!")
    print()
    partida()
else:
    print()
    print("Você escolheu um campeonato!")
    print()
    campeonato()
