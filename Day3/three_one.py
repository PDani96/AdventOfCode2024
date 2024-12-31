import os
import re

# path to input file
file = open(fr"{os.getcwd()}\memory_dump.txt")

def scan_memory(file):
    # placeholder for sum of instructions' results
    result = 0
    # read input file into string
    instructions = file.read()

    # define regex pattern
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    # use regex to get a list of all instructions that match
    uncorrupted_instructions = re.findall(regex, instructions)

    # redefine regex pattern using grouping to easily extract the numbers to multiply
    regex = r"(\d+),(\d+)"
    # loop through all matches
    for ui in uncorrupted_instructions:
        # store grouped matches
        numbers = re.search(regex, ui)
        # multiply the first group from the match by the second group
        result += int(numbers.group(1)) * int(numbers.group(2))

    print(result)

scan_memory(file)

# https://adventofcode.com/2024/day/3
# ANSWER: 178538786 (varies with input file)


