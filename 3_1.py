"""
Vytvorte program, ktorý bude simulovať činnosť palubného počítača v električke takto:

- načíta zo súboru názov prvej zastávky do pamäte, vypíše na displej názov prvej zastávky,
- názov zastávky sa na displeji roluje sprava doľava, keď nejaká časť textu odíde z ľavej
  strany displeja, objaví sa na pravej strane,
- po stlačení ľubovoľnéh o  klávesu vypíše na displej názov ďalšej zastávky,
- ak sa na displeji vypisuje názov poslednej zastávky linky, tak sa k názvu zastávky vypíše aj
  upozornenie, že treba vystúpiť.
"""

import tkinter

with open("3_1.txt", "r", encoding="UTF-8") as file:
    tram_lines = file.read().splitlines()

tram_lines[0] += "  |  "
tram_lines[-1] += " - PROSÍME VYSTÚPTE!"

window = tkinter.Tk()
canvas = tkinter.Canvas(width=1400, height=300, bg="black")
canvas.pack()


def roll():
    tram_lines[position] = f"{tram_lines[position][1:]}{tram_lines[position][0]}"
    canvas.itemconfigure(stop_text, text=tram_lines[position])


def next_stop(event):
    global position
    position += 1
    if position >= stop_count:
        position -= 1
        return
    tram_lines[position] = f"{tram_lines[position]}  |  "
    canvas.itemconfigure(stop_text, text=tram_lines[position])


stop_count = len(tram_lines)
position = 0
stop_text = canvas.create_text(700, 150, text=tram_lines[position], fill="white", font="Arial 60")


def repeat():
    roll()
    canvas.after(250, repeat)
    canvas.bind_all("<Key>", next_stop)


repeat()
window.mainloop()
