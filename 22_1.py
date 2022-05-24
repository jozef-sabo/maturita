"""Známky žiakov z predmetu sú zapisované v textovom súbore známky.txt v tvare :

10 2 2 3 1 5 1 2 4 3 2
11 1 2 2 2 3 4 2 1 1 1 2

Prvé číslo znamená počet známok a potom nasledujú známky oddelené medzerou.
Riadok v súbore obsahuje známky jedného žiaka.
Vytvorte program, ktorý:
- umožní vypisovať údaje z tohto súboru tak, že na konci riadka vypíše priemernú známku,
podľa kritérií stanovených učiteľom sa však do priemeru nezapočíta jedna najhoršia známka,
- vytvorte nový textový súbor známky_novy.txt do ktorého zapíšete len počet známok
a známky bez najhoršej z nich. """

with open("22_1.txt", "r", encoding="UTF-8") as file:
    marks_lines = file.read().splitlines()

with open("22_1_1.txt", "w+", encoding="UTF-8") as file:
    for marks in marks_lines:
        marks_string = marks
        marks = [int(x) for x in marks.split()[1:]]
        marks_line_sum = 0
        marks_line_min = 0

        for mark in marks:
            if marks_line_min < mark:
                marks_line_min = mark

            marks_line_sum += mark

        marks_line_sum -= marks_line_min

        average_mark = marks_line_sum / (len(marks) - 1)
        print(f"{marks_string} {average_mark:.3f}")
        marks.remove(marks_line_min)

        marks = [str(x) for x in marks]
        file.write(f"{len(marks) + 1} {' '.join(marks)}\n")
