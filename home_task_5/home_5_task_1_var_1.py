import random

number = random.randint(1, 100)
print(number, end=' - ')
if number % 2 == 0:
    print(f"чётное число")
else:
    print(f"нечётное число")
