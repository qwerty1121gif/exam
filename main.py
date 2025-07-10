from rectangle import Rectangle

def main():
    while True:
        try:
            input_width = float(input("Введите ширину прямоугольника: "))
            input_height = float(input("Введите высоту прямоугольника: "))
            
            if input_width <= 0 or input_height <= 0:
                raise ValueError("Ширина и высота должны быть положительными числами.")
            break  
        except ValueError as e:
            print(e)

    rect = Rectangle(input_width, input_height)

    print(f"Площадь прямоугольника: {rect.area():.2f}")
    print(f"Периметр прямоугольника: {rect.perimeter():.2f}")

    if rect.is_square():
        print("Это квадрат.")
    else:
        print("Это не квадрат.")


if __name__ == "__main__":
    main()