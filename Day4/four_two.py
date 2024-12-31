import os

# path to input file
file = open(fr"{os.getcwd()}\word_search.txt")

def find_mas_x(file):
    # placeholder for amount of "XMAS" words found
    count = 0
    # read input file into list of lines and strip newline characters
    word_search = [line.strip() for line in file.readlines()]

    # iterate through lines in the word search
    for i, line in enumerate(word_search):
        # iterate through characters in the line
        for j, char in enumerate(line):
            # look for 'A's to center the 'X's
            if (char == 'A'):
                # check that there is enough space above/below/left/right
                if(0 < i < len(word_search) - 1 and 0 < j < len(line) - 1):
                    # get letters in the two diagonals
                    bwd_slash = ''.join(word_search[i+k][j+k] for k in range(-1, 2))
                    fwd_slash = ''.join(word_search[i+k][j-k] for k in range(-1, 2))

                    # skip to the next character if the backward diagonal is neither 'SAM' nor 'MAS'
                    if('SAM' != bwd_slash != 'MAS'):
                        continue
                    # skip to the next character if the forward diagonal is neither 'SAM' nor 'MAS'
                    elif('SAM' != fwd_slash != 'MAS'):
                        continue
                    # both diagonals passed checks
                    else:
                        # increment count
                        count += 1

    print(count)

find_mas_x(file)

# https://adventofcode.com/2024/day/4
# ANSWER: 1923 (varies with input file)


