import re
import gzip
import json


def load_uk_text():
    with gzip.open("jawiki-country.json.gz", "rt") as f:
        lines = f.readlines()

    for line in lines:
        df = json.loads(line)
        if df["title"] == "イギリス":
            return df["text"]

    try:
        raise ValueError("error!")
    except ValueError as text:
        return print(text)


text = load_uk_text()
pattern = re.compile(r"\[\[Category:.*?\]\]")
for line in pattern.findall(text):
    print(line.rstrip("\n"))
