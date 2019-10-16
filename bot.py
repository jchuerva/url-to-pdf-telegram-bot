import logging
import pdfkit

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config.auth import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('AchicaynaBot')


def echo(update, context):
    """Echo the user message."""
    logger.info('url recibida y convirtiendo a pdf')
    chat_id = update.message.chat_id
    url = update.message.text
    pdfkit.from_url(url, 'out.pdf')
    context.bot.send_document(chat_id=chat_id, document=open('out.pdf', 'rb'))
    logger.info('Pdf convertido y enviado')


def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text("""
      👋 Hola y gracias por usarme. Simplemente copia la url y te enviaré el pdf en cuanto lo tenga. ❤️
      """)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


if __name__ == '__main__':
    updater = Updater(token=token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(CommandHandler(['start', 'ayuda', 'help'], start))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
