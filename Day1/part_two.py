file = open(r"F:\Users\prest\Documents\Projects\AdventOfCode2024\Day1\input.txt")

def find_similarity(file):
    score = 0
    lines = file.readlines()

    pairs = [[int(id.strip()) for id in line.split("   ")] for line in lines]

    ids1, ids2 = [pair[0] for pair in pairs], [pair[1] for pair in pairs]

    for i, id in enumerate(ids1):
        score += id * ids2.count(id)

    print(score)

find_similarity(file)


