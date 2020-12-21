
if __name__ == "__main__":
    print("Hello World!")

    code = input("Please enter the animal identity codes. (Press return when done.)\nAnimal no. 1:\n")
    codes = []
    locations = {}
    number = 2

    while code != "":
        codes.append(code)
        code = input("Animal no. {}:\n".format(number))
        number = number + 1

    command = input("Commands: print, log <animal id> <x ord> <y ord>, quit.\n>")
    while command != 'quit':

        command_items = command.split(" ")
        if command_items[0] == "print":
            for code in codes:
                if code in locations:
                    location = locations[code]
                    print("Animal {} last seen at {}.".format(code, location))
                else:
                    print("Animal {} cannot be located.".format(code))
        elif command_items[0] == "log":
            locations[command_items[1]] = (int(command_items[2]), int(command_items[3]))
        else:
            print("Could not interpret command.")

        command = input("Commands: print, log <animal id> <x ord> <y ord>, quit.\n>")


