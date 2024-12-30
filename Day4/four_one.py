import os
import re

# path to input file
file = open(fr"{os.getcwd()}\word_search.txt")

def find_xmas(file):
    # placeholder for amount of "XMAS" words found
    count = 0
    # read input file into list of lines and strip newline characters
    word_search = [line.strip() for line in file.readlines()]

    # iterate through lines in the word search
    for i, line in enumerate(word_search):
        # iterate through characters in the line
        for j, char in enumerate(line):
            # look for 'X's to start the word
            if (char == 'X'):
                # check if the following 3 letters finish spelling 'XMAS' (Python's slicing automatically handles edge cases)
                if(line[j+1:j+4] == 'MAS'):
                    # increment count if so
                    count += 1
                # check if the preceding 3 letters finish spelling 'XMAS' backwards (Python's slicing automatically handles edge cases)
                if(line[j-3:j] == 'SAM'):
                    # increment count if so
                    count += 1
                # check if the lower 3 letters finish spelling 'XMAS' downwards (Python's slicing automatically handles edge cases)
                if(''.join([line[j] for line in word_search[i+1:i+4]]) == 'MAS'):
                    # increment count if so
                    count += 1
                # check if the above 3 letters finish spelling 'XMAS' upwards (Python's slicing automatically handles edge cases)
                if(''.join([line[j] for line in word_search[i-3:i]]) == 'SAM'):
                    # increment count if so
                    count += 1

                # handle edge cases manually for diagonals since we are not slicing
                # check that there is enough space below
                if(i < len(word_search) - 3):
                    # check that there is enough space to the right
                    if(j < len(line) - 3):
                        # check if the lower right 3 letters finish spelling 'XMAS' diagonally
                        if(''.join(word_search[i+k][j+k] for k in range(1, 4)) == 'MAS'):
                            # increment count if so
                            count += 1
                    # check that there is enough space to the left
                    if(j > 2):
                        # check if the lower left 3 letters finish spelling 'XMAS' diagonally
                        if (''.join(word_search[i + k][j - k] for k in range(1, 4)) == 'MAS'):
                            # increment count if so
                            count += 1
                # check that there is enough space above
                if (i > 2):
                    # check that there is enough space to the right
                    if (j < len(line) - 3):
                        # check if the upper right 3 letters finish spelling 'XMAS' diagonally
                        if (''.join(word_search[i - k][j + k] for k in range(1, 4)) == 'MAS'):
                            # increment count if so
                            count += 1
                    # check that there is enough space to the left
                    if (j > 2):
                        # check if the lower left 3 letters finish spelling 'XMAS' diagonally
                        if (''.join(word_search[i - k][j - k] for k in range(1, 4)) == 'MAS'):
                            # increment count if so
                            count += 1

    print(count)

find_xmas(file)

# ANSWER: 2504 (varies with input file)


