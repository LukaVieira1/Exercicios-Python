n = ''


while n.lower() != 'nao':
    n = input( 'Deseja saber o consumo de algum veiculo? (sim) ou (nao) ')
    if n == 'nao':
        break
    km, litros = float(input('Quantos km você andou? ')), float(input('Quantos litros foram gastos? '))
    consumo = km / litros
    if consumo < 8:
        print('Gastador')
    elif consumo >=8 and consumo <= 14:
        print('Economico')
    elif consumo > 12:
        print('Super economico')



