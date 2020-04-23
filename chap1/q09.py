import random


str1 = "I couldn’t believe that I could actually understand what "\
       "I was reading : the phenomenal power of the human mind ."
words = []
for word in str1.split(" "):
    if len(word) > 4:
        char_list = list(word[1:-1])
        # random.shuffle(char_list)
        """
        等確率に乱順列になるように交換する
        """
        for i in range(len(char_list)-1, 0, -1):
            rand = random.randint(0, i)
            char_list[i], char_list[rand] = char_list[rand], char_list[i]

        """
        指定回数ランダムに交換する
        """
        """
        for _ in range(10):
            rand1 = random.randint(0, len(char_list)-1)
            rand2 = random.randint(0, len(char_list)-1)
            char_list[rand1], char_list[rand2]\
                = char_list[rand2], char_list[rand1]
        """
        word = word[0] + "".join(char_list) + word[-1]
    words.append(word)
print(" ".join(words))
