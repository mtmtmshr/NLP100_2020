n = int(input(""))
with open("popular-names.txt", "r") as f:
    lines = f.readlines()

row_per_file = int(len(lines)/n)
remainder = len(lines) % n
row = 0
for i in range(n):
    with open("popular-names_{}.txt".format(i), "w") as f:
        if remainder > i:
            for line in lines[row:row+row_per_file+1]:
                f.write(line)
            row += row_per_file + 1
        else:
            for line in lines[row:row+row_per_file]:
                f.write(line)
            row += row_per_file
