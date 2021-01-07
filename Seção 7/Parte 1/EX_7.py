valores, maior = [], None
for _ in range(11):
    x = int(input('Insira um valor: '))
    valores.append(x)
    maior = maior if maior != None and maior > x else x

print(f'O maior valor lido foi {maior} e está na pisição {valores.index(maior)}')