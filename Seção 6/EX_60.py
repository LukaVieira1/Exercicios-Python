num, somanum, maior, menor, qtdnum = 1,  0, None, None, 0
qtdnumpar, somanumpar, medianumpar = 0, 0, 0
while num != 0:
    num = int(input('Insira um numero: '))
    qtdnum += 1
    somanum = somanum + num
    maior = maior if maior != None and maior > num else num
    if num != 0:
        menor = menor if menor != None and menor < num else num
    par = num % 2
    if par == 0 and num != 0:
            qtdnumpar += 1
            somanumpar = somanumpar + num
            medianumpar = somanumpar / qtdnumpar
qtdnum -= 1
medianum = somanum / qtdnum
print(f'A soma dos numeros digitados: {somanum} \nA quantidade de numeros digitados: {qtdnum} \n')
print(f'A média dos números digitados: {medianum} \nMaior numero: {maior} e menor: {menor}')
if medianumpar != 0:
    print(f'A média dos núnmeros pares: {medianumpar}')


