n = int(input(""))
with open("popular-names.txt", "r") as f:
    lines = f.readlines()
for line in lines[-n:]:
    print(line, end="")

# tail -n 5 popular-names.txt
