#!/usr/bin/env python3
# Created by: Samuel Nkongolo
# Created on: Nov 4
# This program calculates and displays the power of 2 starting from 0 until this number.


def main():
    # This section deals with explaining the programs's function and defining variables.:)
    loop_count = 0
    print(
        "This program calculates and displays the power of 2 starting from 0 until this number."
    )
    num_pow = input("Enter a whole number: ")
    try:
        num_pow_int = int(num_pow)
        if num_pow_int < 0:
            print(f"{num_pow_int} is a negative number, enter a whole number. (e.g 5)")
        # This part gets every number within the range of 0-NumberGiven.
        for num in range(num_pow_int + 1):
            loop_count += 1
            print(f"{num}^2 = {num*num}. (Looped {loop_count} times)")
    except:
        print(f'"{num_pow}" is not a number, enter a whole number. (e.g 5)')

    try:
        num_pow_float = float(num_pow_int)
        if num_pow_float != num_pow_int:
            print(f"{num_pow_float} is a decimal number, enter a whole number. (e.g 5)")
    except:
        print("Error, restarting...\n")
        return main()


if __name__ == "__main__":
    main()
