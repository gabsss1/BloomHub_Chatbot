from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

user_name = 'BloomHub_bot'

# Variable global para controlar si se han mostrado los botones
buttons_shown = False

def handle_response(text: str, context: ContextTypes, update: Update):
    global buttons_shown
    processed_text = text.lower()
    print(processed_text)
    if 'hola' in processed_text:
        # Mostrar botones solo si no se han mostrado antes
        if not buttons_shown:
            buttons_shown = True
            keyboard = [
                [InlineKeyboardButton("Contacto 📞", callback_data='contacto')],
                [InlineKeyboardButton("Catálogo 📓", callback_data='catalogo')],
                [InlineKeyboardButton("Ofertas 🤑", callback_data='ofertas')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            return '¡Bienvenido a BloomHub! 🪴 ¿En qué puedo ayudarte hoy?', reply_markup
        else:
            return '¡Bienvenido a BloomHub! 🪴 ¿En qué puedo ayudarte hoy?', None
    elif 'adios' in processed_text:
        return '¡Hasta luego!', None
    elif 'contacto' in processed_text:
        return 'Puedes contactarnos en support@example.com', None
    elif 'catalogo' in processed_text:
        return 'Nuestro catálogo está disponible en [enlace al catálogo]', None
    elif 'ofertas' in processed_text:
        return 'Consulta nuestras últimas ofertas en [enlace a ofertas]', None
    else:
        return '¿Cómo puedo ayudarte? ¿Necesitas información sobre nuestros productos?', None

async def handle_message(update: Update, context: ContextTypes):
    message_type = update.message.chat.type
    text = update.message.text

    response, reply_markup = handle_response(text, context, update)

    await update.message.reply_text(response, reply_markup=reply_markup)

async def handle_callback_query(update: Update, context: ContextTypes):
    query = update.callback_query
    # Aquí manejamos la lógica según el callback_data
    if query.data == 'contacto':
        await query.answer('Seleccionaste Contacto')
        await query.message.reply_text('Puedes contactarnos en support@example.com')
    elif query.data == 'catalogo':
        await query.answer('Seleccionaste Catálogo')
        await query.message.reply_text('Nuestro catálogo está disponible en [enlace al catálogo]')
    elif query.data == 'ofertas':
        await query.answer('Seleccionaste Ofertas')
        await query.message.reply_text('Consulta nuestras últimas ofertas en [enlace a ofertas]')

async def error(update: Update, context: ContextTypes):
    print(context.error)
    await update.message.reply_text('Ocurrió un error')

if __name__ == '__main__':
    print('Running Chatbot...')
    configure()
    app = Application.builder().token(os.getenv('API_TOKEN')).build()

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_handler(CallbackQueryHandler(handle_callback_query))

    app.add_error_handler(error)

    print('Chatbot iniciado')
    app.run_polling(poll_interval=1, timeout=10)
