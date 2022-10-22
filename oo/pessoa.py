class Pessoa:        # Classe
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome                # self.nome é atributo de dado e nome é parâmetro que ta no parametro de cima
        self.filhos = list(filhos)      # self.filho é atributo complexo passado uma lista como parametro de cima e é variavel com o asterisco

    def cumprimentar(self):         # Método
        return f'Olá{id(self)}'


if __name__ == '__main__':
    francelmo = Pessoa(nome='Francelmo')        # objeto
    francisco = Pessoa(francelmo, nome='Francisco')
    print(Pessoa.cumprimentar(francelmo))  # Classe.método(parâmetro) - não usual
    print(id(francelmo))
    print(francelmo.cumprimentar())         # passamos o objeto.método() o primeiro paramaetro é o próprio objeto devido ao self declado anteriomente
    print(francelmo.nome)                   # o nome que tava Francelmo passa a ter o Sousa do objeto
    print(francelmo.idade)                  # a idade la do método init é passado agora
    for filho in francisco.filhos:          # para cada filho(var) em objeto.parâmetro
        print(filho.nome)                   # imprimir o filho(var).nome
    francelmo.sobrenome = 'Sousa'           # para se criar atributo em tempo de execução(ou dinâmicamente) passando um novo atributo para o objeto
    del francisco.filhos                    # para deletar os atributos dinamicamento se usa del objeto.atributo
    print(francisco.__dict__)               # para visualizar todos os atributos de instância de um objeto __dict__
    print(francelmo.__dict__)               # para visualizar todos os atributos de instância de um objeto __dict__
