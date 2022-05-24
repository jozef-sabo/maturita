"""
Vytvorte program, ktorý bude šifrovať text zapísaný v textovom súbore sifrovat_text.txt nasledovným spôsobom:
Na vstupe načíta šifrovací kľúč. Kľúčom je slovo zložené z malých písmen bez diakritiky.
Zo súboru číta riadky textu, zašifruje ich a zapíše do nového textového súboru zasifrovany_text.txt.

Riadky textu obsahujú len malé písmená abecedy (bez diakritiky).
Každý znak zašifruje posunom v malej abecede, pričom veľkosť posunu je daná kľúčom (príslušným písmenom z kľúča).
Napríklad písmeno b v kľúči znamená, že vstupný znak posunieme v abecede o pozíciu b, teda o 2 znaky. Nasledujúci
znak zašifruje posunom nasledujúceho znaku v kľúči.
V prípade, že posun je za posledné písmeno abecedy, posunie ho na prvé písmená v abecede (podľa daného posunu).

Riadok textu: dnes maturujeme v pythone
Kľúč: abc
Posun: 1231231231231231231231231
Zašifrovaný riadok: epht pbvxswmfoh x qawiqqf
"""

key = "abc"
key.lower()
key = [ord(x) - 96 for x in key]
key_length = len(key)

with open("12_1.txt", "r", encoding="UTF-8") as file:
    file_lines = file.read().splitlines()


def encode(line: str) -> str:
    new_text = []
    for char_num in range(len(line)):
        if line[char_num] == " ":
            new_text.append(" ")
            continue
        char_ord = ord(line[char_num]) - 96
        char_ord += key[char_num % key_length]
        char_ord %= 26
        char_ord += 96
        new_text.append(chr(char_ord))

    return "".join(new_text) + "\n"


for file_line in range(len(file_lines)):
    file_lines[file_line] = encode(file_lines[file_line])

with open("12_1_e.txt", "w", encoding="UTF-8") as file:
    file.writelines(file_lines)
