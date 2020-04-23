with open("popular-names.txt", "r") as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=lambda x: int(x.split("\t")[2]), reverse=True)
for line in sorted_lines:
    print(line.rstrip())

# sort popular-names.txt -rnk 3
