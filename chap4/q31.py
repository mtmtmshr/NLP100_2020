import re


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

for sentence_morphs in morphs:
    for morph in sentence_morphs:
        if morph["pos"] == "動詞":
            print(morph["surface"])
