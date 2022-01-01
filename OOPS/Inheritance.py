class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def isMarried(self):
        print(f"{self.name} is not married")


class Male(User):
    def __init__(self, name, age):
        super().__init__(name, age, "M")

    def isMarried(self):
        super().isMarried()
        print(f'but {self.name} will marry at the age of 29.')


class Female(User):
    def __init__(self, name, age):
        super().__init__(name, age, "F")

    def isMarried(self):
        super().isMarried()
        print(f'There is no immediate plan of {self.name} to get married.')


ankit = Male("Ankit Bharti", 28)
garima = Female("Garima Sharma", 27)


for user in [ankit, garima]:
    print(f'{user.name} is {user.gender}.')
    user.isMarried()

