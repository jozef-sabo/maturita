with open("15_1_1.txt", "r", encoding="UTF-8") as file:
    image_lines = file.read().splitlines()
    image_lines[0] += "\n"


def decode_line(line: str) -> str:
    line = line.split()
    out_str = ""
    for line_group in range(len(line)):
        out_str += str(line_group % 2) * int(line[line_group])
    return out_str


for line_num in range(1, len(image_lines)):
    image_lines[line_num] = decode_line(image_lines[line_num]) + "\n"

with open("15_1_1_e.txt", "w", encoding="UTF-8") as file:
    file.writelines(image_lines)
