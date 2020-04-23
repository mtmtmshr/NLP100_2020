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

noun_phrases = []
for sentence_morphs in morphs:
    for i in range(1, len(sentence_morphs)-1):
        if sentence_morphs[i]["base"] == "の":
            if sentence_morphs[i-1]["pos"] == sentence_morphs[i+1]["pos"]\
               == "名詞":
                noun_phrases.append(sentence_morphs[i-1]["surface"] +
                                    sentence_morphs[i]["base"] +
                                    sentence_morphs[i+1]["surface"])

print(noun_phrases)
