min = int(input("Enter the minimum number of feet (not less than 0):\n"))
max = int(input("Enter the maximum number of feet (not more than 99):\n"))

for i in range(min, max + 1):
    meter = round(i / 3.281, 2)
    print("  {:2}' |   {}m".format(i, meter))
