import os

# path to input file
file = open(fr"{os.getcwd()}\reports.txt")

def safety_test_dampener(file):
    # placeholder for list of safe reports
    passes = []
    # read input file into list split by newlines
    lines = file.readlines()

    # create 1xN list of reports containing N levels split by whitespace and strip newline characters
    reports = [[int(level.strip()) for level in line.split(' ')] for line in lines]

    # iterate through every report
    for i, report in enumerate(reports):
        # initially assume this report is safe
        safe = True
        # initialize a neutral direction tracker (pos+ values mean ascending, neg- values mean descending)
        direction = 0

        # test initial direction and assign corresponding value
        if(report[0] < report[1]):
            direction = 1
        elif(report[0] > report[1]):
            direction = -1

        # iterating through the levels in the report
        for j, level in enumerate(report):
            # check that we aren't on the last level of the report
            if(j < len(report) - 1):
                # check that adjacent levels aren't equal
                if(report[j] == report[j + 1]):
                    # adjacent levels must differ by at least one, report is unsafe
                    break
                # check if direction marker is ascending
                elif(direction > 0):
                    # check distance between levels
                    if(report[j + 1] - report[j] > 3):
                        # mark report as unsafe if difference is greater than 3
                        break
                    elif(report[j +1] - report[j] < 0):
                        # a negative difference means the direction changed and the report is unsafe
                        break
                # otherwise, direction marker is descending
                else:
                    # check distance between levels
                    if(report[j] - report[j + 1] > 3):
                        # mark report as unsafe if difference is greater than 3
                        break
                    elif(report[j] - report[j + 1] < 0):
                        # a negative difference means the direction changed and the report is unsafe
                        break
            # end of report has been reached
            else:
                # double-check report is still safe
                if safe:
                    # track index of safe reports
                    passes.append(i)

    # now do a more in depth safety test on the remaining "failed" tests by testing safety after the removal of one level at a time
    # iterate through every report again
    for i, report in enumerate(reports):
        # iterate through levels in report for removal
        for j, level in enumerate(report):
            # only test report if it has not already passed
            if (passes.count(i) == 0):
                # create a temporary report for testing the current report
                temp_report = report.copy()
                # remove the current level from the temp report
                temp_report.pop(j)

                # double check direction of levels after removal of the current level (removal of first or second level can impact direction)
                if (temp_report[0] < temp_report[1]):
                    direction = 1
                elif (temp_report[0] > temp_report[1]):
                    direction = -1

                # iterate through new temporary report to test if it passes without the current level
                for k, temp_level in enumerate(temp_report):
                    # check that we aren't on the last level of the temp report
                    if (k < len(temp_report) - 1):
                        # check that adjacent levels aren't equal
                        if (temp_report[k] == temp_report[k + 1]):
                            # adjacent levels must differ by at least one, temp report is unsafe, try again with removing the next level
                            break
                        # check if direction marker is ascending
                        elif (direction > 0):
                            # check distance between levels
                            if (temp_report[k + 1] - temp_report[k] > 3):
                                # mark temp report as unsafe if difference is greater than 3, try again with removing the next level
                                break
                            elif (temp_report[k + 1] - temp_report[k] < 0):
                                # a negative difference means the direction changed and the temp report is unsafe, try again with removing the next level
                                break
                        # otherwise, direction marker is descending
                        else:
                            # check distance between levels
                            if (temp_report[k] - temp_report[k + 1] > 3):
                                # mark temp report as unsafe if difference is greater than 3, try again with removing the next level
                                break
                            elif (temp_report[k] - temp_report[k + 1] < 0):
                                # a negative difference means the direction changed and the temp report is unsafe, try again with removing the next level
                                break
                    # end of report has been reached
                    else:
                        # double-check report is still safe
                        if safe:
                            # track index of safe reports
                            passes.append(i)
            # this test has now passed with the removal of a level, break to the next one
            else:
                break

    print(len(passes))

safety_test_dampener(file)

# ANSWER: 354 (varies with input file)


