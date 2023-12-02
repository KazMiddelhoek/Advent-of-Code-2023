with open("Day 02/input.txt") as file:
    games = file.read().splitlines()

limits={"red": 12, "green": 13, "blue": 14}

sum_of_game_ids=0
for game in games:
    game_id = int(game.split(":")[0].split(" ")[-1])
    print(game_id)
    
    game_is_possible_within_limits = True
    for set in game.split(": ")[1].split("; "):
        for dice_set in set.split(", "):
            amount_of_color, color = dice_set.split(" ")
            if int(amount_of_color) > limits[color]:
                game_is_possible_within_limits = False

    if game_is_possible_within_limits:
        sum_of_game_ids += game_id
print(sum_of_game_ids)

# part 2
with open("Day 02/input.txt") as file:
    games = file.read().splitlines()

sum_of_powers=0
for game in games:
    minimum_required = {"red": 0, "green": 0, "blue": 0}
    for set in game.split(": ")[1].split("; "):
        for dice_set in set.split(", "):
            amount_of_color, color = dice_set.split(" ")
            minimum_required[color] = max(minimum_required[color], int(amount_of_color))

    minimum_numbers = [*minimum_required.values()]
    power = minimum_numbers[0]*minimum_numbers[1]*minimum_numbers[2]
    sum_of_powers += power
print(sum_of_powers)