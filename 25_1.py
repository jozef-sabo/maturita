"""
Na informatike sme sa naučili vykonávať prevody čísiel medzi číselnými sústavami. Pre uľahčenie tohto procesu pre
prevod čísla z dekadickej do binárnej či inej sústavy je možné príslušný algoritmus zapísať vo forme programu.
Vytvorte program , ktorý:
- po vložení čísla v dekadickej číselnej sústave prevedie toto číslo do binárnej číselnej sústav
a vypíše obe číselné hodnoty,
- po vložení čísla v dekadickej číselnej sústave a čísla predstavujúceho číselnú sústavu
do ktorej prevod chceme vykonať, prevedie číslo do zvolenej sústavy a obe čísla vypíše.
"""
import math


def dec_to_base(number: int, base: int):
    number_of_places = math.ceil(math.log(number, base))

    new_num = ""
    for _ in range(number_of_places):
        new_num += str(number % base)
        number = number // base

    return int(new_num[::-1])


number_to_convert = int(input("Vložte číslo na konvert: "))
base_to_convert = int(input("Vložte základ na konvert: "))

print(number_to_convert, dec_to_base(number_to_convert, 2))
print(number_to_convert, dec_to_base(number_to_convert, base_to_convert))

# 29


def base_to_dec(number: int, base: int):
    number = str(number)
    new_num = 0
    for exponent in range(len(number)):
        new_num += int(number[-1-exponent]) * math.pow(base, exponent)

    return int(new_num)
