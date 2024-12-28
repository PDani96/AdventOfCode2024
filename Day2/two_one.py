# path to input file
file = open(r"reports.txt")

def safety_test(file):
    # placeholder for number of safe reports
    passes = 0
    # read input file into list split by newlines
    lines = file.readlines()

    # create 1xN list of reports containing N levels split by whitespace and strip newline characters
    reports = [[int(level.strip()) for level in line.split(' ')] for line in lines]

    # iterate through every report
    for report in reports:
        # initially assume this report is safe
        safe = True
        # initialize a neutral direction tracker (pos+ values mean ascending, neg- values mean descending)
        direction = 0

        # test initial direction and assign corresponding value
        if(report[0] < report[1]):
            direction = 1
        elif(report[0] > report[1]):
            direction = -1
        # pre-emptively fail report if first two levels are equal to save time
        else:
            safe = False

        # if report is initially safe start iterating through the levels in the report
        if safe:
            for i, level in enumerate(report):
                # check that we aren't on the last level of the report
                if(i < len(report) - 1):
                    # check that adjacent levels aren't equal
                    if(report[i] == report[i + 1]):
                        # adjacent levels must differ by at least one, report is unsafe
                        break
                    # check if direction marker is ascending
                    elif(direction > 0):
                        # check distance between levels
                        if(report[i + 1] - report[i] > 3):
                            # mark report as unsafe if difference is greater than 3
                            break
                        elif(report[i +1] - report[i] < 0):
                            # a negative difference means the direction changed and the report is unsafe
                            break
                    # otherwise, direction marker is descending
                    else:
                        # check distance between levels
                        if(report[i] - report[i + 1] > 3):
                            # mark report as unsafe if difference is greater than 3
                            break
                        elif(report[i] - report[i + 1] < 0):
                            # a negative difference means the direction changed and the report is unsafe
                            break
                # end of report has been reached
                else:
                    # double-check report is still safe
                    if safe:
                        # increment number of safe reports
                        passes += 1


    print(passes)

safety_test(file)


