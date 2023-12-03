import re
from pathlib import Path

red_re = re.compile(r"\d+(?= red)")
green_re = re.compile(r"\d+(?= green)")
blue_re = re.compile(r"\d+(?= blue)")

text = []
program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"
with open(data_fp, "r", encoding="utf-8") as file:
    # [game, [[r, g, b], [r, g, b]], game, [[r, g, b], [r, g, b]],  ...]
    for line in file:
        game_str, other_str = line.split(":")
        other_str = other_str.strip()
        game = int("".join(char for char in game_str if char.isdigit()))
        all_games = other_str.split("; ")

        text.append((game, []))

        for g in all_games:
            try:
                red_num = int(re.findall(red_re, g)[0])
            except IndexError:
                red_num = 0
            try:
                green_num = int(re.findall(green_re, g)[0])
            except IndexError:
                green_num = 0
            try:
                blue_num = int(re.findall(blue_re, g)[0])
            except IndexError:
                blue_num = 0
            text[-1][1].append([red_num, green_num, blue_num])


def part_1(text: list[tuple[int, list[tuple[int, int, int]]]]):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    total = 0
    for game_num, gameplay in text:
        for r, g, b in gameplay:
            if r > MAX_RED:
                break
            if g > MAX_GREEN:
                break
            if b > MAX_BLUE:
                break
        else:
            total += game_num
    return total


def part_2(text: list[tuple[int, list[tuple[int, int, int]]]]):
    total = 0
    max_red = max_green = max_blue = 0
    for _, gameplay in text:
        for r, g, b in gameplay:
            max_red = max(max_red, r)
            max_green = max(max_green, g)
            max_blue = max(max_blue, b)
        total += max_blue * max_red * max_green
        max_red = max_green = max_blue = 0
    return total


print(f"{part_1(text)= }")
print(f"{part_2(text)= }")
