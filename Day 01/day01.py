with open("Day 01/input.txt") as file:
    lines = file.readlines()

# part one
total_sum = 0
for line in lines:
    number = ""
    for char in line:
        if char.isdigit():
            number += char
            break
    for char in line[::-1]:
        if char.isdigit():
            number += char
            break
    total_sum += int(number)

print(total_sum)

# part two
word_to_digit = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open("Day 01/input.txt") as file:
    lines = file.readlines()

total_sum = 0
for line in lines:
    digits = [(str(digit), line.find(str(digit))) for digit in range(1,10)] 
    digit_words = [(word_to_digit[word_digit], line.find(str(word_digit))) for word_digit in word_to_digit] 
    found_digits = [digit_tuple for digit_tuple in digits+digit_words if digit_tuple[1]!=-1]  
    first_digit = min(found_digits,key=lambda x: x[1])[0]

    # now reverse everything
    digits = [(str(digit), line[::-1].find(str(digit))) for digit in range(1,10)] 
    digit_words = [(word_to_digit[word_digit], line[::-1].find(word_digit[::-1])) for word_digit in word_to_digit] 
    found_digits = [digit_tuple for digit_tuple in digits+digit_words if digit_tuple[1]!=-1]  
    last_digit = min(found_digits,key=lambda x: x[1])[0]

    total_sum += int(first_digit+last_digit)

print(total_sum)
