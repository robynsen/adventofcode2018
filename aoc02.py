# Functions to support part 1
def has_n_char(my_string: str, my_n: int) -> bool:
    my_result = False
    my_char = 'a'
    for i in range(0,26):
        if my_string.count(my_char) == my_n:
            my_result = True            
        my_char = chr(ord(my_char) + 1)
    return my_result

# Functions to support Part 2
def differs_by_one(my_string1: str, my_string2: str) -> bool:
    num_diffs = 0
    if len(my_string1) == len(my_string2):
        for a, b in zip(my_string1, my_string2):
            if a != b:
                num_diffs += 1
    return (num_diffs == 1)

def get_common_letters(my_string1: str, my_string2: str) -> str:
    my_output = ''
    if len(my_string1) == len(my_string2):
        for a, b in zip(my_string1, my_string2):
            if a == b:
                my_output = my_output + a
    return my_output

def solve_part1():
    print("     P A R T    0 1")

    num_doubles = 0
    num_triples = 0
    with open('aoc02-input.txt', 'r') as my_file:
        for line in my_file:
            if has_n_char(line, 2):
                num_doubles = num_doubles + 1
            if has_n_char(line, 3):
                num_triples = num_triples + 1
    my_output = num_doubles * num_triples            
    print("O U T P U T :   "+ str(my_output))

def solve_part2():
    print("     P A R T    0 2")
    is_found = False
    my_output = ''

    with open('aoc02-input.txt', 'r') as my_file:
        my_lines = my_file.readlines()

        i = 0
        while (i < len(my_lines)) and not is_found:
            j = i + 1
            while (j < len(my_lines)) and not is_found:
                # do stuff
                if differs_by_one(my_lines[i], my_lines[j]):
                    my_output = get_common_letters(my_lines[i], my_lines[j])
                    is_found = True
                j = j + 1
            i = i + 1
    print("O U T P U T :   "+ str(my_output))        

if __name__ == '__main__':
    solve_part1()

    solve_part2()
