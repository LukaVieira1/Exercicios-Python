lista_par, lista_impar  = [], []

for _ in range(7):
    x = int(input('Insira um valor: '))
    if (x % 2) == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)
print(f'Numeros pares: {lista_par} sendo a soma deles {sum(lista_par)}')
print(f' Numeros ímpares: {lista_impar} sendo digitados {len(lista_impar)} numeros impares')

