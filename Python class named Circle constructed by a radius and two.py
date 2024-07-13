import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


radius = 5


circle = Circle(radius)


area = circle.calculate_area()
perimeter = circle.calculate_perimeter()


print(f"The area of the circle with radius {radius} is: {area:.2f}")
print(f"The perimeter of the circle with radius {radius} is: {perimeter:.2f}")
