from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Velozes e Furiosos - 8',
        'autor': 'Joniel Marçal'
    },
    {
        'id': 2,
        'titulo': 'Senhor dos Aneis - 2',
        'autor': 'Felix Pina'
    },
    {
        'id': 3,
        'titulo': 'A Vingança Sombria ',
        'autor': 'Jean Marcos Tomas'
    },
    {
        'id': 4,
        'titulo': 'O Rei da Bola',
        'autor': 'Reytler Matheus'
    },
]

# consultar todos os livro


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar por ID


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# editar o livro, recebendo ID


@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# add um novo livro


@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)


@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
