valores = []
for _ in range(11):
    x = int(input('Insira um valor:'))
    par = x % 2
    if par == 0:
        valores.append(x)
print(f'Possui {len(valores)} valores pares')
