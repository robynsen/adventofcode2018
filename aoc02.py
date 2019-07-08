def has_n_char(my_string: str, my_n: int) -> bool:
    my_result = False
    my_char = 'a'
    for i in range(0,26):
        if my_string.count(my_char) == my_n:
            my_result = True            
        my_char = chr(ord(my_char) + 1)
    return my_result

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

solve_part1()