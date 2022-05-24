with open("19_1.txt", "r", encoding="UTF-8") as file:
    essay_lines = file.read().splitlines()

print("\n".join(essay_lines))
print()

word_count = 0
char_count = 0

for line in essay_lines:
    line = line.strip().strip(".")
    line_split = line.split()
    word_count_line = len(line_split)

    char_count_line = 0
    for line_word in line_split:
        char_count_line += len(line_word)

    print(line, word_count_line, char_count_line)

    word_count += word_count_line
    char_count += char_count_line

print(f"Počet slov v texte: {word_count}, počet znakov v texte: {char_count}")
