import collections


with open("popular-names.txt", "r") as f:
    lines = f.readlines()
"""
cols1 = []
for line in lines:
    cols1.append(line.split("\t")[0])
c = collections.Counter(cols1)
for name, freq in c.most_common():
    print(name, freq)
"""
cols1 = {}
for line in lines:
    name = line.split("\t")[0]
    if name in cols1.keys():
        cols1[name] += 1
    else:
        cols1[name] = 1
for name, freq in sorted(cols1.items(), key=lambda x: x[1], reverse=True):
    print(name, freq)
# cut -f 1 popular-names.txt | sort -r | uniq -c | sort -rk 1
