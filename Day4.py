import random

# print random integer value
random_integer = random.randint(1, 10)
print(random_integer)

# print random floa t value
random_float = random.random()
print(random_float)

# print random within range
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Head and tail program
coin_random = random.randint(0,1)
if (coin_random == 1):
    print("Heads")
else:
    print("Tails")    



