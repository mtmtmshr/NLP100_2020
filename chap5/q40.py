import re


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return "surface: {}, base: {}, pos: {}, pos1: {}"\
                .format(self.surface, self.base, self.pos, self.pos1)

    def get_surface(self):
        return self.surface

    def get_base(self):
        return self.base

    def get_pos(self):
        return self.pos

    def get_pos1(self):
        return self.pos1


def load_dependency_analysis_txt():
    with open("neko.txt.cabocha", "r") as f:
        lines = f.readlines()
    morphs = []
    morphs_per_sentence = []
    for line in lines:
        if line[0] == "*":
            continue
        elif line.rstrip("\n") == "EOS" or line.rstrip("\n") == "":
            morphs_per_sentence.append(morphs)
            morphs = []
        else:
            cols = re.split(r"[\t,]", line)
            morphs.append(Morph(cols[0], cols[7], cols[1], cols[2]))

    return morphs_per_sentence


morphs_per_sentence = load_dependency_analysis_txt()
for morphs in morphs_per_sentence:
    for i, morph in enumerate(morphs, 1):
        if i == 3:
            print(morph)
