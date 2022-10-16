class Pessoa:        # Classe
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome                # self.nome é atributo de dado e nome é parâmetro que ta no parametro de cima

    def cumprimentar(self):         # Método
        return f'Olá{id(self)}'


if __name__ == '__main__':
    p = Pessoa('Francelmo')        # objeto
    print(Pessoa.cumprimentar(p))  # Classe.método(parâmetro) - não usual
    print(id(p))
    print(p.cumprimentar())         # passamos o objeto.método() o primeiro paramaetro é o próprio objeto devido ao self declado anteriomente
    print(p.nome)                   # o nome que tava None passa a ter o parametro do objeto
    p.nome = 'Sousa'                # posso alterar o nome
    print(p.nome)                   # o nome que tava Francelmo passa a ter o Sousa do objeto
    print(p.idade)                  # a idade la do método init é passado agora
