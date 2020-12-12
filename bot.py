from telegram import Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import csv
import os
TOKEN='1389483954:AAEy5j55M1rQyl_NhsFzHTR0jtkVcSWI8U0'
PORT = int(os.environ.get('PORT', 5000))
def writeToCsv(bot,update):
    message=update.message.text
    message_list=message.split("\n")
    n=int(len(message_list)/10)
    for i in range(n):
        topic=message_list[10*i+2][7:]
        date=message_list[10*i+3][6:18]
        time=message_list[10*i+3][19:27]
        with open("ClassTimeLine.csv","a+",newline="") as file:
            writer=csv.writer(file)
            writer.writerow([date,time,topic])

def getFile(bot,update):
    chat_id = update.message.chat_id
    if os.path.exists("ClassTimeLine.csv"):
        bot.send_message(chat_id=chat_id, text="Please wait, I am sending your File")
        bot.send_document(chat_id=chat_id, document=open("ClassTimeLine.csv", 'rb')

    else:
        bot.send_message(chat_id=chat_id, text="File not available")

def start(bot,update):
    chat_id = update.message.chat_id
    title=update.message.from_user["first_name"]
    bot.send_message(chat_id=chat_id, text="Hi "+str(title)+" welcome to this Bot. I am feeling great to see you here.")
    
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,writeToCsv))
    dp.add_handler(CommandHandler("remove_file",removeFile))
    dp.add_handler(CommandHandler("get_file",getFile))
    dp.add_handler(CommandHandler("start",start))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://classtimeline.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()