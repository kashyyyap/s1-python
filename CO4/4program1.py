class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
l1 = int(input("Enter length 1: "))
b1 = int(input("Enter breadth 1: "))
r1 = Rectangle(l1, b1)

print("Area of rectangle 1:", r1.area())
print("Perimeter of rectangle 1:", r1.perimeter())
l2 = int(input("Enter length 2: "))
b2 = int(input("Enter breadth 2: "))
r2 = Rectangle(l2, b2)

print("Area of rectangle 2:", r2.area())
print("Perimeter of rectangle 2:", r2.perimeter())
a1 = r1.area()
a2 = r2.area()

if a1 > a2:
    print("Rectangle 1 has a larger area.")
elif a1 == a2:
    print("Both rectangles have equal area.")
else:
    print("Rectangle 2 has a larger area.")
