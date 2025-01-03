import os

# path to input file
file = open(fr"{os.getcwd()}\updates.txt")

def verify_updates(file):
    # placeholder for adding up all the median pages
    median_sum = 0

    # read the file
    printing_instructions = file.read()

    # split by newlines to separate rules from updates
    split_instructions = printing_instructions.split('\n\n')
    # split by newline to separate rules and pipes to separate pages in a rule
    # (using sets and tuples for efficiency because these should not be changed, and duplicate rules are unwanted)
    rules = set(tuple(rule.split('|')) for rule in split_instructions[0].split('\n'))
    # split by newlines to separate updates and commas to separate pages in an update
    # (using tuples for efficiency because these should not be changed)
    updates = tuple(tuple(update.split(',')) for update in split_instructions[1].split('\n'))

    # create a set of keys for rules for faster lookup
    rule_keys = set(rule[0] for rule in rules)

    # iterate through updates
    for update in updates:
        # iterate through page numbers in an update
        for i, page in enumerate(update):
            # skip first page, it can be anything
            if i > 0:
                # check if any rules exist for this page
                if page in rule_keys:
                    # get which pages must come after this page according to applicable rules
                    rule_values = set(rule[1] for rule in rules if rule[0] == page)
                    # filter out rule values that compare pages that aren't even in the update
                    applicable_rule_values = rule_values.intersection(set(update))
                    # get which pages came before this page in the update
                    prev_pages = update[0:i]

                    # check if any of the previous pages are restricted according to the rule values
                    if len(set(prev_pages).intersection(applicable_rule_values)) > 0:
                        # this update is invalid, skip to the next one
                        break
                    elif i == len(update) - 1:
                        # this update is valid, add it's median page number
                        median_sum += int(update[len(update) // 2])

    print(median_sum)

verify_updates(file)

# https://adventofcode.com/2024/day/5
# ANSWER: 5391 (varies with input file)


