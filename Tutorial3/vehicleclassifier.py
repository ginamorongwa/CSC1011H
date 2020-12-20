gvm = int(input("What is the gross vehicle mass (in kg)?\n"))
_class = ""

if gvm <= 3500:
    _class = 'B'
elif 3500 < gvm <= 16000:
    _class = 'C1'
else:
    _class = 'C'

hasTrailer = input("Does the vehicle have a trailer?\n")

if hasTrailer == 'y':
    gvm = int(input("What is the gross vehicle mass of the trailer (in kg)?\n"))
    if gvm > 750:
        print("This vehicle is class E{}.".format(_class))
    else:
        print("This vehicle is class {}.".format(_class))
else:
    isArticulated = input("Is the vehicle articulated?\n")
    if isArticulated == 'y':
        print("This vehicle is class E{}.".format(_class))
    else:
        print("This vehicle is class {}.".format(_class))
