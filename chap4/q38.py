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

words = []
for sentence_morphs in morphs:
    for morph in sentence_morphs:
        words.append(morph["base"])
c = collections.Counter(words)
left = []
height = []
for word, freq in c.most_common():
    left.append(freq)
print(left)
rcParams['font.family'] = 'IPAGothic'

plt.hist(left, log=True)

plt.title(
    'graph',
)

plt.xlabel(
    'freq',

)
plt.ylabel(
    'words_num',
)

plt.show()
