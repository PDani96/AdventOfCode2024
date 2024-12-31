import os

# path to input file
file = open(fr"{os.getcwd()}\ids.txt")

def find_distance(file):
    # placeholder for distance value
    distance = 0
    # read input file into list split by newlines
    lines = file.readlines()

    # create a 1x2 list of pairs on each line split by white space and strip the newline characters
    pairs = [[int(id.strip()) for id in line.split("   ")] for line in lines]

    # create two new lists, one of the left column of pairs and one of the right column of pairs
    ids1, ids2 = [pair[0] for pair in pairs], [pair[1] for pair in pairs]

    # sort ascending order
    ids1.sort()
    ids2.sort()

    # create a rolling sum of the difference between ids in the left column and right column
    for i, id in enumerate(ids1):
        distance += abs(id - ids2[i])

    print(distance)

find_distance(file)

# https://adventofcode.com/2024/day/1
# ANSWER: 1873376 (varies with input file)