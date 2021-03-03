
def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove

        else:
            computadorRemove += 1

    if computadorRemove == 1:
            print()
            print('O computador tirou uma peça')
    else:
            print()
            print('O computador tirou ', computadorRemove, 'peças')

    return computadorRemove


def usuario_escolhe_jogada(n, m):
    jogadaValida = False

    while not jogadaValida:
        jogadorRemove = int(input('Quantas peças você vai tirar? '))
        if jogadorRemove > m or jogadorRemove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()

        else:
            jogadaValida = True

    return jogadorRemove


def partida():

    tipo = int(input("1 - Para partida solo\n2 - Para campeonato: "))

    p = True


    if tipo == 1:

        n = int(input('Quantas peças? '))

        m = int(input('Limite de peças por jogada? ')) 

        p = True
        



        if n % (m+1) == 0:
            print()
            print('Voce começa!')

            while p:

                n = n - usuario_escolhe_jogada(n, m)

                if n == 0 or n < 0:

                    print("você Ganhou! \n")
                    p = False

                else:

                    n = n - computador_escolhe_jogada(n, m)

                    if n == 0 or n < 0:
                        print("O computador venceu! \n")
                        p = False


        else:
          

            print()
            print('Computador começa!')

            while p:
                

                n = n - computador_escolhe_jogada(n, m)

                if n == 0 or n < 0:

                    print("O computador venceu! \n")
                    p = False
                    
                    

                else:

                    n = n - usuario_escolhe_jogada(n, m)

                    if n == 0 or n < 0:

                        print("Você venceu! ")

                        p = False
                        





    else:
        ro = 1

        pc_win = 0
        local_win = 0

        while ro != 4:  # rodada
            p = True

            n = int(input('Quantas peças? '))

            m = int(input('Limite de peças por jogada? '))

            if n % (m+1) == 0:
                print()
                print('Voce começa!')

                while p:

                    n = n - usuario_escolhe_jogada(n, m)

                    if n == 0 or n < 0:

                        print("você Ganhou! \n")
                        p = False
                        ro = ro + 1
                        local_win = local_win + 1


                    else:

                        n = n - computador_escolhe_jogada(n, m)

                        if n == 0 or n < 0:
                            print("O computador venceu! \n")
                            p = False
                            ro = ro + 1
                            pc_win = pc_win + 1


            else:
                print()

                print('Computador começa!')

                while p:



                    n = n - computador_escolhe_jogada(n, m)

                    if n == 0 or n < 0:

                        print("O computador venceu! \n")
                        ro = ro + 1
                        p = False
                        pc_win = pc_win + 1


                    else:

                        n = n - usuario_escolhe_jogada(n, m)

                        if n == 0 or n < 0:
                            print("Você venceu! ")
                            ro = ro + 1
                            p = False
                            local_win = loclocal_win + 1
        
        print("placar: Você {} X {} Computador".format(local_win, pc_win))






partida()




