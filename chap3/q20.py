import gzip
import json


with gzip.open("jawiki-country.json.gz", "rt") as f:
    lines = f.readlines()

for line in lines:
    df = json.loads(line)
    if df["title"] == "イギリス":
        print(df["text"])
        break
