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

# 強調マークアップの除去
basic_info = re.sub(r"\'{2,5}", "", basic_info.group())

# 内部リンクの除去
basic_info = re.sub(r"\[\[(?!ファイル).*?([^\|\]]*?|\{\{.*?\}\})(?=\]\])\]\]",
                    r"\1", basic_info)

# マークアップの除去
basic_info = re.sub(r"<br\s*\/>", "", basic_info)
basic_info = re.sub(r"<\/*ref(\s|.)*?>", "", basic_info)
basic_info = re.sub(r"\{\{lang\|.*?\|(.*?)\}\}", r"\1", basic_info)
basic_info = re.sub(r"\[\[\ファイル(?:\:|名=)([^\|\]]*).*?\]\]", r"\1", basic_info)
basic_info = re.sub(r"\{\{.*?([^\|]*?)(?=\}\})\}\}", r"\1", basic_info)
basic_info = re.sub(r"\[https?:\/\/[\w\/:%#\$&\?\(\)~\.=\+\-]+(.*?)\]",
                    r"\1", basic_info)

info_pattern = re.compile(r"(?:\|(.*?)\s*=\s*(.*?)"
                          r"(?:(?=\n\|)|(?=\n$)|(?=\n\})))",
                          re.MULTILINE+re.DOTALL)
print(info_pattern.findall(basic_info))
