idade = int(input('Qual sua idade? '))
if idade >= 65:
    print('Pode se aposentar')
    exit()
TempoServiço = int(input('Qual tempo de serviço? '))
if TempoServiço >= 30 or (idade >=60 and TempoServiço >= 25):
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
