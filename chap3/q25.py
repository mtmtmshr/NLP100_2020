import re
import gzip
import json
import regex


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
pattern = re.compile(r"\{\{基礎情報.*", re.DOTALL)
text = pattern.search(text).group()
regex_pattern = r"(?<rec>\{\{(([^{}])|(?&rec))*\}\})"
basic_info = regex.search(regex_pattern, text)
info_pattern = re.compile(r"(?:\|(.*?)\s*=\s*(.*?)"
                          r"(?:(?=\n\|)|(?=\n$)|(?=\n\})))",
                          re.MULTILINE+re.DOTALL)
print(info_pattern.findall(basic_info.group()))
