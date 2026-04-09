from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
{
"id": 1,
"titulo": "Dom Casmurro",
"autor": "Machado de Assis",
"ano": 1899
}
]

@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def criar_livro():
    novo_livro = request.json
    dados = request.json
    if not dados.get('titulo') or not dados.get('autor'):
        return {"erro": "Título e autor são obrigatórios"}, 400

    if dados['ano'] < 0: return {"erro": "Ano inválido"}, 400

    for livro in livros:
        if livro['titulo'] == dados['titulo']:
            return {"erro": "Livro já cadastrado"}, 400
    return {"mensagem": "Livro cadastrado com sucesso",
    "livro": novo_livro
    }, 201

    novo_livro['id'] = len(livros) + 1
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_infos(id):
    for livro in livros:
        if livro['id'] == id:
            dados = request.json
            livro['titulo'] = dados.get('titulo', livro['titulo'])
            return jsonify(livro)
    return {"erro": "Usuário não encontrado"}, 404

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_registro(id):
    for livro in livros:
        if livro['id'] == id:
            livros.remove(livro)
            return {"mensagem": "Usuário removido"}
    return {"erro": "Usuário não encontrado"}, 404

if __name__ == '__main__':
    app.run(debug=True)