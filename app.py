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

# consultar todos os livros


@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# consultar por ID


@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


app.run(port=5000, host='localhost', debug=True)
