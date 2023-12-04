from pathlib import Path

program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"
with open(data_fp, "r", encoding="utf-8") as file:
    text = [line.strip() for line in file]
    new_text = []
    for line in text:
        before_card_num, after_card_num = line.split(": ")
        card_num = "".join([char for char in before_card_num if char.isdigit()])
        winning_nums, my_nums = after_card_num.split(" | ")
        winning_nums, my_nums = winning_nums.replace("  ", " "), my_nums.replace("  ", " ")
        winning_nums = {i for i in winning_nums.split(" ") if i}
        my_nums = [j for j in my_nums.split(" ") if j]

        winning_nums, my_nums = list(map(int, winning_nums)), list(map(int, my_nums))
        new_text.append((int(card_num), winning_nums, my_nums))


def part_1(text: list[tuple[int, set[int], list[int]]]):
    t = 0
    for card_num, winning, mine in text:
        has_one_win = False
        running_points = 0
        for card in mine:
            if card in winning:
                if not has_one_win:
                    running_points = 1
                    has_one_win = True
                else:
                    running_points *= 2
        t += running_points
    return t


def part_2(text: list[tuple[int, set[int], list[int]]]):
    num_cards = [1 for _ in range(len(text))]
    for card_num, winning, mine in text:
        for _ in range(num_cards[card_num - 1]):
            running_wins = 0
            for card in mine:
                if card in set(winning):
                    running_wins += 1
            for offset in range(1, running_wins + 1):
                try:
                    num_cards[card_num - 1 + offset] += 1
                except IndexError:
                    pass
    return sum(num_cards)


print(f"{part_1(new_text)= }")
print(f"{part_2(new_text)= }")
