from tgbot import TelegramBot
from norm import TextNormalizer, WordExtractor, ApplyStemmer

Bot = TelegramBot("Salutare")
update_id = None
while True:
    updates = Bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            if message:
                chat_id = item["message"]["chat"]["id"]
                # if message=="Salutare":
                #     Bot.send_message("Salutare de la mine", chat_id)
                # else:
                #     Bot.send_message("Nu inteleg informatia", chat_id)

                Bot.chose_reply(message, chat_id)