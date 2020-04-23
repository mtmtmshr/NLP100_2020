import re
import collections
import matplotlib.pyplot as plt
from matplotlib import rcParams


with open("neko.txt.mecab", "r") as f:
    lines = f.readlines()

morphs = []
morphs_per_sentence = []
for line in lines:
    cols = re.split(r"[\t,]", line)
    morph_dict = {}
    morph_dict["surface"] = cols[0]
    morph_dict["base"] = cols[7]
    morph_dict["pos"] = cols[1]
    morph_dict["pos1"] = cols[2]
    morphs_per_sentence.append(morph_dict)

    if morph_dict["surface"] == "。":
        morphs.append(morphs_per_sentence)
        morphs_per_sentence = []


cooccur_word = []
stop_pos = ["助詞", "助動詞", "記号"]
for sentence_morphs in morphs:
    words = []
    for morph in sentence_morphs:
        if morph["pos"] not in stop_pos:
            words.append(morph["base"])
    if "猫" in words:
        words = [word for word in words if word != "猫"]
        cooccur_word += words

c = collections.Counter(cooccur_word)
left = []
height = []
for word, freq in c.most_common()[:10:]:
    left.append(word)
    height.append(freq)
print(left)


rcParams['font.family'] = 'IPAGothic'

plt.bar(left, height)

plt.xlim(
    xmin=-1, xmax=10
)

plt.title(
    'graph',
)

plt.xlabel(
    'top10',

)
plt.ylabel(
    'freq',
)

plt.show()
