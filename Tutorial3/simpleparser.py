ID = "9202204720082"    # input("Please enter your ID number:\n")

rev = ""
for r in range(11, -1, -1):
    rev = rev + ID[r]

sum = 0
for i in range(0, 12):
    if i % 2 == 0:
        sum = sum + ((int(rev[i]) * 2) % 9)
    else:
        sum = sum + int(rev[i])

isValid = (10 - (sum % 10)) == int(ID[12])
if isValid:
    day = ID[4:6]
    month = ID[2:4]
    year = ID[0:2]

    print("Your date of birth is {}/{}/{}.".format(day, month, year))

    gender = int(ID[6:10])
    if gender < 5000:
        print("You are female.")
    else:
        print("You are male.")

    isCitizen = ID[10]
    if isCitizen == '0':
        print("You are a South African citizen.")
    elif isCitizen == '1':
        print("You are a permanent resident.")
else:
    print("Invalid ID number.")
