# path to input file
file = open(r"reports.txt")

def safety_test(file):
    # placeholder for number of safe reports
    passes = 0
    # read input file into list split by newlines
    lines = file.readlines()

    # create 1xN list of reports containing N levels split by whitespace and strip newline characters
    reports = [[int(level.strip()) for level in line.split(' ')] for line in lines]

    print(reports)

safety_test(file)


