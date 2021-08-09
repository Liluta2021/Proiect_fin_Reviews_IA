import json
import requests
import urllib.parse
# import tabulate
import pickle

class TelegramBot:
    is_good = 0
    is_bad = 0
    def __init__(self, pipeline_path):
        self.token = '1920254922:AAG-hsEmI_iyJPHir4cQSrGI1iRnxVf1N_0'
        self.url = f"https://api.telegram.org/bot{self.token}"
        self.pipe = pickle.load(open("pipe.pkl","rb"))

    def get_updates(self, offset):
        url = self.url + "/getUpdates?timeout=100"
        if offset:
            url = url +f"&offset={offset+1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)

    def send_message(self, msg, chat_id):
        url = self.url + f'/sendMessage?chat_id={chat_id}&text={urllib.parse.quote_plus(msg)}'
        if msg is not None:
            requests.get(url)

    def chose_reply(self, message, chat_id):
        if message == "/stats":
            self.send_stats(chat_id)
            return
        print(message)
        prediction = self.pipe.predict([message])
        self.is_good += prediction[0] == 1
        self.is_bad += prediction[0] == 0
        self.send_message("Good reviews incremented 👌" if prediction[0] == 1 else "Bad reviews incremented 👀", chat_id)

    def send_stats(self, chat_id):
        self.send_message("Good Reviews 🔥 -> " + str(self.is_good), chat_id)
        self.send_message("Bad Reviews 🛑 -> " + str(self.is_bad), chat_id);


        # print(tabulate([['Goog', chat_id], ['Bad', chat_id]], headers=['is_good', 'is_bad']))