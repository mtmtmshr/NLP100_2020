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
pattern = re.compile(r"(?:(?:ファイル(?:\:|名=)|\{\{Audio\|)"
                     r"([^\|\]]*).*?(?:\]\]|\|))")
for f in pattern.findall(text):
    print(f)

"""
[[ファイル:Wikipedia-logo-v2-ja.png]]
<gallery>
ファイル:Fuchu Yotsuya Bridge 0001.jpg|多摩川[[府中市 (東京都)|府中]]四谷橋
ファイル:Tamagawa Railway bridges of Keio Line.jpg|多摩川京王線鉄橋
</gallery>
{{試聴|
|ファイル名=Japanese nightingale note01.ogg
|タイトル=ウグイスの声
|説明文=関東地方のウグイスの鳴き声。0.4MB
|フォーマット=[[Ogg]]
}
{{Audio|Japanese nightingale note01.ogg|ウグイスの声}}
[[ファイル:Ja-docchi-which.ogg|日本語の「どっち」の発音]]
[[:ファイル:Musi.ogg|虫の鳴き声]]
画像の表示:
[[ファイル:Wiki2.png]]
説明文を追加: ロゴ

説明文を追加:
[[ファイル:Wiki2.png|ロゴ]]
右寄せ:

ロゴ
テキストが画像の左側に回り込みます。
右寄せ:
[[ファイル:Wiki2.png|right|ロゴ]]
テキストが画像の左側に回り込みます。
フレーム形式での表示:
"""