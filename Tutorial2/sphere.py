import math

center = input("Enter coordinate of centre:\n")
center = center[1:-1]
center_coordinates = center.split(", ")
x1 = float(center_coordinates[0])
y1 = float(center_coordinates[1])
z1 = float(center_coordinates[2])

surface = input("Enter a surface coordinate:\n")
surface = surface[1:-1]
surface_coordinates = surface.split(", ")
x2 = float(surface_coordinates[0])
y2 = float(surface_coordinates[1])
z2 = float(surface_coordinates[2])
# print(surface_coordinates)
print("{} {} {}".format(x2, y2, z2))

radius = math.sqrt(math.pow((x1 - x2), 2) + math.pow((y1 - y2), 2) + math.pow((z1 - z2), 2))
pi = math.pi
volume = (4 / 3) * pi * math.pow(radius, 3)

print("The radius is: {}.\nThe volume is: {}.".format(round(radius, 3), round(volume, 3)))
