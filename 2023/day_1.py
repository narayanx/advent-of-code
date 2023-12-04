import re
from pathlib import Path

program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"
with open(data_fp, "r", encoding="utf-8") as file:
    text = [line.strip() for line in file]


def part_1(text):
    total = 0
    for line in text:
        digits = [d for d in line if d.isdigit()]
        total += int(f"{digits[0]}{digits[-1]}")
    return total


def part_2(text):
    WORD_DIGITS = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    digits = [str(x) for x in range(1, 10)]

    words_to_digit = {string: digit for string, digit in zip(WORD_DIGITS, digits)}

    # https://stackoverflow.com/a/70979561
    regex_digits = "(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)"
    regex_temp = "".join([r"(?=(\d|", regex_digits, "))"])
    regex = re.compile(regex_temp)

    total = 0

    for line in text:
        line_matches = re.findall(regex, line)
        line_matches = [[word for word in match if word] for match in line_matches]

        first_match = line_matches[0][0]
        last_match = line_matches[-1][-1]

        first_num = (
            first_match if first_match.isdigit() else words_to_digit[first_match]
        )
        last_num = last_match if last_match.isdigit() else words_to_digit[last_match]

        total += int(f"{first_num}{last_num}")
    return total


print(f"{part_1(text=text)= }")
print(f"{part_2(text=text)= }")
