from telegram import Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
import requests
import csv
import os
TOKEN='1389483954:AAEy5j55M1rQyl_NhsFzHTR0jtkVcSWI8U0'
PORT = int(os.environ.get('PORT', 5000))
def writeToCsv(bot,update):
    message=update.message.text
    chat_id = update.message.chat_id
    message_list=message.split("\n")
    topic=message_list[2][7:]
    date=message_list[3][6:18]
    time=message_list[3][19:27]
    with open("ClassTimeLine_"+str(chat_id)+".csv","a+",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([date,time,topic])
def removeFile(bot,update):
    chat_id = update.message.chat_id
    if os.path.exists("ClassTimeLine_"+str(chat_id)+".csv"):
        bot.send_message(chat_id=chat_id, text="Please wait, I am removing your File")
        os.remove("ClassTimeLine_"+str(chat_id)+".csv")
        bot.send_message(chat_id=chat_id, text="File removed sucessfully")
        
    else:
        bot.send_message(chat_id=chat_id, text="File not available")
def getFile(bot,update):
    chat_id = update.message.chat_id
    if os.path.exists("ClassTimeLine_"+str(chat_id)+".csv"):
        bot.send_message(chat_id=chat_id, text="Please wait, I am sending your File")
        bot.send_document(chat_id=chat_id, document=open("ClassTimeLine_"+str(chat_id)+".csv", 'rb'))
        document.close()
    else:
        bot.send_message(chat_id=chat_id, text="File not available")
      
    
def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command,writeToCsv))
    dp.add_handler(CommandHandler("remove_file",removeFile))
    dp.add_handler(CommandHandler("get_file",getFile))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://classtimeline.herokuapp.com/' + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()