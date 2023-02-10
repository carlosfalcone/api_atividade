from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Eduardo', idade=45)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Eduardo').first()
    print(pessoa.idade)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Eduardo').first()
    # pessoa.idade = 46
    pessoa.nome = 'Falcone'
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Falcone').first()
    pessoa.delete()

if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()