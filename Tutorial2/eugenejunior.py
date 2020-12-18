import sys
import math

print("Hello, I am Eugene Junior.")

name = input("What is your first name?\n")
surname = input("What is your last name?\n")

print("Hi {}.{}.!".format(name[0].upper(), surname[0].upper()))

year = int(input("What year is this?\n"))
age = int(input("What age are you?\n"))

year_born = year - age
print("Okay, so you were born in {}/{}.".format(year_born-1, str(year_born)[2:]))

height = float(input("How tall are you (metres)?\n"))

feet = height * 3.281
inches = math.floor((feet - math.floor(feet)) * 12)
feet = math.floor(feet)

print("That\'s {}'{}\"!".format(feet, inches))
print("I'm going to tell you your Star Wars name.")

mother = input("What's your mother's first name?\n")
city = input("What's the name of the city nearest to your place of birth?\n")

star_wars_name = surname[:3] + name[:2]
star_wars_surname = mother[-2:] + city[-3:]

print("Your Star Wars name is {} {}.".format(star_wars_name, star_wars_surname))