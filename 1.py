class Example:
    static_var1 = 10
    static_var2 = 20

    def __init__(self, dynamic_var1, dynamic_var2):
        self.dynamic_var1 = dynamic_var1
        self.dynamic_var2 = dynamic_var2

    def method1(self):
        self.new_var = 5
        print(f"Метод 1: {self.new_var}")

    @classmethod
    def method2(cls):
        return Example.static_var1 + Example.static_var2

    def method3(self):
        return self.dynamic_var1 ** self.dynamic_var2


x = int(input("Введите переменную x: "))
y = int(input("Введите переменную y: "))

obj = Example(x, y)

obj.method1()
print(f"Метод 2: {Example.method2()}")
print(f"Метод 3: {obj.method3()}")
