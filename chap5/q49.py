import re
import copy


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

    def get_masked_clause(self, pos, mask, dist=False):
        if dist:
            for moprh in self.morphs:
                if moprh.get_pos() == pos:
                    return mask

        return "".join([morph.get_surface() if morph.pos != pos
                        else mask for morph in self.morphs
                        if morph.pos != "記号"])


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


def print_on_the_line_pathes(chunks):
    for chunk in chunks:
        pathes = []
        if chunk.is_including_pos("名詞"):
            dst = chunk.get_dst()
            path = [chunk.get_masked_clause("名詞", "X")]
            while dst != -1:
                if chunks[dst].is_including_pos("名詞"):
                    tmp_path = copy.deepcopy(path)
                    tmp_path.append(chunk.get_masked_clause("名詞", "Y", True))
                    pathes.append(tmp_path)
                path.append(chunks[dst].get_normalized_clause())
                dst = chunks[dst].get_dst()
            for path in pathes:
                print(" -> ".join(path))


def print_conflict_pathes(chunks):
    for chunk in chunks:
        pathes = [[]]
        get_conflict_pathes(pathes, chunk, chunks)
        if len(pathes) < 2:
            continue

        for i, pathes_a in enumerate(pathes[:-1], 1):
            for pathes_b in pathes[i:]:
                for path_a in pathes_a[::-1]:
                    for path_b in pathes_b[::-1]:
                        print(path_a[0].get_masked_clause("名詞", "X"), end="")
                        if len(path_a) >= 2:
                            print(" -> " + " -> ".
                                  join([c.get_normalized_clause() for
                                        c in path_a[1:]]), end="")
                        print(" | ", end="")
                        print(path_b[0].get_masked_clause("名詞", "Y"), end="")
                        if len(path_b) >= 2:
                            print(" -> " + " -> ".
                                  join([c.get_normalized_clause() for
                                        c in path_b[1:]]), end="")
                        print(" | ", end="")
                        print(chunk.get_normalized_clause())


def get_conflict_pathes(pathes, chunk, chunks, index=0, path=[]):
    srcs = chunk.get_srcs()
    if len(srcs) == 0:
        return
    else:
        for i, src in enumerate(srcs):
            if len(pathes) <= index+i:
                pathes.append([])
            add_path(pathes, path, chunks[src], index+i)
            tmp_path = copy.deepcopy(path)
            tmp_path.append(chunks[src])
            get_conflict_pathes(pathes, chunks[src], chunks,
                                index+i, tmp_path)


def add_path(pathes, path, chunk, index):
    if chunk.is_including_pos("名詞"):
        tmp_path = copy.deepcopy(path)
        tmp_path.append(chunk)
        pathes[index].append([])
        pathes[index][-1] = tmp_path[::-1]


def print_pathes(chunks):
    print_conflict_pathes(chunks)
    print_on_the_line_pathes(chunks)


chunks_per_sentence = load_dependency_analysis_txt()
print_pathes(chunks_per_sentence[6])
"""
for chunks in chunks_per_sentence:
    print_pathes(chunks)
"""
