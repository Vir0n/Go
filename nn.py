import random
import time
from datetime import datetime
import telebot

# Insira seu token de acesso do bot do Telegram aqui
TOKEN = '6949496666:AAFLisICFUiuEGAiZMnW4QZCfPy5WUBvrQE'

# Inicializa o bot do Telegram
bot = telebot.TeleBot(TOKEN)

# Função para gerar um campo minado aleatório
def gerar_campo_minado(dimensao, numero_minas):
    campo_minado = [['⚫️' for _ in range(dimensao)] for _ in range(dimensao)]
    for _ in range(numero_minas):
        x, y = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
        while campo_minado[x][y] == '💎':
            x, y = random.randint(0, dimensao - 1), random.randint(0, dimensao - 1)
        campo_minado[x][y] = '💎'
    return campo_minado

# Função para enviar a solução do campo minado para o grupo do Telegram
def enviar_solucao_campo_minado(dimensao, numero_minas):
    campo_minado = gerar_campo_minado(dimensao, numero_minas)
    chance_acerto = round(random.uniform(70, 99), 2)
    mensagem = f"🟢 SINAL CONFIRMADO 🟢\n\nGian Mines 💎\n\n CLIQUE AQUI\n https://bit.ly/FORTUNEVIP \n\n💣 Minas: 3\n⏱ Válido até: próximos 3 mins\n📊 Chance de acerto: {chance_acerto}%\n🔁 Nº de tentativas: 3\n\n"
    for linha in campo_minado:
        mensagem += ' '.join(str(i) for i in linha) + '\n'
    bot.send_message(-1002112118428, mensagem)  # Substitua -100123456789 pelo ID do seu grupo
    
# Loop para enviar a solução do campo minado a cada 5 minutos
while True:
    try:
        enviar_solucao_campo_minado(5, 4)  # Aqui, 5 representa a dimensão e o número de minas
        print(f"Solução do Campo Minado enviada para o grupo às {datetime.now()}")
        time.sleep(300)  # Aguarda 5 minutos (300 segundos) antes de enviar a próxima solução
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
