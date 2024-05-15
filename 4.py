import telebot
from telebot import types

import requests
import time

bot = telebot.TeleBot('6852601494:AAH-ejvEJirOAkatEPqTLa2rbFkmrVREW6I')

# Définir l'ID du développeur
developer_id = 6631613512

# Définir les identifiants des groupes autorisés
allowed_group_chat_ids = [-1002136444842, -1002136444842]

@bot.message_handler(commands=['SH'])
def check_status_command(message):
    if message.from_user.id == developer_id or message.chat.id in allowed_group_chat_ids:
        if len(message.text.split()) == 2:
            player_id = message.text.split()[1]
            check_status(message, player_id)
        else:
            bot.reply_to(message, "𝐕𝐞𝐮𝐢𝐥𝐥𝐞𝐳 𝐟𝐨𝐮𝐫𝐧𝐢𝐫 𝐮𝐧𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐯𝐚𝐥𝐢𝐝𝐞 {𝐩𝐚𝐫 𝐞𝐱𝐞𝐦𝐩𝐥𝐞, 𝐒𝐇 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖}")
    else:
        bot.reply_to(message, "𝐕𝐨𝐮𝐬 𝐧'ê𝐭𝐞𝐬 𝐩𝐚𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐬é à 𝐮𝐭𝐢𝐥𝐢𝐬𝐞𝐫 𝐜𝐞𝐭𝐭𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐞 𝐝𝐚𝐧𝐬 𝐜𝐞 𝐠𝐫𝐨𝐮𝐩𝐞.")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.chat.id in allowed_group_chat_ids:
        bot.reply_to(message, "𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐅𝐫𝐞𝐞 𝐅𝐢𝐫𝐞 𝐁𝐚𝐧 𝐂𝐡𝐞𝐜𝐤 𝐭𝐡𝐞 𝐁𝐨𝐭! 𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚 𝐩𝐥𝐚𝐲𝐞𝐫'𝐬 𝐈𝐃 𝐮𝐬𝐢𝐧𝐠  SH 𝐜𝐨𝐦𝐦𝐚𝐧𝐝 𝐭𝐨 𝐜𝐡𝐞𝐜𝐤 𝐭𝐡𝐞𝐢𝐫 𝐛𝐚𝐧 𝐬𝐭𝐚𝐭𝐮𝐬. 𝐄𝐱𝐚𝐦𝐩𝐥𝐞: SH 𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖 🕵️‍♂️")
    elif message.chat.type == 'private':
        bot.reply_to(message, "𝐉𝐞 𝐧𝐞 𝐬𝐮𝐢𝐬 𝐩𝐚𝐬 𝐩𝐫𝐨𝐠𝐫𝐚𝐦𝐦é 𝐩𝐨𝐮𝐫 𝐫é𝐩𝐨𝐧𝐝𝐫𝐞 à 𝐝𝐞𝐬 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐩𝐫𝐢𝐯é𝐬. 𝐔𝐭𝐢𝐥𝐢𝐬𝐞𝐳-𝐦𝐨𝐢 𝐝𝐚𝐧𝐬 𝐮𝐧 𝐠𝐫𝐨𝐮𝐩𝐞 𝐨ù 𝐣𝐞 𝐬𝐮𝐢𝐬 𝐚𝐮𝐭𝐨𝐫𝐢𝐬é à 𝐟𝐨𝐧𝐜𝐭𝐢𝐨𝐧𝐧𝐞𝐫\n 𝐆𝐑𝐎𝐔𝐏 𝐋𝐈𝐍𝐂𝐊 \n 𝐡𝐭𝐭𝐩𝐬://𝐭.𝐦𝐞/𝐥𝐢𝐨𝐧𝐛𝐨𝐭_𝐯𝟏")
