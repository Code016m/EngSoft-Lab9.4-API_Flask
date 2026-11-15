
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de livros
livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 2, "titulo": "O Cortiço", "autor": "Aluísio Azevedo"},
    {"id": 3, "titulo": "Iracema", "autor": "José de Alencar"}
]

# Listar todos os livros
@app.route("/livros", methods=["GET"])
def listar():
    return jsonify(livros), 200

# Buscar livro por ID
@app.route("/livros/<int:id>", methods=["GET"])
def buscar(id):
    for livro in livros:
        if livro["id"] == id:
            return jsonify(livro), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# Adicionar um livro
@app.route("/livros", methods=["POST"])
def adicionar():
    dados = request.get_json(silent=True)
    if not dados or not dados.get("titulo") or not dados.get("autor"):
        return jsonify({"erro": "Informe titulo e autor"}), 400
    novo_livro = {
        "id": max([livro["id"] for livro in livros], default=0) + 1,
        "titulo": dados["titulo"],
        "autor": dados["autor"]
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

# Atualizar um livro
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar(id):
    for livro in livros:
        if livro["id"] == id:
            dados = request.get_json(silent=True)
            if not dados or not dados.get("titulo") or not dados.get("autor"):
                return jsonify({"erro": "Informe titulo e autor"}), 400
            livro["titulo"] = dados["titulo"]
            livro["autor"] = dados["autor"]
            return jsonify(livro), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# Excluir um livro
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir(id):
    for livro in livros:
        if livro["id"] == id:
            livros.remove(livro)
            return jsonify({"mensagem": "Livro excluído"}), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# Executar a aplicação
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
