greeting = 'Hello!'
letter_list = []
for letter in greeting:
    letter_list.append(letter)
print(letter_list)

letter_list = [letter for letter in greeting]
print(letter_list)
# str
number_list = [number for number in '0123456789']
print(number_list)
# int
number_list_1 = [num for num in range(0, 10)]
print(number_list_1)


number_list_2 = [num ** 2 for num in range(0, 10)]
print(number_list_2)

number_list_3 = [-((num - 2) / 3) ** 2 for num in range(0, 10)]
print(number_list_3)

list_number = [6, 3, 34, -543, 23, 534, 2, -432]
new_list = [number for number in list_number if number < 0]
print(new_list)


greetings = ['hello', 'hi', 'hey', 'hola']
secound_letter = []
for word in greetings:
    secound_letter.append(word[1])
print(secound_letter)

greetings = ['hello', 'hi', 'hey', 'hola']
letter_list = [greeting[1] for greeting in greetings]
print(letter_list)


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_digits = []
for dig in digits:
    if dig % 2 == 0:
        new_digits.append(dig)

print(new_digits)

new_digits_1 = []
new = [gid for gid in digits if gid % 2 == 0]
print(new)
