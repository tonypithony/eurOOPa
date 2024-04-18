from first_class import Point

point1 = Point()
point2 = Point()

point1.reset()
point2.move(4,3)

print(Point.calculate_distance(point1,point2))
print(point1.calculate_distance(point2) == point2.calculate_distance(point1))

print(help(Point))
print(help(Point.calculate_distance))