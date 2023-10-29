class Car:
    def __init__(self):
        self.speed = 0
        self.color = ""
        self.name = ""
        self.is_police = False

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"\n{self.name} остановилась\n")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"\nТекущая скорость {self.name} - {self.speed} км/ч\n")

    def info(self):
        print(f"{self.name}")
        print(f"Цвет: {self.color}")
        print(f"Начальная скорость: {self.speed}\n")


class TownCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 60
        self.color = "черный"
        self.name = "Городская машина"

    def show_speed(self):
        super().show_speed()
        if self.speed > 80:
            print("! Превышение скорости !\n")


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 100
        self.color = "красный"
        self.name = "Спортивная машина"

    def show_speed(self):
        super().show_speed()
        if self.speed > 80:
            print("! Превышение скорости !\n")


class WorkCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 50
        self.color = "желтый"
        self.name = "Рабочая машина"

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("! Превышение скорости !\n")


class PoliceCar(Car):
    def __init__(self):
        super().__init__()
        self.speed = 90
        self.color = "синий"
        self.name = "Милицейская машина"
        self.is_police = True


def choice_car(cars):
    if not cars:
        print("Машин нет!")

    while True:
        print("\nВыберите машину для начала поездки:\n")

        for i in range(len(cars)):
            print("-------------")
            print(f"| Машина №{i + 1} |")
            print("-------------")
            cars[i].info()

        try:
            choice = int(input("Ваш выбор: "))
            if 1 <= choice <= len(cars):
                return choice
            else:
                print("Введите верное значение!")
        except ValueError:
            print("Введите верное значение!")


def choice_action():
    print("1. Прибавить скорость")
    print("2. Убавить скорость")
    print("3. Повернуть")
    print("4. Сменить машину")
    try:
        choice = int(input("Ваш выбор: "))
        if 1 <= choice <= 4:
            return choice
        else:
            print("Введите верное значение!")
    except ValueError:
        print("Введите верное значение!")


cars = []

town_car = TownCar()
cars.append(town_car)

sport_car = SportCar()
cars.append(sport_car)

work_car = WorkCar()
cars.append(work_car)

police_car = PoliceCar()
cars.append(police_car)

while True:
    index_choice_car = choice_car(cars)
    current_car = cars[index_choice_car - 1]

    print(f"Вы выбрали '{current_car.name}'!\n")
    current_car.go()
    current_car.show_speed()

    while True:
        choice = choice_action()

        if choice == 1:
            current_car.speed += 10
            current_car.show_speed()
        elif choice == 2:
            if current_car.speed == 10:
                current_car.stop()
            else:
                current_car.speed -= 10
                current_car.show_speed()
        elif choice == 3:
            direction = input("\nВведите направление: ")
            current_car.turn(direction)
            current_car.show_speed()
        else:
            current_car.stop()
            break
