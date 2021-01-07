opção = int(input('Selecione: \n 1.Adição 2.Subtração 3.Divisão 4.Multiplicação\n'))
v1, v2 = int(input('Insira 2 valores: \n')), int(input())
if opção == 1:
    resultado = v1 + v2
    print(f'O resultado é {resultado}')
elif opção == 2:
    resultado = v1 - v2
    print(f'O resultado é {resultado}')
elif opção == 3:
    resultado = v1 / v2
    print(f'O resultado é {resultado}')
elif opção == 4:
    resultado = v1 * v2
    print(f'O resultado é {resultado}')





