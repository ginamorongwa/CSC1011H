min = int(input("Enter the minimum number of inches (not less than 0):\n"))
max = int(input("Enter the maximum number of inches (not greater than 11):\n"))

print('Inches: ', end='')
for v in range(min, max + 1):
    print('  {:2} '.format(v), end='')

print('\nMeters: ', end='')
for i in range(min, max + 1):
    meter = round(i / 39.37, 2)
    print('{:4} '.format(meter), end='')

