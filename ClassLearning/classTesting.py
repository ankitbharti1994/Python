class Person:
    '''A simple person model'''

    def __init__(self, personName):
        self.name = personName
        self.age = 25
        self.friends = []

    def greeting(self):
        print(f'hello {self.name}')

    def addFriends(self, friend):
        self.friends.append(friend)


person = Person('ankit kumar bharti')
person.addFriends('rohit')
print(person.name, person.age, person.friends)
person.greeting()
print(person.__doc__)


person2 = Person('rohit shrivastva')
person2.addFriends('kailash')
person2.addFriends('garima')
person2.age = 26
print(person2.name, person2.age, person2.friends)

print(person.__class__)
