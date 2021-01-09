with open('texto.txt', 'w+') as texto:
      texto.write(input('Insira um Texto: '))
      texto.seek(0)
      vogais = 'aeiouAEIOU'
      qtd_vogais = len([c for c in texto.readline() if c in vogais])
      print(qtd_vogais)
