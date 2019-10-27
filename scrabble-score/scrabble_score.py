def score(word: str) -> int:
    values = dict()
    values[1] = 'A, E, I, O, U, L, N, R, S, T'.split(", ")
    values[2] = 'D, G'.split(", ")
    values[3] = 'B, C, M, P'.split(", ")
    values[4] = 'F, H, V, W, Y'.split(", ")
    values[5] = 'K'
    values[8] = 'J, X'.split(", ")
    values[10] = 'Q, Z'.split(", ")
    points = 0
    for letter in word:
        for key, value in values.items():
            if letter.upper() in value:
                points += key
    return points
