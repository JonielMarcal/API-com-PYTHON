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
]
