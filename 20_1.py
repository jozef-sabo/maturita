with open("20_1.txt", "r", encoding="UTF-8") as file:
    wages_lines = file.read().splitlines()

wages_sum = 0
_100s = 0
_10s = 0
_1s = 0

for wage in wages_lines:
    wage = wage.split()
    wage_num = int(wage[0])
    wages_sum += wage_num

    print(f"{wage[1]} {wage[2]}: {wage[0]}")

    _100s += wage_num // 100
    wage_num %= 100
    _10s += wage_num // 10
    wage_num %= 10
    _1s += wage_num

print(f"Suma: {wages_sum} €")
print(f"Počet 100viek: {_100s}, počet 10tok: {_10s}, počet 1tiek: {_1s}")

