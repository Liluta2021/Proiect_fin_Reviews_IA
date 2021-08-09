import json
from googletrans import Translator
import simplejson

# google stuff
translator = Translator()

reviews_file = open("./reviews.json")

reviews_json = json.load(reviews_file)
translated_reviews = []

t = 0
debug = False

for conference_paper in reviews_json["paper"]:
    if t == 5 and debug:
        break
    for review in conference_paper["review"]:
        t += 1
        if t == 5 and debug:
            break
        if review["lan"] == "en" or (not review["text"]):
            translated_reviews.append(review)
            continue
        try:
            print("\033[92m" + review["text"])
            translation = translator.translate(review["text"][0:14999], dest='en')
            print("\033[94m trans: " + translation.text)
            review["text"] = translation.text
            translated_reviews.append(review)
        except:
            print("\033[91m" + " Error")


with open("english_reviews2.json", "w") as outfile:
    simplejson.dump(translated_reviews, outfile)
