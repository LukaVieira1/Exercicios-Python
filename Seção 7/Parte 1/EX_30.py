lista1, lista2 = [], []

for _ in range(11):
    x = int(input('Insira os valores do primeiro vetor: '))
    y = int(input('Insira os valores do segundo vetor: '))
    lista1.append(x)
    lista2.append(y)
set1 = set(lista1)
set2 = set(lista2)

set = set1.intersection(set2)
print(f'{set}')