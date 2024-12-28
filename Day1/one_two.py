# path to input file
file = open(r"F:\Users\prest\Documents\Projects\AdventOfCode2024\Day1\input.txt")

def find_similarity(file):
    # placeholder for similarity value
    score = 0
    # read input file into list split by newlines
    lines = file.readlines()

    # create a 1x2 list of pairs on each line split by white space and strip the newline characters
    pairs = [[int(id.strip()) for id in line.split("   ")] for line in lines]

    # create two new lists, one of the left column of pairs and one of the right column of pairs
    ids1, ids2 = [pair[0] for pair in pairs], [pair[1] for pair in pairs]

    # create a rolling sum of the ids in the left list multiplied by how often they occur in the right list
    for id in ids1:
        score += id * ids2.count(id)

    print(score)

find_similarity(file)


