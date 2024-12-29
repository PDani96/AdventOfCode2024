import os

# path to input file
file = open(fr"{os.getcwd()}\memory_dump.txt")

def scan_memory(file):
    # read input file into string
    instructions = file.read()

    for c in instructions:


    print(instructions)

scan_memory(file)

# ANSWER: ??? (varies with input file)