def check_status(message, player_id):
    bot.send_chat_action(message.chat.id, 'typing')  # Indiquer que le bot est en train de taper

    # Envoyer le message "recherche d'informations"
    searching_message = bot.reply_to(message, "Recherche des informations...")

    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={player_id}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'authority': "ff.garena.com",
        'accept-language': "en-GB,en-US;q=0.9,en;q=0.8",
        'referer': "https://ff.garena.com/en/support/",
        'sec-ch-ua': "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-fetch-dest': "empty",
        'sec-fetch-mode': "cors",
        'sec-fetch-site': "same-origin",
        'x-requested-with': "B6FksShzIgjfrYImLpTsadjS86sddhFH",
        'Cookie': "_ga_8RFDT0P8N9=GS1.1.1706295767.2.0.1706295767.0.0.0; apple_state_key=8236785ac31b11ee960a621594e13693; datadome=bbC6XTzUAS0pXgvEs7uZOGJRMPj4wRJzOh2zJmrQaYViaPVLZOIi__jw~cnNaIU1FzrByJ_qVJa7MwmpH3Z2jjRxtDkzsy2hiDTQ4cPY_n0mAwB3seemjGYszNpsfteh; token_session=f40bfc2e69a573f3bdb597e03c81c41f9ecf255f69d086aac38061fc350315ba5d64968819fe750f19910a1313b8c19b; _ga_Y1QNJ6ZLV6=GS1.1.1707023329.1.1.1707023568.0.0.0; _ga_KE3SY7MRSD=GS1.1.1707023591.1.1.1707023591.0.0.0; _gid=GA1.2.1798904638.1707023592; _gat_gtag_UA_207309476_25=1; _ga_RF9R6YT614=GS1.1.1707023592.1.0.1707023592.0.0.0; _ga=GA1.1.925801730.1706287088"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        is_banned = result.get('data', {}).get('is_banned', 0)
        period = result.get('data', {}).get('period', 0)
        if is_banned == 1:
            message_text = f"𓅓3 𝑺 𝑲 𝑹𖤍 - 𝐋𝐈𝐎𝐍 𝐒𝐎𝐔𝐇𝐀𝐈𝐋𓅓\n\n"
            message_text += f"┏ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f"┃ 𒀽   ID du joueur : {player_id}\n"
            message_text += f"┣ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f"┃ 𒀽  Statut : Banni\n"
            message_text += f"┣ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f"┃ 𒀽   Durée : {period} jours\n"
            message_text += f"┗ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f" 💻𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧: @lion_souhail\n"
        else:
            message_text = f"𓅓3 𝑺 𝑲 𝑹𖤍 - 𝐋𝐈𝐎𝐍 𝐒𝐎𝐔𝐇𝐀𝐈𝐋𓅓\n\n"
            message_text += f"┏ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f"┃ 𒀽   ID du joueur : {player_id}\n"
            message_text += f"┣ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f"┃ 𒀽  Statut : Non Banni\n"
            message_text += f"┗ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━ ━\n"
            message_text += f" 💻𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧: @lion_souhail\n"

        # Construire le clavier en ligne
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        url_button = types.InlineKeyboardButton(text="𝐕𝐨𝐢𝐫 𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 ❤️", url="https://www.instagram.com/blrx__souhail?igsh=bXhwd2FuMXd2cXh4")
        keyboard.add(url_button)

        # Envoyer la réponse avec le clavier en ligne
        sent_message = bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

        # Supprimer le message "recherche d'informations" après un délai (par exemple, 3 secondes)
        time.sleep(3)
        bot.delete_message(message.chat.id, searching_message.message_id)
    else:
        bot.reply_to(message, "𝐈𝐦𝐩𝐨𝐬𝐬𝐢𝐛𝐥𝐞 𝐝𝐞 𝐫é𝐜𝐮𝐩é𝐫𝐞𝐫 𝐥𝐞𝐬 𝐝𝐨𝐧𝐧é𝐞𝐬 𝐝𝐞𝐩𝐮𝐢𝐬 𝐥'𝐀𝐏𝐈")

bot.polling()
