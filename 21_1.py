"""
V textovom súbore zoznam.txt sú zapísané údaje žiakov. Každý riadok textového súboru obsahuje meno priezvisko
a rodné číslo žiaka v tvare :

Milan Strelka 990809/0938
Eva Komarova 975406/0874

Vytvorte program, ktorý:
- prečíta a vypíše obsah textového súboru zoznam.txt,
- umožní vypísať mená dievčat a dátum ich narodenia v tvare DD.MM.RRRR.
- zapíše mená a rodné čísla chlapcov do nového súboru chlapci.txt
"""

with open("21_1.txt", "r", encoding="UTF-8") as file:
    people_lines = file.read().splitlines()

girls = []
boys = []

for person in people_lines:
    person = person.split()
    print(f"{person[1]} {person[0]}: {person[2]}")

    yy = int(person[2][:2])
    mm = int(person[2][2:4])
    dd = int(person[2][4:6])

    if mm > 50:
        year = 1900 + yy if yy > 22 else 2000 + yy
        girls.append(f"{person[1]} {person[0]}: {str(dd).zfill(2)}.{str(mm-50).zfill(2)}.{year}")
        continue

    boys.append(f"{person[1]} {person[0]}: {person[2]}\n")

with open("21_1_e.txt", "w", encoding="UTF-8") as file:
    file.writelines(boys)

print()
print("\n".join(girls))
