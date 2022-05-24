"""
V textovom súbore zasadaci_poriadok.csv je abecedne zoradený zoznam žiakov triedy. Na každom riadku je
meno jedného žiaka v tvare priezvisko;meno. Ukážka textového súboru:

Bajčičák;Roman
Barancová;Tatiana
Bištiak;Michal
Borový;Oliver
Brezoňák;Ján
Čepčárová;Simona

Vytvorte program, ktorý, po vložení vstupných hodnôt počet radov a počet lavíc v rade umožní nasledovné:
- prečíta z textového súboru a zapamätá si všetkých študentov,
- ak používateľ zadal nedostatočný počet lavíc pre všetkých študentov, program nás na to upozorní vypísaním textu,
- ak sa všetci študenti zmestia do lavíc, program vypíše náhodný zasadací poriadok.
"""

import random
import tkinter
import math

window = tkinter.Tk()
window_width = 1200
window_height = 650

with open("11_1.csv", "r", encoding="UTF-8") as file:
    students_list = file.read().splitlines()


def show():
    tables_number = int(entry_tables.get())
    columns = int(entry_rows.get())
    rows = math.ceil(tables_number / columns)

    rect_width = window_width // columns
    rect_height = window_height // rows

    if tables_number < len(students_list):
        print("Počet lavíc je menší ako počet žiakov.")
        return

    canvas.delete("all")
    random.shuffle(students_list)
    for student_num in range(len(students_list)):
        student_name = students_list[student_num].split(";")
        student_name = f"{student_name[1]} {student_name[0]}"
        rect_x_beginning = (student_num % columns) * rect_width
        rect_y_beginning = (student_num // columns) * rect_height
        rect_x_end = ((student_num % columns) + 1) * rect_width
        rect_y_end = ((student_num // columns) + 1) * rect_height

        canvas.create_rectangle(rect_x_beginning, rect_y_beginning, rect_x_end, rect_y_end, fill="silver",
                                outline="black")
        canvas.create_text((rect_x_beginning + rect_x_end) // 2, (rect_y_beginning + rect_y_end) // 2, anchor="center",
                           text=student_name)
    canvas.delete()


label_tables = tkinter.Label(window, text='Počet lavíc')
entry_tables = tkinter.Entry(window)
label_rows = tkinter.Label(window, text='Počet radov')
label_tables.pack()
entry_tables.pack()
label_rows.pack()
entry_rows = tkinter.Entry(window)

entry_rows.pack()
button = tkinter.Button(window, text='Enter', command=show)
button.pack()
canvas = tkinter.Canvas(window, width=window_width, height=window_height)
canvas.pack()

window.geometry(f"{window_width}x{window_height+100}")
window.mainloop()
