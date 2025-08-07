import telebot
import config
bot = telebot.TeleBot(config.tg_api_key)


'''----bot commands----'''
@bot.message_handler(commands=["start"])
# func for command/start: Teels about sending of content
def start(message):
    chat_id = message.chat.id
    username = message.from_user.username
    adm_flag = False
    for i in config.admins_usn:
        if username == i:
            adm_flag = True
    if adm_flag == True:
        bot.send_message(chat_id, f"Привет, @{username}, ты — админ. Тебе будут пересылаться сообщения из предложки, готовься)")
    else:
        bot.send_message(chat_id, '''👋Привет! Админы уже ждут твоих истории, так напиши же🙏''')

'''----message handler----'''
@bot.message_handler(func=lambda message: True, content_types=['text', 'image', 'video'])
def msg_answer(message):
    chat_id = message.chat.id
    username = message.from_user.username
    bot.send_message(chat_id=chat_id, text=f"✅Принято! Благодарим за сотрудничество🫂")
    print(f"пользователь @{username}, чат {chat_id} отправил мне предложку, отвечаю ему и пересылаю админу...")
    for i in config.admins_id:
        bot.send_message(chat_id=i, text=f"пользователь @{username} отправил предложку:")
        bot.forward_message(chat_id=i, from_chat_id=chat_id, message_id=message.id)

if __name__ == "__main__":
    bot.infinity_polling()