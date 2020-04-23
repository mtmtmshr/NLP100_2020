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
pattern = re.compile(r"(?:(={2,})\s*(.*?)\s*\1)")
for seqtion in pattern.findall(text):
    print(len(seqtion[0])-1, seqtion[1])
