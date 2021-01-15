class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_novo):
        self.__nome = nome_novo


    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade_novo):
        self.__idade = idade_novo

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura_novo):
        self.__altura = altura_novo

    def dados(self):
        print(f'Nome: {self.__nome}\nIdade: {self.__idade}\nAltura: {self.__altura}')


pessoa1 = Pessoa("Luka Vieira", 21, 1.90)

pessoa1.dados()

print(pessoa1.nome, pessoa1.idade, pessoa1.altura)

pessoa1.altura = 1.75
pessoa1.nome = "Claudio"
pessoa1.idade = 25

print(pessoa1.nome, pessoa1.idade, pessoa1.altura)

pessoa1.dados()













