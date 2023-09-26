from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

perguntas_respostas = {
    1: "Olá! Como posso ajudar você?",
    2: "Estou bem, obrigado por perguntar.",
    3: "Meu nome é Hero.",
    4: "Posso responder a perguntas simples.",
    5: "Tchau! Tenha um bom dia!",
}

cumprimento = [
    "olá",
    "oi",
    "iai",
    "opa",
    "oba",
]
curiosidade = [
    "bão",
    "como vc esta",
    "como esta vc",
    "como esta você",
    "como você estar",
]
nomeBot = ["qual seu nome", "seu nome é", "seu nome"]
ajuda = [
    "o que vc faz",
    "vc faz o que",
    "o que você faz",
    "você faz o que",
    "oq vc faz",
    "vc faz oq",
]
encerrar = ["adeus", "até", "obrigado", "ta ok", "ta bom"]

app = Flask(__name__)

@app.route('/chatBot', methods=['POST'])
def chatbot():
  data = request.json
  user_question= data['question']
  resposta = responder_pergunta(user_question)
  return jsonify({'response': resposta})

def responder_pergunta(pergunta):
    tokens = word_tokenize(pergunta.lower())

    if len(tokens) > 1:
        expectativa = tokens[0] + " " + tokens[1] + " " + tokens[2]
        if expectativa in cumprimento:
            resposta = perguntas_respostas.get(1)
            if resposta:
                return resposta
        elif expectativa in curiosidade:
            resposta = perguntas_respostas.get(2)
            if resposta:
                return resposta
        elif expectativa in nomeBot:
            resposta = perguntas_respostas.get(3)
            if resposta:
                return resposta
        elif expectativa in ajuda:
            resposta = perguntas_respostas.get(4)
            if resposta:
                return resposta
        elif expectativa in encerrar:
            resposta = perguntas_respostas.get(5)
            if resposta:
                return resposta

    for word in tokens:
        if word in cumprimento:
            resposta = perguntas_respostas.get(1)
            if resposta:
                return resposta
        else:
            return "Desculpe não entendi a pergunta."
            break


# def chatbot():
#     print("Olá!, sou o Hero. Digite 'Tchau' para finalizar a nossa conversa.")

#     while True:
#         pergunta = input("Você: ")
#         if pergunta.lower() == "tchau":
#             print("ChatBot🤖: Tchau!, Até a próxima.")
#             break
#         reposta = responder_pergunta(pergunta)
#         print("ChatBot:", reposta)


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
