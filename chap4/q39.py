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
for i, (word, freq) in enumerate(c.most_common(), 1):
    left.append(i)
    height.append(freq)
rcParams['font.family'] = 'IPAGothic'

plt.scatter(left, height)

ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')

plt.title(
    'graph',
)

plt.xlabel(
    'rank',

)
plt.ylabel(
    'freq',
)

plt.show()
