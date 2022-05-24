with open("16_1.txt", "r", encoding="UTF-8") as file:
    text = file.read()
print(text)

analyse = {}

for character in text:
    if character not in analyse.keys():
        analyse[character] = 1
        continue

    analyse[character] += 1

print()
user_char = input("Zadajte znak na skúmanie: ")[0]
if user_char in analyse.keys():
    print(analyse[user_char])
else:
    print(0)

for character in analyse.keys():
    if ("A" <= character <= "Z") or ("a" <= character <= "z"):
        print(f"{character} - {analyse[character]}", end=",\t")
