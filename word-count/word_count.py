import re

def word_count(phrase):
    counts = {}
    words = re.compile(r"[a-zA-Z0-9]+'*[a-zA-Z0-9]+|[a-zA-Z0-9]+")
    for word in re.findall(words, phrase.lower()):
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
    return counts