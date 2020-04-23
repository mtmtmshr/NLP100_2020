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

    def get_srcs(self):
        return self.srcs

    def get_normalized_clause(self):
        return "".join([morph.get_surface() for morph in self.morphs
                        if morph.get_pos() != "記号"])

    def is_including_pos(self, pos):
        return any([True if morph.pos == pos else False
                    for morph in self.morphs])

    def get_selected_pos_morph(self, pos):
        return [morph for morph in self.morphs if morph.pos == pos]


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
        srcs = chunk.get_srcs()
        verbs = chunk.get_selected_pos_morph("動詞")
        if srcs and verbs:
            case_particles = []
            for src in srcs:
                post_particles = chunks[src].get_selected_pos_morph("助詞")
                if post_particles:
                    if len(post_particles) >= 2:
                        for post_particle in post_particles:
                            if post_particle.get_pos1() == "格助詞":
                                case_particles.append(post_particle)
                    else:
                        case_particles.append(post_particles[0])
            if case_particles:
                print(verbs[0].get_base() + "\t" +
                      " ".join(sorted([c.get_base() for c in case_particles])))

#  sort q45.txt | uniq -c | sort -rn
# grep ^"する" q45.txt | sort | uniq -c | sort -rn
