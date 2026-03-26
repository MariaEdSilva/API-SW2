from flask import Flask, jsonify, request
import os

app = Flask(__name__)

alunos = [
    {"id": 1, "nome": "Ana"},
    {"id": 2, "nome": "Carlos"},
    {"id": 3, "nome": "Carol"}
]

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    novo = request.json
    novo['id'] = len(alunos) +1
    alunos.append(novo)
    return jsonfy(novo), 201