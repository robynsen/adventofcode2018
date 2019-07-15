import re

# Functions to support part 1
def get_claim_data(my_string: str):
    """Return a list containing the values given in string format #ID @ l,t: wxh"""
    # #4 @ 809,807: 24x16
    return re.findall(r'\d+', my_string)

def add_claim(my_string: str, my_claim_layers: list) -> list:
    """Add 1 to every cell in my_claim_layers covered the claim represented by my_string """
    my_params = get_claim_data(my_string)
    for i in range(int(my_params[1]), int(my_params[1]) + int(my_params[3])):
        for j in range(int(my_params[2]), int(my_params[2]) + int(my_params[4])):
            my_claim_layers[i][j] += 1
    return my_claim_layers

def get_num_duplicate_claims(my_claim_layers: list) -> int:
    my_count = 0
    for i in range(0, len(my_claim_layers)):
        for j in range(0, len(my_claim_layers[0])):
            if (my_claim_layers[i][j] > 1):
                my_count += 1
    return my_count

def solve_part1():
    print("     P A R T    0 1")
    # create a 2d grid filled where values will show number of claims on that coordinate 
    my_claim_layers = [x[:] for x in [[0] * 1000] * 1000]

    with open('aoc03-input.txt', 'r') as my_file:
        for line in my_file:
            my_claim_layers = add_claim(line, my_claim_layers)

    print("O U T P U T :   " + str(get_num_duplicate_claims(my_claim_layers)))

if __name__ == '__main__':

    solve_part1()