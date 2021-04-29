#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: April 2021
# This program adds two numbers that were given by the user


def main():
    # This adds two numbers together
    print("This program adds 2 numbers together.")
    print("")

    # Input
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    # Process
    answer = first_number + second_number

    # Output
    print("")
    print("{0} + {1} = {2}".format(first_number, second_number, answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
