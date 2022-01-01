from classTesting import Person as P


class User(P):
    """Inherited from person"""

    def __init__(self, name, address):
        super().__init__(name)
        self.name = name
        self.address = address


user = User('ankit bharti', 'Mumbai')
print(user.name, user.address)
print(user.greeting())
print(isinstance(user, P))
print(issubclass(User, P))


class Employee(User):
    """Multiple inheritance"""

    def greeting(self):
        print(f'Hello {self.name} for staying at {self.address}.')

    def superGreeting(self):
        super().greeting()


employee = Employee('ankit', 'mumbai')
employee.greeting()
employee.superGreeting()


class A:
    """class A which is base class"""

    def __init__(self, num):
        self.number = 0
        self.__result(num)

    def increaseBy2(self, num):
        self.number = num + 2

    __result = increaseBy2


class B(A):
    def increaseBy2(self, num1, num2):
        return num1 + num2


val = A(2)
print(val.number)

val1 = B(5)
print(val1.number)
print(val1.increaseBy2(5, 6))
print(val.number)


class Rohit:
    pass


rohit = Rohit()
rohit.name = 'rohit'
rohit.age = 26

print(rohit.name, rohit.age)
