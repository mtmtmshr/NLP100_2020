import re


def cipher(str1: str):
    result = "".join([char if not char.islower()
                      else chr(219-ord(char)) for char in str1])
    """
    result = ""
    for char in str1:
        if re.search("[a-z]", char):
            result += chr(219-ord(char))
        else:
            result += char
    """
    return result


str1 = "Hey guys! we have a gift for you!"
ciphertext = cipher(str1)
print(ciphertext)
print(cipher(ciphertext))
