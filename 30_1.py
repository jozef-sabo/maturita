"""
Na Mars dopadne denne priemerne N meteoritov s rozptylom 1000 metrov od centra dopadu sledovanej oblasti.
V pásme od 10 do 99 metrov od centra sú rozmiestnené dôležité vedeckovýskumné zariadenia – vedecká zóna.
Vytvorte program, ktorý bude simulovať tento proces a umožní zistiť nasledovné:

- vypíše hodnoty vzdialeností dopadov meteoritov od centra, ktoré zasiahli vedeckú zónu za deň,
- zistí a vypíše ich počet,
- zistí a vypíše hodnotu pravdepodobnosti zásahu vedeckej zóny z priemerných hodnôt za 100 dní.

Simuláciu znázornite v programe tiež graficky.
"""
import math
import tkinter
import random

meteorites_count = int(input("Zadajte počet meteoritov: "))

window = tkinter.Tk()
canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

in_field_common = 0


def simulate(with_drawing: bool = False):
    global in_field_common
    in_field = 0

    if with_drawing:

        canvas.delete("all")
        canvas.create_oval(0, 0, 1000, 1000, outline="black")
        canvas.create_oval(450, 450, 550, 550, outline="black", fill="red")
        canvas.create_oval(490, 490, 510, 510, outline="black", fill="white")

    for _ in range(meteorites_count):
        angle = random.randint(0, 360)
        distance = random.randint(0, 500)
        if 10 <= distance <= 99:
            in_field += 1
            if with_drawing:
                print(distance, end=" ")

        x = (distance * math.cos(angle)) + 500
        y = (distance * math.sin(angle)) + 500
        if with_drawing:
            canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="silver")

    in_field_common += in_field
    if with_drawing:
        probability_local = in_field / meteorites_count * 100
        label.config(text=f"Počet v centre posledného dňa je {in_field}/{meteorites_count}. "
                          f"Pravdepodobnosť je {probability_local:.3f}%")


label = tkinter.Label()
label.pack()
for try_number in range(100):
    simulate(try_number == 99)

all_meteorites = meteorites_count * 100
probability = in_field_common / all_meteorites * 100
label.config(text=f"{label.cget('text')} Počet v centre celkovo {in_field_common}/{all_meteorites}. "
                  f"Pravdepodobnosť je {probability:.3f}%")

window.geometry("1000x1050")
window.mainloop()
