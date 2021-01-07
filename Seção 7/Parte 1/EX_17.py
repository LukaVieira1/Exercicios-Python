lista = []

for _ in range(11):
    x = int(input('Insira o valor: '))
    if x < 0:
        lista.append(0)
    else:
        lista.append(x)
print(f'{lista}')