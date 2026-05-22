from flask import Flask, jsonify
from flask_cors import CORS
from gemini_service import gerar_missao

app = Flask(__name__)
CORS(app)  # Permite que seu frontend (React, Vue, HTML puro) acesse a API sem erros de CORS

@app.route("/gerar-missao")
def missao():
    try:
        # Obtém os dados estruturados da missão
        resposta = gerar_missao()
        
        # Retorna o JSON diretamente
        return jsonify(resposta)
        
    except Exception as e:
        # Caso ocorra algum erro (API key inválida, queda de conexão, etc)
        return jsonify({
            "erro": "Não foi possível gerar a missão.",
            "detalhes": str(e)
        }), 500

if __name__ == "__main__":
    # Roda o servidor local em modo de desenvolvimento
    app.run(debug=True, port=5002)