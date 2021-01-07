
from collections import Counter
sexos, cores_olhos, cores_cabelos, idades, qtd_olhos_cabelos = [], [], [], [], 0 # Variaveis da função ler_dados
def ler_dados():
    global sexos, cores_olhos, cores_cabelos, idades, qtd_olhos_cabelos
    for _ in range(2):
        sexo, cor_olhos = (input('Masculino ou Feminino? ')), input('Qual a cor dos seus olhos? Azuis (L) ou Castanhos (C):  ')
        cor_cabelo, idade = input('Qual a cor do seu cabelo? Louros (L), Pretos (P) ou Castanhos (C):  '), int(input('Qual a sua idade? '))
        if (cor_olhos.lower() == 'c') and (cor_cabelo.lower() == 'p'):
            qtd_olhos_cabelos = qtd_olhos_cabelos +1
        sexos.append(sexo)
        cores_olhos.append(cor_olhos)
        cores_cabelos.append(cor_cabelo)
        idades.append(idade)


def media_idade():
    olhos_local = Counter(cores_olhos)
    cabelos_local = Counter(cores_cabelos)
    print(f'{qtd_olhos_cabelos}')
    #media = qtd_olhos_cabelos / 5
    #return media

def maior_idade():
    max_idade = max(idades)
    return max_idade


def qtd_idade():
    global idades, cores_cabelos, cores_olhos
    idade = Counter(idades)
    cabelos = Counter(cores_cabelos)
    olhos_local = Counter(cores_olhos)



ler_dados()
print(f'{media_idade()}')