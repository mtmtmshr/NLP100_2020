import re
import pydot_ng as pydot
import CaboCha


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

    def is_including_pos(self, pos):
        return any([True if morph.pos == pos else False
                    for morph in self.morphs])


def read_dependency_analysis_txt(text: str):
    chunks = {}
    chunks_per_sentence = []
    for line in text.split("\n"):
        if line.rstrip("\n") == "EOS" or line.rstrip("\n") == "":
            if not chunks:
                continue
            sorted_chunks = sorted(chunks.items(), key=lambda x: x[0])
            chunks_per_sentence.append(list(zip(*sorted_chunks))[1])
            chunks = {}
        elif line[0] == "*":
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
        else:
            cols = re.split(r"[\t,]", line)
            morph = Morph(cols[0], cols[7], cols[1], cols[2])
            chunks[idx].add_morphs(morph)

    return chunks_per_sentence[0]


c = CaboCha.Parser()
text = input(">>> ")
tree = c.parse(text)
chunks = read_dependency_analysis_txt(tree.toString(CaboCha.FORMAT_LATTICE))
graph = pydot.Dot(graph_type='digraph')
for i, chunk in enumerate(chunks):
    dst = chunk.get_dst()
    if dst != -1:
        src_clause = chunk.get_normalized_clause()
        dst_clause = chunks[dst].get_normalized_clause()
        if src_clause != "" and dst_clause != "":
            graph.add_node(pydot.Node(i, label=chunk.get_normalized_clause()))
            graph.add_node(pydot.Node(dst,
                           label=chunks[dst].get_normalized_clause()))
            graph.add_edge(pydot.Edge(i, dst))

graph.write_png('q44.png')
