from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {'nome': pessoa.nome,
                        'idade': pessoa.idade,
                        'id': pessoa.id}
        except AttributeError:
            response = {'status': 'error', 'mensagem': 'Pessoa nao encontrada!'}
        return response

    def put(self,  nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {'id': pessoa.id,
                    'nome': pessoa.nome,
                    'idade': pessoa.idade}
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': f'Pessoa excluida {pessoa} com sucesso'}

class ListaPessoas(Resource):
    def get(self):  # Lista todas as pessoas do banco de dados
        pessoas = Pessoas.query.all()
        response = [{'id': p.id, 'nome': p.nome, 'idade': p.idade} for p in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        # response = [{'id': p.id, 'nome': p.nome, 'idade': p.idade} for p in pessoas]
        return ListaPessoas.get(self)

class ListaAtividades(Resource):
    def get(self):  # Lista todas as atividades do banco de dados
        atividades = Atividades.query.all()
        response = [{'id': a.id, 'nome': a.nome, 'pessoa': a.pessoa.nome} for a in atividades]
        return response


    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {'pessoa': atividade.pessoa.nome, 'nome': atividade.nome, 'id': atividade.id}
        return response


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoa')
api.add_resource(ListaAtividades, '/atividades')


if __name__ == '__main__':
    app.run(debug=True)