with open("13_1_1.txt", "r", encoding="UTF-8") as file:
    image_lines = file.read().splitlines()
    image_lines[0] += "\n"


def encode_line(line: str) -> str:
    line_out = []
    counter = 1
    last_char = "0"
    if line[0] != "0":
        line_out.append("0")
        last_char = "1"

    for actual_character in line[1:]:
        if actual_character == last_char:
            counter += 1
            continue

        line_out.append(str(counter))
        last_char = actual_character
        counter = 1

    line_out.append(str(counter))
    return " ".join(line_out)


for line_num in range(1, len(image_lines)):
    image_lines[line_num] = encode_line(image_lines[line_num]) + "\n"

with open("13_1_1_e.txt", "w", encoding="UTF-8") as file:
    file.writelines(image_lines)
