class Person:
    # Методы экземпляра
    def __init__(self, surname, name, age, height):
        self.surname = surname
        self.name = name
        self.age = age
        self.height = height

    def get_age(self):
        return self.age

    def print_info(self):
        print(f"\nФамилия: {self.surname}")
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Рост: {self.height}")

    # Статические методы

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def correct_age(age):
        try:
            if 1 <= age <= 120:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def correct_height(age):
        try:
            if 50 <= age <= 240:
                return True
            else:
                return False
        except ValueError:
            return False

    # Метод класса

    @classmethod
    def from_string(cls, info_str):
        last_name, first_name, age, height = info_str.split()
        return cls(last_name, first_name, age, height)


person1 = Person("Андреенко", "Павел", 18, 175)  # Метод экземпляра
person1.print_info()  # Метод экземпляра

if Person.is_adult(person1.get_age()):  # Статический метод
    print("Совершеннолетний(ая)")
else:
    print("Несовершеннолетний(ая)")

while True:
    info_str = input("\nВведите данные о человеке через пробел в формате 'ФАМИЛИЯ ИМЯ ВОЗРАСТ РОСТ': ")

    info = info_str.split()

    if len(info) == 4:
        if not Person.correct_age(int(info[2])):  # Статический метод
            print("Введите корректное значение возраста!")
        elif not Person.correct_height(int(info[3])):  # Статический метод
            print("Введите корректное значение роста!")
        else:
            person2 = Person.from_string(info_str)  # Метод класса
            person2.print_info()  # Метод экземпляра
    else:
        print("Данные введены неверно!")
