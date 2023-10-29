class Door:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height


class Room:
    def __init__(self):
        while True:
            self.doors = []
            self.windows = []

            self.length = float(input("Введите длину комнаты: "))
            self.width = float(input("Введите ширину комнаты: "))
            self.height = float(input("Введите высоту комнаты: "))

            if self.length <= 0 or self.width <= 0 or self.height <= 0:
                print("Длина, ширина и высота комнаты должны быть положительными значениями")
            else:
                break

        self.square = 2 * self.height * (self.length + self.width)

        while True:
            self.num_doors = int(input("Введите количество дверей: "))
            if self.num_doors < 1:
                print("Количество дверей не может быть меньше 1")
            else:
                break

        for i in range(self.num_doors):
            while True:
                width = float(input(f"Введите ширину двери {i + 1}: "))
                height = float(input(f"Введите высоту двери {i + 1}: "))
                if width <= 0 or height <= 0:
                    print("Ширина и высота двери должны быть положительными значениями")
                else:
                    self.doors.append(Door(width, height))
                    break

        while True:
            self.num_windows = int(input("Введите количество окон: "))
            if self.num_windows < 1:
                print("Количество дверей не может быть меньше 1")
            else:
                break

        for i in range(self.num_windows):
            while True:
                width = float(input(f"Введите ширину окна {i + 1}: "))
                height = float(input(f"Введите высоту окна {i + 1}: "))
                if width <= 0 or height <= 0:
                    print("Ширина и высота окна должны быть положительными значениями")
                else:
                    self.windows.append(Window(width, height))
                    break

    def calculate(self):
        square = self.square
        for i in range(self.num_doors):
            square -= self.doors[i].square()
        for i in range(self.num_windows):
            square -= self.windows[i].square()
        return square


room = Room()
print(f"Общая площадь комнаты: {room.square}")
print(f"Площадь после вычета окон и дверей: {room.calculate()}")
