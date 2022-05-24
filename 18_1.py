with open("18_1_2.txt", "r", encoding="UTF-8") as file:
    voted_lines = file.read().splitlines()
with open("18_1_inp.txt", "r", encoding="UTF-8") as file:
    out = file.read().splitlines()

print(f"Počet hlasov: {len(voted_lines)}")

votes = {}
for vote in voted_lines:
    if vote not in votes:
        votes[vote] = 1
        continue
    votes[vote] += 1

lowest_score = 10e10
lowest_score_in_game = 10e10
lowest_player = ""
lowest_player_in_game = ""
for key in votes.keys():
    print(f"{key} - {votes[key]}", end="\t")
    if votes[key] < lowest_score:
        lowest_player = key
        lowest_score = votes[key]

    if votes[key] < lowest_score_in_game and key not in out:
        lowest_player_in_game = key
        lowest_score_in_game = votes[key]

print()
print(f"Hráč s najnižśim skóre: {lowest_player}")
print(f"Hráč s najnižśim skóre v hre: {lowest_player_in_game}")
