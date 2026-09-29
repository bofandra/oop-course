from models import Point


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point(1, 2)

print("p1:", p1)
print("p2:", p2)

print("p1 is p3:", p1 is p3)
print("p1 == p3:", p1 == p3)

print("p1 + p2:", p1 + p2)
