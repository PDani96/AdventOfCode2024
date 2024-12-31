import os
import re

# path to input file
file = open(fr"{os.getcwd()}\memory_dump.txt")

def scan_memory_conditional(file):
    # placeholder for sum of instructions' results
    result = 0
    # flag for noting if multiplication is enabled or disabled. Default to enabled
    enable = True
    # read input file into string
    instructions = file.read()

    # define regex pattern for valid multiple or enable/disable commands
    regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    # find all uncorrupted instructions
    uncorrupted_instructions = re.findall(regex, instructions)

    # placeholder to store cleaned instructions
    cleaned_instructions = []

    # iterate through every uncorrupted instruction to determine which instructions are enabled/disabled.
    for i, ui in enumerate(list(uncorrupted_instructions)):
        # instructions are currently enabled
        if enable:
            # set enable to false if disable function is encountered
            if(ui == 'don\'t()'):
                enable = False
            # instructions are already enabled, store all instructions except for extra enable instructions
            elif(ui != 'do()'):
                cleaned_instructions.append(ui)
        # instructions are currently disabled
        else:
            # re-enable instructions
            if(ui == 'do()'):
                enable = True
            # all other instructions are disabled, ignore them

    # re-define regex pattern using grouping to easily extract the numbers to multiply
    regex = r"(\d+),(\d+)"
    # loop through all matches
    for mul in cleaned_instructions:
        # store grouped matches
        numbers = re.search(regex, mul)
        # multiply the first group from the match by the second group
        result += int(numbers.group(1)) * int(numbers.group(2))

    print(result)

scan_memory_conditional(file)

# https://adventofcode.com/2024/day/3
# ANSWER: 102467299 (varies with input file)


