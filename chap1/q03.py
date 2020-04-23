import re
str1 = "Now I need a drink, alcoholic of course, "\
       "after the heavy lectures involving quantum mechanics."
# str1 = str1.replace(",", "").replace(".", "")
str1 = re.sub(r"(,|\.)", "", str1)
# str1 = str1.translate(str.maketrans({",": "", ".": ""}))
# str1 = str1.translate(str.maketrans("", "", ",."))
num_of_chars_list = [len(word) for word in str1.split(" ")]
print(num_of_chars_list)
