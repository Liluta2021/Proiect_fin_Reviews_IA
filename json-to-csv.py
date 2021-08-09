import pandas as pd
import json

reviews_file = open("./english_reviews.json")


def add_mark(i):
    i["is_good"] = (int(i["evaluation"]) >= 0) * 1
    return i


reviews_json = json.load(reviews_file)
rr = map(add_mark, reviews_json)

df = pd.DataFrame.from_dict(rr)

df.to_csv(r'./en_reviews.csv', index=None, columns=["confidence", "is_good", "evaluation", "text"])
