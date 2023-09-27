from flask import Flask, request, jsonify
import random
from nltk.tokenize import word_tokenize
import nltk

nltk.download("punkt")

perguntas_respostas = {
    1: "Olá! Como posso ajudar você?",
    2: "Estou bem, obrigado por perguntar.",
    3: "Meu nome é Hero.",
    4: "Tiro dúvidas de algumas funções que podem ser realizadas dentro do jogo.",
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



duvidas = {
    "Menu": {"jogo", "tem opções", "alterar volume"},   
    "op1": "Para iniciar o jogo voce deve ir com mouse até o canto inferior esquerdo da tela e clicar com botão esquerdo do mouse.",
    "op2": "Em configurações e possivel alterar a jogabilidade, vídeo, áudio e controle. ",
    "op3": "Se estiver com problemas de conexão, verifique sua rede, se possivel renicie seu roteador e verifique se não estar com VPN ativo.",
    "op4": "Se estiver com problemas de travamento, reduza a qualidade grafica do jogo e tente diminuir sua resolução."
}
recarga = {
    "Recarga": {"donate"},   
    "op5": "A recarga pode ser feita por dentro da propria loja do jogo a (Steam), ou pelo no site www.Hero2044.com.br.",
    "op6": "Os meios de pagamentos são Pix, Boleto e Cartão de Credito e Debito, ou proprio saldo da loja (Steam).",
    "op7": "Você vai recerber um E-mail com o seu codigo de recarga, após isso basta logar no jogo ir ate a aba resgatar codigo e colar seu codigo lá.",
}


def Duvidas(token):
    opcao = {}
    if token in duvidas["Menu"]:
        opcao = """ㅤㅤop1: Como inicializar jogo?ㅤㅤㅤㅤ
                    ㅤop2: Sobre Configurações?ㅤㅤㅤㅤ
                   ㅤop3: Problemas de Conexão?ㅤㅤㅤㅤ
                   op4: Problemas com FPS?ㅤㅤㅤ"""
        return opcao
    
def Recarga(token):
    opcaoRecarga = {}
    if token in recarga["Recarga"]:
        opcaoRecarga = """ㅤㅤop5: Como Fazer Recarga?ㅤㅤㅤㅤ
                        op6: Quais os meios de pagamento?ㅤ
                        op7: Como resgatar o codigo?"""
        return opcaoRecarga

def ResponderDuvidaMenu(pergunta):
    tokens = word_tokenize(pergunta.lower())
    
    for word in tokens:
       if word in duvidas.keys():          
            if word == "op1":
                resposta = duvidas.get("op1")
                return resposta
            elif word == "op2":
                resposta = duvidas.get("op2")
                return resposta
            elif word == "op3":
                resposta = duvidas.get("op3")
                return resposta
            elif word == "op4":
                resposta = duvidas.get("op4")
                return resposta
    else:
        return "Desculpe não entendi a pergunta."

def RecarregarDuvidas(pergunta):
    tokens = word_tokenize(pergunta.lower())
    
    for word in tokens:
       if word in recarga.keys():          
            if word == "op5":
                resposta = recarga.get("op5")
                return resposta
            elif word == "op6":
                resposta = recarga.get("op6")
                return resposta
            elif word == "op7":
                resposta = recarga.get("op7")
                return resposta
    else:
        return "Desculpe não entendi a pergunta."
       
                
                

app = Flask(__name__)

@app.route('/DetalheResposta', methods=['POST'])
def DetalheResposta():
    data = request.json
    user_question= data['question']
    resposta = ResponderDuvidaMenu(user_question)
    return jsonify({'response': resposta})


@app.route('/ComoRecarregar', methods=['POST'])
def ComoRecarregar():
    data = request.json
    user_question= data['question']
    resposta = RecarregarDuvidas(user_question)
    return jsonify({'response': resposta})



@app.route('/chatBot', methods=['POST'])
def chatbot():
  data = request.json
  user_question= data['question']
  resposta = responder_pergunta(user_question)
  return jsonify({'response': resposta})

def responder_pergunta(pergunta):
    tokens = word_tokenize(pergunta.lower())
    
    if len(tokens) > 2:
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
        
        
    for word in tokens:
        if word in duvidas["Menu"]:        
            return Duvidas(word)
      
    for word in tokens:
        if word in recarga["Recarga"]:        
            return Recarga(word)
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
