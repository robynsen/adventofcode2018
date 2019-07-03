import re

def show_evaluation(my_input):
    print("  I N P U T :   "+str(my_input))
    my_output = 0
    with open('aoc01-input.txt', 'r') as my_file:
        for line in my_file:
            my_output += int(line)
    print("O U T P U T :   "+ str(my_output))

my_input = 0
show_evaluation(my_input)
