from pathlib import Path
from collections import Counter
text = []
program_fp = Path(__file__)
data_fp = program_fp.parent / f"{program_fp.stem}.txt"
with open(data_fp, "r", encoding="utf-8") as file:
    text = [line.strip().split() for line in file]

NUM_CARDS = 13
def part_1(hands_bids):
    non_digit_cards = {"A": 14, "K": 13, "Q": 12, "J": 11, "T":10}
    
    def sort_cards(hand):
        cards = list(hand)
        int_cards = [int(card) if card.isdigit() else non_digit_cards[card] for card in cards]
        card_counts = Counter(int_cards)

        one_count = two_count = three_count = 0
        for value, count in card_counts.most_common():
            if count == 5:
                return 7
            if count == 4:
                return 6
            if count == 3:
                three_count += 1
            # one pair
            if count == 2:
                two_count += 1
            if count == 1:
                one_count += 1
        # full house
        if three_count == 1 and two_count == 1:
            return 5
        # three of a kind
        if three_count == 1:
            return 4
        # two pair
        if two_count == 2:
            return 3
        # one pair
        if two_count == 1:
            return 2
        # highest card
        return 1
    ranks_values_bid = sorted((sort_cards(value), value, bid) for value, bid in hands_bids)
    print(f"{ranks_values_bid=}")
        
        

def part_2(text):
    pass

print(f"{part_1(text)= }")
print(f"{part_2(text)= }")
