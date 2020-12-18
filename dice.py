# Created by Ryan Nguyen
# Created on December 2020
# This program runs a dice rolling simulation

import random


def main():
    # This function runs a dice rolling simulation

    times_counter = 0
    loop_counter = 0
    total_rolls = 0
    doubles = True

    # input
    trial_counter_as_string = input("Enter trial count: ")

    # integer + positive check
    try:
        trial_counter_as_number = int(trial_counter_as_string)
        if trial_counter_as_number > 0:

            # loops trials
            for loop_counter in range(trial_counter_as_number):
                doubles = False

                # trial sequence
                while doubles is False:
                    rand1 = random.randint(1, 6)
                    rand2 = random.randint(1, 6)
                    times_counter = times_counter + 1
                    print("{}, {}".format(rand1, rand2))

                    # if doubles are rolled
                    if rand1 == rand2:
                        doubles = True
                        print("It took {} rolls to get doubles".format
                              (times_counter))
                        total_rolls = total_rolls + times_counter
                        times_counter = 0

            # final calculation and output
            percentage = trial_counter_as_number/total_rolls * 100
            print("The chance of rolling doubles is a {}% chance".format
                  (percentage))
        else:
            print("Integer must be positive")
    except Exception:
        print("Invalid integer")


if __name__ == "__main__":
    main()
