import telebot
import random

bot = telebot.TeleBot('8043100316:AAHkIDsMBB5F9vD1N4vTyHzAMSl8AnjWwNE')
#dp = Dispatcher(bot)

@bot.message_handler(commands=['кусь'])
def main(message : telebot.types.Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "mention":# упоминание чере @
                foruser = message.text[entity.offset:entity.offset + entity.length]
               # await message.reply_text(foruser)
    place_for_kusb = ('мизинец', 'лапку', 'руку', 'коленку', 'локоть', 'плечо', 'попу', 'голову', 'ушко', 'шею', 'ногу' ,'нос' ,'предплечье','грудь','бочок','икру','животик','ляшку','пятку','спину','червячка','щеку')
    kak_kusb = ('балуясь','больно','заигрывая','злобно','игриво','исподтишка','нежно','сильно','случайно','шутя')
    random_kak = random.choice(kak_kusb)
    random_place = random.choice(place_for_kusb)
    user = '@' + message.from_user.username+' ' +random_kak+' кусает ' + foruser +' за '+ random_place
    bot.send_message(message.chat.id, user)



@bot.message_handler(commands=['обнять'])
def main(message : telebot.types.Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "mention":# упоминание чере @
                foruser = message.text[entity.offset:entity.offset + entity.length]
               # await message.reply_text(foruser)
    kak_hug = ('подбегает', 'подкрадывается', 'Подкрадывается сзади', 'подлетает', 'подползает', 'подходит')
    hug = ('без желания','возбужденно','жмакая попу','заигрывая','крепко','ласково','нежно','от скуки','растерянно','со всей любовью','стесняясь','тихо','утешающе')
    random_kak_hug = random.choice(kak_hug)
    random_hug = random.choice(hug)
    user = '@' + message.from_user.username+' ' +random_kak_hug+' и ' + random_hug +' обнимает '+ foruser
    bot.send_message(message.chat.id, user)

@bot.message_handler(commands=['я'])
def main(message : telebot.types.Message):
    who = ('богиня весны', 'богиня красоты', 'воришка', 'ворчун', 'дерзкий чувак', 'должен подарок чатерсу сверху', 'ждет свой подарок от чатерса сверху', 'замерз', 'знает эльфийский', 'колдун ебу4ий', 'любимчик главной чайки', 'любит гулять по лужам', 'мандарин столетней выдержки', 'моль с рулеткой')
    random_who = random.choice(who)
    user = '@'+message.from_user.username + ' '+ random_who
    bot.send_message(message.chat.id, user)


bot.polling(non_stop=True)