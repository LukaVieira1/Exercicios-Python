def ler_caracteres():
    with open('arq.txt', 'w') as arq:
        while True:
            caractere = input('Insira um caractere ou escreva "0" para sair: ')
            if caractere != '0':
                arq.write(caractere + '\n')
            else:
                break


def imprimir_caracteres():
    with open('arq.txt') as arq:
        arq.seek(0)
        print(arq.readlines())

ler_caracteres()
imprimir_caracteres()







