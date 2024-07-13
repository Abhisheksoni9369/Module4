class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width


length = 5
width = 4


rectangle = Rectangle(length, width)


area = rectangle.calculate_area()


print(f"The area of the rectangle with length {length} and width {width} is: {area}")
