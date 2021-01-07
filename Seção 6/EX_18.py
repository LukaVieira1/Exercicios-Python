qtd = int(input('Insira a quantidade de numeros: '))
cont = 0
num = []
maior = None
for _ in range(1, qtd+1):
    x = int(input('Insira um numero: '))
    num.append(x)
    vezes = max(num)
    maior = maior if maior != None and maior >  x else x

print(f'O maior numero foi {maior} e ele foi inserido {num.count(vezes)} vezes')

