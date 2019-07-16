def process_reaction(my_input: str) -> str:
    """Returns string that has adjacent same characters of opposite cases removed """
    my_output = ''
    i = 0
    while i < (len(my_input)):
        if (i == (len(my_input) - 1)) or (my_input[i].swapcase() != my_input[i+1]):
            my_output += my_input[i]
        else:
            i += 1 
        i += 1
    return my_output

if __name__ == '__main__':

    with open('aoc05-input.txt', 'r') as my_file:
        my_string = ''
        for line in my_file:
            my_string = my_string + line.strip()
        my_old_string = ''

        while (len(my_old_string) != len(my_string)):
            my_old_string = my_string
            my_string = process_reaction(my_string)

    print("P A R T   0 1      O U T P U T :   " + str(len(my_string)))
