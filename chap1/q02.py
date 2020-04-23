str1 = "パトカー"
str2 = "タクシー"
result = ""
for char1, char2 in zip(str1, str2):
    result += char1 + char2
print(result)
