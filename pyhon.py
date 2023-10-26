number_list = [12, 23, 44, 32, 564, 34, 123, 32, 545, 2342134]
for first_number in number_list:
    print(str(first_number) + 'hola' + str(321))
for number in number_list:
    if number % 2 == 0:
        print(number)
    else:
        print('hey')


number_list = [12, 23, 44, 32, 564, 34, 123, 32, 545, 2342134]
list_number_sum = 0
for sum in number_list:
    list_number_sum = list_number_sum + sum
print(list_number_sum)

for letter in "Hello Python":
    if letter != 'o':
        print(letter)

tuple_list_1 = [('a', 'b'), ('c', 'd'), ('e', 'f'), ('g', 'h')]
for item in tuple_list_1:
    print(item)

for letter_1, letter_2 in tuple_list_1:
    print(letter_1, letter_2)
print(type(item))
print(type(letter_2))
print(type(tuple))


tuple_list = [('a', 'b', 3), ('c', 'd', 32),
              ('e', 'f', 321), ('g', 'h', 32123)]
for letter_1, letter_2, number_1 in tuple_list:
    print(letter_1, letter_2, number_1)

name = input(("Input your name:"))
surname = input(("Input your surname:"))
dict = {
    'user_id': 2131,
    'user_name': name,
    'user_sername': surname
}
# key
for items in dict:
    print(items)

for items in dict.keys():
    print(items)
# key velue pairs in tuples
for items in dict.items():
    print(items)
# velue
for items in dict.values():
    print(items)
for items, velue in dict.items():
    print(velue)


for i in range(4):
    print(i)
