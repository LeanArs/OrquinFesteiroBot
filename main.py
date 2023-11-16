from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import pytz

#Constantes
chat_id = '-4019595171'
token = '6859849602:AAEMCAPyupSKDE3J0GsGh6Z5qdDkPtmg3yk'

# Definindo o fuso horário de Brasília e horário pra realizar a rotina (so trabalhamos em horário comercial --- ou tentamos)
timezone_brasilia = pytz.timezone('America/Sao_Paulo')
horario_brasilia = datetime.time(8, 00, tzinfo=timezone_brasilia)

# Lista de aniversariantes com suas respectivas datas de nascimento
birthdays = [
    {'name': 'Alexia', 'birthDate': datetime.date(2003, 4, 9)},
    {'name': 'Amanda', 'birthDate': datetime.date(2004, 8, 21)},
    {'name': 'Borges', 'birthDate': datetime.date(2003, 9, 15)},
    {'name': 'Itacaramby', 'birthDate': datetime.date(2003, 4, 24)},
    {'name': 'Pfeilsticker', 'birthDate': datetime.date(2004, 4, 3)},
    {'name': 'Brandão', 'birthDate': datetime.date(2004, 11, 28)},
    {'name': 'Arthur', 'birthDate': datetime.date(2002, 3, 18)},
    {'name': 'Brunomedo', 'birthDate': datetime.date(2002, 11, 4)},
    {'name': 'Menezes', 'birthDate': datetime.date(2003, 11, 15)},
    {'name': 'Caio', 'birthDate': datetime.date(2003, 9, 12)},
    {'name': 'Camila', 'birthDate': datetime.date(2004, 3, 2)},
    {'name': 'Kadu', 'birthDate': datetime.date(2003, 5, 26)},
    {'name': 'Clara', 'birthDate': datetime.date(2002, 11, 2)},
    {'name': 'D2', 'birthDate': datetime.date(2003, 2, 18)},
    {'name': 'Mesquita', 'birthDate': datetime.date(2004, 6, 17)},
    {'name': 'D1', 'birthDate': datetime.date(2003, 2, 18)},
    {'name': 'Storch', 'birthDate': datetime.date(2000, 8, 17)},
    {'name': 'Iagow', 'birthDate': datetime.date(2002, 12, 13)},
    {'name': 'Schmitz', 'birthDate': datetime.date(2002, 2, 26)},
    {'name': 'Morbeck', 'birthDate': datetime.date(1999, 10, 16)},
    {'name': 'Léo', 'birthDate': datetime.date(2003, 2, 25)},
    {'name': 'Luanzin Gameplays', 'birthDate': datetime.date(2002, 6, 8)},
    {'name': 'Ricardo', 'birthDate': datetime.date(1999, 3, 20)},
    {'name': 'Luis', 'birthDate': datetime.date(2001, 3, 27)},
    {'name': 'Marcola', 'birthDate': datetime.date(2002, 1, 25)},
    {'name': 'Maliz', 'birthDate': datetime.date(2003, 9, 30)},
    {'name': 'Abritta', 'birthDate': datetime.date(2002, 7, 2)},
    {'name': 'Malena', 'birthDate': datetime.date(2003, 11, 22)},
    {'name': 'Mari', 'birthDate': datetime.date(2002, 1, 23)},
    {'name': 'Marllon', 'birthDate': datetime.date(2001, 12, 20)},
    {'name': 'Tavinho', 'birthDate': datetime.date(2002, 10, 11)},
    {'name': 'Cabeceira', 'birthDate': datetime.date(2003, 1, 3)},
    {'name': 'PH', 'birthDate': datetime.date(2001, 11, 26)},
    {'name': 'Renan', 'birthDate': datetime.date(2003, 6, 29)},
    {'name': 'Pariz', 'birthDate': datetime.date(2003, 8, 14)},
    {'name': 'Digão', 'birthDate': datetime.date(2001, 11, 10)},
    {'name': 'Rodrigo', 'birthDate': datetime.date(2001, 9, 2)},
    {'name': 'Sabrina', 'birthDate': datetime.date(2002, 2, 15)},
    {'name': 'Tales', 'birthDate': datetime.date(2004, 5, 10)},
    {'name': 'Torugo', 'birthDate': datetime.date(2003, 12, 30)}
]

# Função para enviar mensagem de parabéns caso seja o dia
async def checkBirthday(context: ContextTypes.DEFAULT_TYPE):
    today = datetime.datetime.now(tz=timezone_brasilia).date()
    for someone in birthdays:
        if someone["birthDate"].month == today.month and someone["birthDate"].day == today.day:
            await context.bot.send_message(chat_id=chat_id, text=f"Hoje é aniversário do(a) {someone['nickname']}!!")
            await context.bot.send_message(chat_id=chat_id, text=f"FIIIIIIIIIIIIIIIUUUUUUUUMM PA PA PA POW")
            await context.bot.send_message(chat_id=chat_id, text=f"Feliz aniversário, Orc!")
            

# Função que indica inicialização do bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=chat_id, text=f"Oii! Orquin festeiro chegou!")

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    

    # Agendamento para verificar aniversário diariamente
    application.job_queue.run_daily(checkBirthday, time=horario_brasilia)

    application.run_polling()
