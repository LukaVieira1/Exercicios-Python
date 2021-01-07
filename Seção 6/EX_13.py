qtd = int(input('Insira a quantidade de numeros: '))
for n in range(0, qtd+1):
    par = n % 2
    if par == 0:
        print(f'{n}')
