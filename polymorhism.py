class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        print("Area of circle:", self.pi * self.radius * self.radius)

# Membuat objek dari kelas Circle
circle = Circle(5)
circle.calculate_area()
