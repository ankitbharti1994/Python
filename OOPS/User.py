class User:
    """Create a user by giving id & name"""
    def __init__(self, user_id, name, followers=0, followings=0):
        self.id = user_id
        self.name = name
        self.followers = followers
        self.followings = followings
        print("new user created...")

    def follow(self, user):
        user.followers += 1
        self.followings += 1


user_1 = User(user_id=1, name="Ankit Bharti")
print(user_1.__doc__)

user_2 = User(user_id=2, name="Binit Bharti")
user_1.follow(user_2)

print(user_1.followers)
print(user_1.followings)
print(user_2.followers)
print(user_2.followings)
