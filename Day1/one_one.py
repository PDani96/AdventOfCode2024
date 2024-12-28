file = open(r"F:\Users\prest\Documents\Projects\AdventOfCode2024\Day1\input.txt")

def find_distance(file):
    distance = 0
    lines = file.readlines()

    pairs = [[int(id.strip()) for id in line.split("   ")] for line in lines]

    ids1, ids2 = [pair[0] for pair in pairs], [pair[1] for pair in pairs]

    ids1.sort()
    ids2.sort()

    for i, id in enumerate(ids1):
        distance += abs(id - ids2[i])

    print(distance)

find_distance(file)


