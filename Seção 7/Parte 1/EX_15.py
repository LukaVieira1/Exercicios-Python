lista = []

for _ in range(21):
    x = int(input('Insira o valor: '))
    lista.append(x)

set = set(lista)
print(f' {set}')