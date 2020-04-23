def make_n_gram(seq, n: int) -> list:
    n_gram = []
    for i in range(len(seq)-n+1):
        n_gram.append(seq[i:i+n:])
    return n_gram


str1 = "paraparaparadise"
str2 = "paragraph"
X = set(make_n_gram(str1, 2))
Y = set(make_n_gram(str2, 2))
print(X | Y)
print(X & Y)
print(X - Y)
print("se" in X)
print("se" in Y)
