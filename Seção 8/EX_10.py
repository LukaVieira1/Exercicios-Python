def maior_num(num1, num2):
    if num1 > num2:
        return num1
    return num2

num1, num2 = int(input('Insira o primeiro valor: ')), int(input('Insira o segundo valor: '))

print(f'O maior numéro é {maior_num(num1, num2)}')
