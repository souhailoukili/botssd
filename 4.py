import telebot
import requests
import json
import time

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6852601494:AAH-ejvEJirOAkatEPqTLa2rbFkmrVREW6I')

# Définir l'ID du développeur
developer_id = 6631613512

# Définir les identifiants des groupes autorisés
allowed_group_chat_ids = [-1002136444842, -1002136444842]

# Replace with your actual cookies and headers
cookies = {
    'source': 'mb',
    '_gid': 'GA1.2.1236421304.1706295770',
    '_gat_gtag_UA_137597827_4': '1',
    'session_key': 'hnl4y8xtfe918iiz2go67z85nsrvwqdn',
    '_ga': 'GA1.2.1006342705.1706295770',
    'datadome': '3AmY3lp~TL1WEuDKCnlwro_WZ1C6J66V1Y0TJ4ITf1Hvo4833Fh4LF3gHrPCKFJDPUPoXh2dXQHJ_uw0ifD8jmCaDltzE5T3zzRDbXOKH9rPNrTFs29DykfP3cfo7QGy',
    '_ga_R04L19G92K': 'GS1.1.1706295769.1.1.1706295794.0.0.0',
}

headers = {
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Origin': 'https://shop.garena.sg',
    'Referer': 'https://shop.garena.sg/app/100067/idlogin',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'accept': 'application/json',
    'content-type': 'application/json',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'x-datadome-clientid': 'DLm2W1ajJwdv~F~a_1d_1PyWnW6ns7GY5ChVcZY3HJ9r6D29661473aQaL2~3Nfh~Vf3m7rie7ObIb1_3eRN7J0G6uFZhMq5pM2jA828fE1dS7rZ7H3MWGQ5vGraAQWd',
}

def get_player_info_from_garena(UID):
    json_data = {
        'app_id': 100067,
        'login_id': UID,
        'app_server_id': 0,
    }
    
    try:
        response = requests.post('https://shop.garena.sg/api/auth/player_id_login', cookies=cookies, headers=headers, json=json_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

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
        status_text = f"not banned" if is_banned == 0 else f"banned for {period} days"
        
        player_info = get_player_info_from_garena(player_id)
        if player_info:
            region = player_info.get('region', 'N/A')
            nickname = player_info.get('nickname', 'N/A')
            img_url = player_info.get('img_url', None)
            
            message_text = (
                "┏━━━━━━━━━━━━━━━━━━\n"
                "┃🧾 PLAYER INFO\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃🔰 ID : {player_id}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃👤 NAME : {nickname}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃🌐 SERVER : {region}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃👾 STATUS : {status_text}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                "┃💻 Développeur : @lion_souhail\n"
                "┗━━━━━━━━━━━━━━━━━━"
            )
            if img_url:
                bot.send_photo(message.chat.id, img_url, caption=message_text)
            else:
                bot.reply_to(message, message_text)
        else:
            message_text = (
                "┏━━━━━━━━━━━━━━━━━━\n"
                "┃🧾 PLAYER INFO\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃🔰 ID : {player_id}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                f"┃👾 STATUS : {status_text}\n"
                "┣━━━━━━━━━━━━━━━━━━\n"
                "┃💻 Développeur : @lion_souhail\n"
                "┗━━━━━━━━━━━━━━━━━━"
            )
            bot.reply_to(message, message_text)
        
        # Supprimer le message "recherche d'informations" après un délai (par exemple, 3 secondes)
        time.sleep(3)
        bot.delete_message(message.chat.id, searching_message.message_id)
    else:
        bot.reply_to(message, "Impossible de récupérer les données depuis l'API")

@bot.message_handler(commands=['SH'])
def check_status_command(message):
    if message.from_user.id == developer_id or message.chat.id in allowed_group_chat_ids:
        if len(message.text.split()) == 2:
            player_id = message.text.split()[1]
            check_status(message, player_id)
        else:
            bot.reply_to(message, "Usage: /SH <player_id>")
    else:
        bot.reply_to(message, "Vous n'êtes pas autorisé à utiliser cette commande.")

@bot.message_handler(func=lambda message: True)
def get_player_info(message):
    if message.chat.id in allowed_group_chat_ids or message.from_user.id == developer_id:
        try:
            UID = message.text.strip()
            player_info = get_player_info_from_garena(UID)
            if player_info:
                region = player_info.get('region', 'N/A')
                nickname = player_info.get('nickname', 'N/A')
                img_url = player_info.get('img_url', None)
                
                message_text = (
                    "┏━━━━━━━━━━━━━━━━━━\n"
                    "┃🧾 PLAYER INFO\n"
                    "┣━━━━━━━━━━━━━━━━━━\n"
                    f"┃🔰 ID : {UID}\n"
                    "┣━━━━━━━━━━━━━━━━━━\n"
                    f"┃👤 NAME : {nickname}\n"
                    "┣━━━━━━━━━━━━━━━━━━\n"
                    f"┃🌐 SERVER : {region}\n"
                    "┣━━━━━━━━━━━━━━━━━━\n"
                    "┃💻 Développeur : @lion_souhail\n"
                    "┗━━━━━━━━━━━━━━━━━━"
                )
                if img_url:
                    bot.send_photo(message.chat.id, img_url, caption=message_text)
                else:
                    bot.reply_to(message, message_text)
            else:
                bot.reply_to(message, "Les informations du joueur ne sont pas disponibles.")
        except Exception as e:
            bot.reply_to(message, f"Une erreur est survenue : {str(e)}")
    else:
        bot.reply_to(message, "Je ne suis pas programmé pour répondre dans ce groupe. Contactez le développeur pour plus d'informations.")

bot.polling()
