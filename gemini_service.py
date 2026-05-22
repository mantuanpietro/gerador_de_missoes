import os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Inicializa o cliente do SDK
client = genai.Client(api_key=os.getenv("MISSOES_API_KEY"))

def gerar_missao():
    prompt = """
    Você é uma IA do sistema ROTA 27, uma inteligência focada em investigações cibernéticas e geográficas pelo Brasil.

    Gere uma missão investigativa brasileira e retorne ESTREITAMENTE um objeto JSON com a seguinte estrutura:
    {
      "titulo": "Título da Missão",
      "personagem": "Nome do Personagem Regional",
      "fala": "Fala do personagem usando gírias reais do estado dele",
      "historia": "Uma pequena história contextualizando o mistério ou crime",
      "pistas": [
        "Pista geográfica 1",
        "Pista geográfica 2",
        "Pista geográfica 3"
      ],
      "resposta": "O estado ou cidade final onde o mistério se resolve"
    }

    REGRAS DE CONTEÚDO:
    - Escolha um estado brasileiro aleatório a cada requisição.
    - O personagem e as gírias devem ser característicos desse estado escolhido.
    - As pistas devem envolver pontos turísticos, biomas, relevo ou a história real daquela região geográfica para que o jogador possa investigar.
    """

    # ATENÇÃO AQUI: O nome precisa ser exatamente 'gemini-2.5-flash'
    resposta = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json"
        ),
    )

    # Converte a string JSON da resposta em um dicionário Python
    dados_missao = json.loads(resposta.text)
    
    return dados_missao