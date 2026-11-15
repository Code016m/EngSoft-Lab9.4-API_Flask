from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"id": 3, "titulo": "Iracema", "autor": "José de Alencar"}
]

@app.route("/livros", methods=["GET"])
def listar():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods=["GET"])
def buscar(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

@app.route("/livros", methods=["POST"])
def adicionar():
    dados = request.json
    novo_livro = {
        "id": max([livro["id"] for livro in livros]) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"],
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar(id):
    for livro in livros:
        if livro["id"] == id:
            dados = request.json
            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]
            return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404

@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro excluído"})
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)