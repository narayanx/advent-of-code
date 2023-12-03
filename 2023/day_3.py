from itertools import permutations
from pathlib import Path

program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"
with open(data_fp, "r", encoding="utf-8") as file:
    text = [line.strip() + "." for line in file]


def count_numbers(text: list[str]) -> int:
    num_numbers = 0
    for line in text:
        last_was_digit = False
        for char in line:
            if char.isdigit():
                if not last_was_digit:
                    num_numbers += 1
                    last_was_digit = True
            else:
                last_was_digit = False
    return num_numbers


def get_id_number_text(text: list[str]) -> list[str]:
    id_number_text = []
    running_number_count = 0
    for line in text:
        last_was_digit = False
        id_line = []
        for char in line:
            if not char.isdigit():
                if last_was_digit:
                    running_number_count += 1
                id_line.append(char)
                last_was_digit = False
            elif char.isdigit():
                id_line.append(str(running_number_count))
                last_was_digit = True
            else:
                id_line.append(char)

        id_number_text.append(id_line)
    return id_number_text


def part_1(text: list[str]):
    num_numbers = count_numbers(text)

    is_valid_part = [False for _ in range(num_numbers)]
    number_value = ["" for _ in range(num_numbers)]

    # make copy where numbers have id's
    id_number_text = get_id_number_text(text)

    # # get value of each number
    for line_idx, line in enumerate(id_number_text):
        for char_idx, char in enumerate(line):
            if char.isdigit():
                # it's an id number
                number_value[int(char)] += text[line_idx][char_idx]

    # convert to ints
    number_value = [int(num) for num in number_value]

    # .permuations doesn't generate duplicates
    deltas = list(permutations([-1, 0, 1], 2))
    deltas.extend([(1, 1), (-1, -1)])

    for line_idx, line in enumerate(id_number_text):
        for char_idx, char in enumerate(line):
            if not char.isdigit() and char != ".":
                # it's a symbol
                for d1, d2 in deltas:
                    try:
                        around_char = id_number_text[line_idx + d1][char_idx + d2]
                    except IndexError:
                        continue
                    if around_char.isdigit():
                        # is an id number
                        is_valid_part[int(around_char)] = True

    # sum all the valid parts
    total = sum(num for num, valid in zip(number_value, is_valid_part) if valid)

    return total


def part_2(text: list[str]):
    total = 0

    num_numbers = count_numbers(text)

    # make copy where numbers have id's
    id_number_text = get_id_number_text(text)

    number_value = ["" for _ in range(num_numbers)]

    # get value of each number
    for line_idx, line in enumerate(id_number_text):
        for char_idx, char in enumerate(line):
            if char.isdigit():
                # it's an id number
                number_value[int(char)] += text[line_idx][char_idx]

    # convert to ints
    number_value = [int(num) for num in number_value if num]

    # .permuations doesn't generate duplicates
    deltas = list(permutations([-1, 0, 1], 2))
    deltas.extend([(1, 1), (-1, -1)])

    for line_idx, line in enumerate(id_number_text):
        for char_idx, char in enumerate(line):
            if not char.isdigit() and char != ".":
                # it's a symbol
                ids_around = set()
                for d1, d2 in deltas:
                    try:
                        around_char = id_number_text[line_idx + d1][char_idx + d2]
                    except IndexError:
                        continue
                    if around_char.isdigit():
                        # is an id number
                        ids_around.add(around_char)

                # special case if char is * and exactly 2 numbers around it
                if char == "*" and len(ids_around) == 2:
                    id_1, id_2 = ids_around
                    id_1, id_2 = int(id_1), int(id_2)
                    total += number_value[id_1] * number_value[id_2]
    return total


print(f"{part_1(text)= }")
print(f"{part_2(text)= }")
