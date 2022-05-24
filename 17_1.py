import random

n = 500
interval_from = 0
interval_to = 500

numbers = []

if interval_from > interval_to:
    interval_to, interval_from = interval_from, interval_to

for _ in range(n):
    random_number = random.randint(interval_from, interval_to)
    numbers.append(str(random_number))

print(" ".join(numbers))

with open("17_1_e.txt", "w+", encoding="UTF-8") as file:
    for random_number in numbers:
        if random_number == random_number[::-1]:
            file.write(f"{random_number} ")
            print(random_number, end=" ")
    print()

with open("17_1_e.txt", "r", encoding="UTF-8") as file:
    print(file.read())

