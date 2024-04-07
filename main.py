from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

user_name = 'BloomHub_bot'

#comandos

async def start(update: Update, context: ContextTypes):
    await update.message.reply_text("Hola soy un bot. ¿Necesitas Ayuda?")

async def help(update: Update, context: ContextTypes):
    await update.message.reply_text('Ayuda')

async def custom(update: Update, context: ContextTypes):
    await update.message.reply_text(update.message.text)

def handle_response(text: str,context: ContextTypes,update: Update):
    proccesed_text = text.lower()
    print(proccesed_text)
    if 'hola' in proccesed_text:
        return 'hola como estas?'
    elif 'adios' in proccesed_text:
        return 'bye'
    else:
        return 'habla bien ps'
    
async def handle_message(update: Update, context: ContextTypes):
    message_type = update.message.chat.type
    text = update.message.text

    if message_type == 'group':
        if text.startswith(user_name):
            new_text = text.replace(user_name, '')
            response = handle_response(new_text,context,update)
        else:
            return
    else:
        response = handle_response(text, context, update)

    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ocurrio un error')

if __name__ == '__main__':
    print('Running Chatbot...')
    configure()
    app = Application.builder().token(os.getenv('API_TOKEN')).build()

    app.add_handler(CommandHandler('start',start))
    app.add_handler(CommandHandler('help',help))
    app.add_handler(CommandHandler('echo',custom))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Chatbot iniciado')
    app.run_polling(poll_interval=1, timeout=10)