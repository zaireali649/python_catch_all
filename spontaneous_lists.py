import random

likes = []

print(likes)

likes.append("pokemans")
likes.append("lambdas")
likes.append("s. cats")
likes.append("his seeds")
likes.append("work")
likes.append("python")

print(likes)

print(random.sample(likes, len(likes)))

likes.sort()

print(likes)

for like in likes:
    print(like)
