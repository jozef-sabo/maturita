import random

num_of_throws = int(input("Počet hodov: "))

rounds = []
for _ in range(num_of_throws):
    round_value = 0
    for _ in range(5):
        round_value += random.randint(1, 6)
    rounds.append(round_value)

winning_value = 0
for round_num in range(num_of_throws):
    if rounds[round_num] == rounds[-1]:
        winning_value += rounds[-1]

print(winning_value)
