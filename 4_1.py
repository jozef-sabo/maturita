"""
Vytvorte program, ktorý zo vstupného súboru krizovka.txt vykreslí krížovku.
V textovom súbore jeden riadok popisuje jeden riadok krížovky. Na začiatku riadku je číslo, ktoré určuje,
ktorý zo znakov tvorí tajničku.
Napríklad '3 KOPÍRKA' znamená, že v krížovke je riadok s textom KOPÍRKA' a tretí znak tohto textu je súčasťou tajničky.


Vlastnosti programu:
- prečíta obsah textového súboru a vypíše text tajničky,
- vykreslí krížovku so zadanou veľkosťou štvorčekov, krížovka je vykreslená tak, že
  štvorčeky tajničky sú podfarbené a sú umiestnené v jednom  stĺpci,
- vykreslí vyplnenú krížovku.
"""
import tkinter

square_width = int(input("Zadajte šírku štvorčeka (px): "))

with open("4_1.txt", "r", encoding="UTF-8") as file:
    crossword_lines = file.read().splitlines()

crossword = ""
offset_by = 0
for line_num in range(len(crossword_lines)):
    crossword_lines[line_num] = crossword_lines[line_num].split()
    crossword_lines[line_num][0] = int(crossword_lines[line_num][0])
    crossword += crossword_lines[line_num][1][crossword_lines[line_num][0] - 1]

    if crossword_lines[line_num][0] > offset_by:
        offset_by = crossword_lines[line_num][0]

window = tkinter.Tk()
canvas = tkinter.Canvas(window, width=800, height=800)
canvas.pack()

for line_num in range(len(crossword_lines)):
    offset = crossword_lines[line_num][0]
    word = crossword_lines[line_num][1]
    position = offset_by - offset
    for char_ord in range(len(word)):
        x_beginning = position * square_width
        x_end = (position+1)*square_width
        y_beginning = line_num * square_width
        y_end = (line_num+1) * square_width
        color = "gray" if char_ord == (offset-1) else "silver"
        font = f"Arial {square_width//2} bold" if char_ord == (offset-1) else f"Arial {square_width//2}"
        canvas.create_rectangle(x_beginning, y_beginning, x_end, y_end, fill=color, outline="black")
        canvas.create_text((x_beginning+x_end) / 2, (y_beginning+y_end) / 2, text=word[char_ord], font=font)
        position += 1


print(crossword)

window.geometry("800x800")
window.mainloop()
