from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/mensagens", methods=["GET"])
def listar_mensagens():
    return jsonify({"mensagens": ["Olá, mundo!"]})

    from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "mensagem": "API funcionando!"
    })


@app.route('/dados', methods=['POST'])
def dados():
    conteudo = request.json
    
    return jsonify({
        "recebido": conteudo
    })

if __name__ == '__main__':
    app.run(debug=True)