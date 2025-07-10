class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Метод для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height

    # Метод для нахождения периметра прямоугольника
    def perimeter(self):
        return 2 * (self.width + self.height)

    # Метод для проверки, является ли прямоугольник квадратом
    def is_square(self):
        return self.width == self.height

