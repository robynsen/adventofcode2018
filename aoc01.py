import re

def do_part1(my_input):
    print("     P A R T    0 1")
    print("I N I T I A L   V A L U E :   "+str(my_input))
    my_output = 0
    with open('aoc01-input.txt', 'r') as my_file:
        for line in my_file:
            my_output += int(line)
    print("              O U T P U T :   "+ str(my_output))

def do_part2(my_input):
    print("     P A R T    0 2")
    print("I N I T I A L   V A L U E :   "+str(my_input))
    my_freq_history = {my_input}
    my_freq = 0
    is_found = False

    with open('aoc01-input.txt', 'r') as my_file:
        my_lines = my_file.readlines()

        i = 0
        while (i < len(my_lines)) and not is_found:
            my_freq += int(my_lines[i])
            if my_freq in my_freq_history:
                # do something
                my_output = my_freq
                is_found = True
            else:
                my_freq_history.add(my_freq)
            i = i + 1
            if i == len(my_lines) and not is_found:
                i = 0

    print("              O U T P U T :   "+ str(my_output))

my_input = 0
do_part1(my_input)

do_part2(my_input)