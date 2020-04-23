with open("popular-names.txt", "r") as f:
    lines = f.readlines()
names = set()
for line in lines:
    names.add(line.split("\t")[0])
sorted_names = sorted(names)
for name in sorted_names:
    print(name)
# cut -f 1 popular-names.txt | sort | uniq
