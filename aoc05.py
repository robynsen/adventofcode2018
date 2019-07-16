if __name__ == '__main__':

    with open('aoc05-input.txt', 'r') as my_file:
        my_string = ''
        for line in my_file:
            my_string = my_string + line.strip()
        my_old_string = ''

        while (len(my_old_string) != len(my_string)):
            my_old_string = my_string
            my_string = ''
            i = 0
            while i < (len(my_old_string)):
                if (i == (len(my_old_string) - 1)) or (my_old_string[i].swapcase() != my_old_string[i+1]):
                    my_string = my_string + my_old_string[i]
                else:
                    i += 1 
                i += 1

    print("P A R T   0 1      O U T P U T :   " + str(len(my_string)))
