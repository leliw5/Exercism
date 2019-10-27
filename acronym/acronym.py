import re


def abbreviate(words: str) -> str:
    return re.sub("[^A-Z]", "", " ".join(w.capitalize() for w in re.split(r"[, _\-!?:]+", words)))
