from flask import Flask, request, jsonify

app = Flask(__name__)

veiculos = []

@app.route("/")
def index():
    return "API AutoCare rodando!"

@app.route("/veiculos", methods=["GET"])
def listar():
    return jsonify(veiculos)

@app.route("/veiculos", methods=["POST"])
def cadastrar():
    dados = request.json
    veiculos.append(dados)
    return jsonify({"msg": "cadastrado", "data": dados})

@app.route("/manutencoes/<int:id>", methods=["GET"])
def manutencoes(id):
    if id >= len(veiculos):
        return jsonify({"erro": "nao existe"}), 404

    manutencoes = [
        {"tipo": "Troca de óleo", "km": 10000},
        {"tipo": "Alinhamento e balanceamento", "km": 15000}
    ]

    return jsonify({"veiculo": veiculos[id], "manutencoes": manutencoes})

if __name__ == "__main__":
    app.run(debug=True)
