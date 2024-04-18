from first_package.first_class import Point as position

print(help(position))

point3 = position()
point4 = position()

point3.reset()
point4.move(5,6)

print(position.calculate_distance(point3,point4))

point3.move(17, 19)

print(point4.calculate_distance(point3))

print(point3.calculate_distance(point3))