# Create a shape class, and sub-classes which represent different geometric
# shapes, such as rectangles, circles and triangles. Give these classes 
# methods to perform standard geometric calculations such as finding the 
# area and perimeter of a shape.

class Shape():
    def __init__(self, name):
        self.name = name

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

class Circle(Shape):
    def __init__(self, rad):
        self.rad = rad

class Triangle(Shape):
    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3