from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DB_NAME = 'jogos.db'

def executar_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None

    try:
        cursor.execute(query, params)

        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()

    return resultado

@app.route('/jogos', methods=['GET'])
def listar_jogos():
    dados = executar_query("SELECT * FROM jogos", fetch=True)
    lista = [dict(item) for item in dados]
    return jsonify(lista), 200


@app.route('/jogos/<int:id>', methods=['GET'])
def buscar_jogo(id):
    jogo = executar_query("SELECT * FROM jogos WHERE id = ?", (id,), fetch=True)

    if jogo:
        return jsonify(dict(jogo[0])), 200

    return jsonify({"erro": "Jogo não encontrado"}), 404

@app.route('/jogos', methods=['POST'])
def criar_jogo():
    dados = request.get_json()

    if not dados:
        return jsonify({"erro": "JSON inválido"}), 400

    executar_query(
        """INSERT INTO jogos (nome, genero, plataforma, quantidade, preco)
           VALUES (?, ?, ?, ?, ?)""",
        (
            dados.get('nome'),
            dados.get('genero'),
            dados.get('plataforma'),
            dados.get('quantidade'),
            dados.get('preco')
        ),
        commit=True
    )

    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201
@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    existe = executar_query("SELECT id FROM jogos WHERE id = ?", (id,), fetch=True)
    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        """UPDATE jogos 
           SET nome = ?, genero = ?, plataforma = ?, quantidade = ?, preco = ?
           WHERE id = ?""",
        (
            dados.get('nome'),
            dados.get('genero'),
            dados.get('plataforma'),
            dados.get('quantidade'),
            dados.get('preco'),
            id
        ),
        commit=True
    )

    return '', 204

@app.route('/jogos/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = executar_query("SELECT nome FROM jogos WHERE id = ?", (id,), fetch=True)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query("DELETE FROM jogos WHERE id = ?", (id,), commit=True)

    return jsonify({"mensagem": f"Jogo '{jogo[0]['nome']}' removido!"}), 200

@app.route('/')
def home():
    return jsonify({"mensagem": "API Inventário de Jogos rodando!"})


if __name__ == '__main__':
    app.run(debug=True)