from collections import Counter
from functools import cmp_to_key
from itertools import combinations_with_replacement
with open("Day 07/input.txt") as file:
    hands = file.read().splitlines()


def find_type_of_hand(hand) -> int:
    hand = Counter(hand)
    if len(list(hand)) == 5:
        return 1
    if len(list(hand)) == 4:
        return 2
    if len(list(hand)) == 3 and hand.most_common(1)[0][1] == 2:
        return 3
    if len(list(hand)) == 3 and hand.most_common(1)[0][1] == 3:
        return 4
    if len(list(hand)) == 2 and hand.most_common(1)[0][1] == 3:
        return 5        
    if len(list(hand)) == 2 and hand.most_common(1)[0][1] == 4:
        return 6    
    if len(list(hand)) == 1:
        return 7    

def compare_hands(hand_1, hand_2):
    hand_1 = hand_1.split(" ")[0]
    hand_2 = hand_2.split(" ")[0]

    if find_type_of_hand(hand_1) > find_type_of_hand(hand_2):
        return 1
    if find_type_of_hand(hand_1) < find_type_of_hand(hand_2):
        return -1
    
    letter_to_number = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10
    }
    
    for card_hand_1, card_hand_2 in zip(hand_1, hand_2):
        if card_hand_1 == card_hand_2:
            continue
        
        card_hand_1, card_hand_2 = [int(card) if card.isnumeric() else letter_to_number[card] for card in [card_hand_1, card_hand_2] ]

        if card_hand_1 > card_hand_2:
            return 1
        if card_hand_1 < card_hand_2:
            return -1        

    return 0

hands = sorted(hands,  key=cmp_to_key(compare_hands))

total_winnings = 0
for rank,hand in enumerate(hands, 1):
    total_winnings += rank*int(hand.split(" ")[1])
print(total_winnings)


# part two
with open("Day 07/input.txt") as file:
    hands = file.read().splitlines()

def type_of_hand(hand) -> int:
    if "J" not in hand:
        return find_type_of_hand(hand)

    best_hand = -1
    n_Js = len([card for card in hand if card == "J"])
    for combination in combinations_with_replacement([str(n) for n in range(2,10)]+["T", "Q", "K", "A"], n_Js):
        hand_attempt = hand
        for card in combination:
            hand_attempt=hand_attempt.replace("J", card, 1)
        best_hand = max(best_hand, find_type_of_hand(hand_attempt))
    return best_hand

def compare_hands(hand_1, hand_2):
    hand_1 = hand_1.split(" ")[0]
    hand_2 = hand_2.split(" ")[0]

    if type_of_hand(hand_1) > type_of_hand(hand_2):
        return 1
    if type_of_hand(hand_1) < type_of_hand(hand_2):
        return -1
    
    letter_to_number = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "T": 10,
        "J": 1
    }
    
    for card_hand_1, card_hand_2 in zip(hand_1, hand_2):
        if card_hand_1 == card_hand_2:
            continue
        
        card_hand_1, card_hand_2 = [int(card) if card.isnumeric() else letter_to_number[card] for card in [card_hand_1, card_hand_2]]

        if card_hand_1 > card_hand_2:
            return 1
        if card_hand_1 < card_hand_2:
            return -1        

    return 0

hands = sorted(hands,  key=cmp_to_key(compare_hands))

total_winnings = 0
for rank,hand in enumerate(hands, 1):
    total_winnings += rank*int(hand.split(" ")[1])
print(total_winnings)