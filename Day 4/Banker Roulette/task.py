import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_friend = random.randint(0, len(friends) -1)
print(friends[random_friend])
print("-----------------")
print(random.choice(friends))