import requests
import telebot
import re
import threading

bot = telebot.TeleBot("7180634708:AAER89JJRZPiWd8unIe2bfjyntq4HATIpQA")

# Define the group chat IDs
allowed_group_chat_ids = [-1002017761926, -1002136444842]  # Remplacez par les identifiants de vos groupes de discussion réels

# Définir l'identifiant de l'utilisateur développeur
developer_user_id = "6631613512"

def search_player(message, uid):
    try:
        region = "sg"  # Remplacez par la région appropriée si nécessaire
        data = {'info_type': 'user', 'server': region, 'id': uid}

        response = requests.post("https://www.freefireinfo.site/", data=data)
        if response.status_code == 200:
            match = re.findall(r"strong>Account Name:</strong>(.*?)</li>", response.text)
            if match:
                name = match[0].strip()
                if message.chat.type == 'private':
                    bot.reply_to(message, f"𝙁𝙤𝙪𝙣𝙙 𝙋𝙡𝙖𝙮𝙚𝙧: {𝙣𝙖𝙢𝙚}\n 𝙇𝙚 𝙗𝙤𝙩 𝙚𝙣𝙫𝙚𝙧𝙧𝙖 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙦𝙪𝙚𝙢𝙚𝙣𝙩 +99999")
                else:
                    bot.send_message(message.chat.id, f"𝙁𝙤𝙪𝙣𝙙 𝙋𝙡𝙖𝙮𝙚𝙧: {𝙣𝙖𝙢𝙚}\n 𝙇𝙚 𝙗𝙤𝙩 𝙚𝙣𝙫𝙚𝙧𝙧𝙖 𝙖𝙪𝙩𝙤𝙢𝙖𝙩𝙞𝙦𝙪𝙚𝙢𝙚𝙣𝙩 +99999")
            else:
                if message.chat.type == 'private':
                    bot.reply_to(message, "Player name not found in response.")
                else:
                    bot.send_message(message.chat.id, "Player name not found in response.")
        else:
            if message.chat.type == 'private':
                bot.reply_to(message, f"Player Not Found, Status Code: {response.status_code}")
            else:
                bot.send_message(message.chat.id, f"Player Not Found, Status Code: {response.status_code}")
    except Exception as e:
        if message.chat.type == 'private':
            bot.reply_to(message, f"Error: {str(e)}")
        else:
            bot.send_message(message.chat.id, f"Error: {str(e)}")

@bot.message_handler(func=lambda message: message.chat.id in allowed_group_chat_ids or message.chat.type == 'private')
def handle_message(message):
    if message.text.startswith('SH'):
        try:
            uid = message.text.split()[1]
            bot.send_message(message.chat.id, "𝙍𝙚𝙘𝙝𝙚𝙧𝙘𝙝𝙚 𝙙𝙪 𝙟𝙤𝙪𝙚𝙪𝙧...⏳")
            threading.Thread(target=search_player, args=(message, uid)).start()
        except IndexError:
            if message.chat.type == 'private':
                bot.reply_to(message, "Invalid format. Please enter the input in the correct format: SH 12345678")
            else:
                bot.send_message(message.chat.id, "Invalid format. Please enter the input in the correct format: SH 12345678")
        except Exception as e:
            if message.chat.type == 'private':
                bot.reply_to(message, f"Error: {str(e)}")
            else:
                bot.send_message(message.chat.id, f"Error: {str(e)}")

bot.polling()
