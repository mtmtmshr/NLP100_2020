def sentence_generation(x, y, z):
    return "{}時の{}は{}".format(x, y, z)
    # return str(x) + "時の" + str(y) + "は" + str(z)


print(sentence_generation(x=12, y="気温", z=22.4))
