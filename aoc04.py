import re
import os

def is_new_guard(my_string: str) -> bool:
    return re.search(r'begins shift', my_string)

def get_guard_id(my_string: str) -> int:
    """Returns True if this input string is a notification of a new guard beginning a shift"""
    my_result = re.findall("\#(\d+) begins shift", my_string)
    return int(my_result[0])

def is_sleep_min(my_string: str) -> bool:
    """Returns True if this input string is a notification of a guard falling asleep """
    return re.search(r'falls asleep', my_string)

def is_wake_min(my_string: str) -> bool:
    """Returns True if this input string is a notification of a guard waking up"""
    return re.search(r'wakes up', my_string)

def get_min(my_string: str) -> int:
    """Returns the minute value in the timestamp on this notification string """
    my_result = re.findall("\:(\d+)\]", my_string)
    return int(my_result[0])

def get_sleepiest_guard_id(my_sleep_tally: dict) -> int:
    """Return the ID of the guard with the max cumulative minutes spent asleep """
    my_result = 0
    max_mins_asleep = 0
    this_mins_asleep = 0
    for my_key in my_sleep_tally:
        this_mins_asleep = sum(my_sleep_tally[my_key])
        if this_mins_asleep > max_mins_asleep:
            max_mins_asleep = this_mins_asleep
            my_result = int(my_key)
    return my_result

def get_sleepiest_min(my_sleep_tally: dict, my_guard_id: int) -> int:
    """Return the minute (as an int) that this guard slept most frequently """
    my_result = 0
    max_times_asleep = 0
    for i in range(0, len(my_sleep_tally[my_guard_id])):
        if my_sleep_tally[my_guard_id][i] > max_times_asleep:
            max_times_asleep = my_sleep_tally[my_guard_id][i]
            my_result = i
    return my_result

if __name__ == '__main__':

    with open('aoc04-input.txt', 'r') as my_file:
        my_id = 0
        my_sleep_min = 0
        my_wake_min = 0
        my_sleep_tally = {}
        for line in sorted(my_file):
            if is_new_guard(line):
                my_id = get_guard_id(line)
            elif is_sleep_min(line):
                my_sleep_min = get_min(line)
            elif is_wake_min(line):
                my_wake_min = get_min(line)

                if my_id not in my_sleep_tally:
                    my_sleep_tally[my_id] = [0 for i in range(0, 60)]

                for i in range(my_sleep_min, my_wake_min):
                    my_sleep_tally[my_id][i] += 1

    my_id = get_sleepiest_guard_id(my_sleep_tally)
    my_sleepiest_min = get_sleepiest_min(my_sleep_tally, my_id)

    print("P A R T   0 1      O U T P U T :   " + str(my_id * my_sleepiest_min))
