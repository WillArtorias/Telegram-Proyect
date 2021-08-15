from phonenumbers.phonenumberutil import is_valid_number
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler,MessageHandler,ConversationHandler,Filters
import phonenumbers
from phonenumbers import carrier,geocoder,timezone

input_no=0

def start(update,context):
    update.message.reply_text("Loading\n\n Introduce /number para obtener la informacion")
    
    
def number_handler(update,context):
    update.message.reply_text("Introduce the phone number with country code")
    return input_no

def input_number(update,context):
    text=update.message.text
    chat=update.message.chat
    information=generate_information(text)
    print(information)
    return ConversationHandler.END
def generate_information(text):
    number=phonenumbers.parse(text)
    timezones=timezone.time_zones_for_number(text)
    carriers=carrier.name_for_number(text,"sp")
    valid=is_valid_number(text)
    posibbility=phonenumbers.is_possible_number(text)
    geocode=geocoder.description_for_number(text,"sp","America")
    information="El numero {},se encuentra en la zona de tiempo {}, su proveedor es {}, es un numero valido o no:{} ,existe este numero:{}".format(number,timezones,carriers,valid,posibbility)
    return information
def send_information(information,chat):
    chat.send_action(
        action=ChatAction.FIND_LOCATION
    )
        
if __name__=='__main__':
    updater=Updater(token="1986002567:AAECZEhkZKDxXIgZAFlag6xt3ElkLWifwGo",use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(ConversationHandler(
        entry_points=[CommandHandler("number",number_handler)],
        states={
            input_no:[MessageHandler(Filters.all,input_number)]
            
            },
        fallbacks=[]
           ))

updater.start_polling()
updater.idle()    