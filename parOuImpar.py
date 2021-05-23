from random import randint
lista = ['Par', 'Ímpar']
contador = 0
print('\033[34mVAMOS JOGAR PAR OU ÍMPAR!\033[m')
while True:
    computador = randint(1, 9)
    numero = int(input('Digite um número: '))
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0]
    print(f'Você escolheu o número {numero} e o computador escolheu o número {computador},', end='')
    if (numero + computador) % 2 == 0:
        print(f' dando um total de {numero + computador} que é PAR')
    elif (numero + computador) % 2 == 1:
        print(f' dando um total de {numero + computador} que é ÍMPAR')
    if escolha in 'Pp':
        if (numero + computador) % 2 == 0:
            print('\033[32mVocê VENCEU\033[m')
        else:
            print('\033[31mVocê PERDEU\033[m')
            break
    if escolha in 'Ii':
        if (numero + computador) % 2 == 1:
            print('\033[32mVocê VENCEU\033[m')
        else:
            print('\033[31mVocê PERDEU\033[m')
            break
    contador += 1
print(f'\033[31mGAME OVER!\033[m \033[32mVocê VENCEU {contador} vezes')
