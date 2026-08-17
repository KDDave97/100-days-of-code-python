class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)

data1 = [user_1.id, user_1.username, user_1.followers, user_1.following]
data2 = [user_2.id, user_2.username, user_2.followers, user_2.following]

print(data1)
print(data2)