def distance(strand_a, strand_b):
    differences = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Wrong length of strings!")
    for i in range(len(strand_a)):
        if list(strand_a)[i-1] != list(strand_b)[i-1]:
            differences += 1
    return differences