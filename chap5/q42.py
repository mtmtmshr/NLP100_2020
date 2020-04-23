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


class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __str__(self):
        morphs = ""
        for morph in self.morphs:
            morphs += morph.get_surface()
        return "morphs: {}, dst: {}, srcs: {}"\
               .format(morphs, self.dst, self.srcs)

    def set_dst(self, dst):
        self.dst = dst

    def get_dst(self):
        return self.dst

    def add_morphs(self, morphs):
        self.morphs.append(morphs)

    def add_src(self, src):
        self.srcs.append(src)

    def get_normalized_clause(self):
        return "".join([morph.get_surface() for morph in self.morphs
                        if morph.get_pos() != "記号"])


def load_dependency_analysis_txt():
    with open("neko.txt.cabocha", "r") as f:
        lines = f.readlines()
    chunks = {}
    chunks_per_sentence = []
    for line in lines:
        if line[0] == "*":
            cols = line.split(" ")
            idx = int(cols[1])
            dst = int(re.sub("D", "", cols[2]))
            if idx not in chunks.keys():
                chunks[idx] = Chunk()
            chunks[idx].set_dst(dst)

            if dst != -1:
                if dst not in chunks.keys():
                    chunks[dst] = Chunk()

                chunks[dst].add_src(idx)
        elif line.rstrip("\n") == "EOS" or line.rstrip("\n") == "":
            if not chunks:
                continue
            sorted_chunks = sorted(chunks.items(), key=lambda x: x[0])
            chunks_per_sentence.append(list(zip(*sorted_chunks))[1])
            chunks = {}
        else:
            cols = re.split(r"[\t,]", line)
            morph = Morph(cols[0], cols[7], cols[1], cols[2])
            chunks[idx].add_morphs(morph)

    return chunks_per_sentence


chunks_per_sentence = load_dependency_analysis_txt()
for chunks in chunks_per_sentence:
    for chunk in chunks:
        dst = chunk.get_dst()
        if dst != -1:
            src_clause = chunk.get_normalized_clause()
            dst_clause = chunks[dst].get_normalized_clause()
            if src_clause != "" and dst_clause != "":
                print(src_clause, end="\t")
                print(dst_clause)
