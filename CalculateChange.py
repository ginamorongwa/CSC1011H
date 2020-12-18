import sys
import math

# get the amount from input
amount = int(input("Enter change amount:\n"))

# get the number of R5's
five = math.floor(amount / 5)

# get the remaining amount
amount = amount - 5 * five

if five != 0:
    print("The change:\n{} R5 coins".format(five))

if amount != 0:
    two = math.floor(amount / 2)
    amount = amount - 2 * two

    if two != 0:
        print("{} R2 coins".format(two))

    if amount != 0:
        print("1 R1 coins")
