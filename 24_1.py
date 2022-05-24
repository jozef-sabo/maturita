"""
Vstupom do zemskej atmosféry došlo k rozpadu meteoritu na N menších častí, ktoré dopadli na zemský povrch
a náhodne zasiahli jeho časť o rozmeroch 80 x 80 m. Na tejto ploche sa nachádza malé ihrisko s plochou 40 x 20 m.
Vytvorte program pomocou ktorého budete simulovať tento jav.
Simuláciu znázornite v programe tiež graficky.
Vstupná hodnota je tvorená počtom pokusov (počet meteoritov) PP a počtom častí N na ktoré sa meteorit rozpadol.
Zistite počet úlomkov, ktoré dopadli na plochu ihriska a pravdepodobnosť zasiahnutia tohto ihriska.
"""
import tkinter
import random

try_count = int(input("Zadajte počet pokusov: "))
parts_count = int(input("Zadajte počet častí: "))

window = tkinter.Tk()
canvas = tkinter.Canvas(width=800, height=800)
canvas.pack()


def simulate():
    global try_count
    in_field = 0
    if try_count <= 0:
        return
    try_count -= 1
    canvas.delete("all")
    canvas.create_rectangle(200, 300, 600, 500, outline="red")
    canvas.create_rectangle(0, 0, 800, 800, outline="black")
    for _ in range(parts_count):
        x = random.randint(0, 800)
        y = random.randint(0, 800)
        if (200 < x < 600) and (300 < y < 500):
            in_field += 1
        canvas.create_oval(x-2, y-2, x+2, y+2, fill="silver")
    probability = in_field / parts_count * 100
    label.config(text=f"Počet zostávajúcich pokusov: {try_count}, počet kúskov v ihrisku {in_field}/{parts_count}, "
                      f"pravdepodobnosť: {probability:.3f}%")


button = tkinter.Button(window, text="Simuluj ďalej", command=simulate)
button.pack()
label = tkinter.Label()
label.pack()
simulate()

window.geometry("800x850")
window.mainloop()
