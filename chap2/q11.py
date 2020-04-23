with open("popular-names.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line.replace("\t", " "), end="")

# cat popular-names.txt | sed -e $'s/\t/ /g'
# sed -e $'s/\t/ /g' popular-names.txt
# cat popular-names.txt | tr '\t' ' '
# expand -t 1 popular-names.txt
