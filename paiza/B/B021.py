from re import match, sub


def pluralize(word: str):
    if match(r".*?s$|.*?sh$|.*?ch$|.*?o$|.*?x$", word):
        return word + "es"
    if match(r".*?fe?$", word):
        return sub(r"fe?$", "ves", word)
    if match(r".*?y$", word):
        if match(r".*?ay$|.*?ey$|.*?iy$|.*?oy$|.*?uy$", word):
            return word + "s"
        else:
            return sub(r"y$", "ies", word)
    return word + "s"


n = int(input())
words = []

for _ in range(n):
    words.append(input())

for i in words:
    print(pluralize(i))
