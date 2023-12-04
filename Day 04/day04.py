with open("Day 04/input.txt") as file:
    cards = file.read().splitlines()

total_number_of_points = 0
for card in cards:
    winning_numbers = set(card.split(": ")[1].split(" | ")[0].split())
    my_numbers = card.split(": ")[1].split(" | ")[1].split()

    n_numbers_in_winning_numbers = sum(1 for number in my_numbers if number in winning_numbers)
    if n_numbers_in_winning_numbers >= 1:
        total_number_of_points += 2**(n_numbers_in_winning_numbers-1)
print(total_number_of_points)


# part two
with open("Day 04/input.txt") as file:
    cards = file.read().splitlines()

n_instances_per_card = {i: 1 for i in range(1, len(cards)+1)}
for card, card_number in zip(cards, n_instances_per_card):
    winning_numbers = set(card.split(": ")[1].split(" | ")[0].split())
    my_numbers = card.split(": ")[1].split(" | ")[1].split()
    n_numbers_in_winning_numbers = sum(1 for number in my_numbers if number in winning_numbers)

    for next_card_number in range(1, 1+n_numbers_in_winning_numbers):
        n_instances_per_card[card_number+next_card_number] += n_instances_per_card[card_number]
print(sum(n_instances_per_card.values()))