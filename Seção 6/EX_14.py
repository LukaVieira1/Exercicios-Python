from collections import defaultdict
lista = []


for _ in range(11):
    x = int(input('Insira o valor: '))
    lista.append(x)

indices = defaultdict(list);

for indice, valor in enumerate(lista):
    indices[valor].append(indice)

for valor in indices:
    if len(indices[valor]) > 1:
        print(valor, indices[valor])
