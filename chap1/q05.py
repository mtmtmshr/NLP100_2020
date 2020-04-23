def make_n_gram(seq, n: int) -> list:
    n_gram = []
    for i in range(len(seq)-n+1):
        n_gram.append(seq[i:i+n:])
    return n_gram


str1 = "I am an NLPer"
char_bi_gram = make_n_gram(str1, 2)
word_bi_gram = make_n_gram(str1.split(" "), 2)
print(char_bi_gram)
print(word_bi_gram)
