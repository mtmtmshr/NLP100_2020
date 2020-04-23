str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. "\
       "New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_char_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
char_dict = {}
for i, word in enumerate(str1.split(" "), 1):
    if i in one_char_list:
        char_dict[word[0]] = i
        # char_dict.update({word[0]: i})
    else:
        char_dict[word[0:2]] = i
        # char_dict.update({word[0:2]: i})
print(char_dict)
