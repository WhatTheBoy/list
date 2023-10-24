first_list = [123, 32]
secound_list = ['abc', 'melon']

finaly_list = first_list.__add__(secound_list)


print(len(finaly_list))
print(finaly_list[2])


new_list = finaly_list[:2]
finaly_list[0] = '213'
changed_list = finaly_list + new_list

# Adding items
changed_list.append('New_object')
changed_list.insert(0, 'start')
changed_list.insert(4, 'middle')
# Removing items
changed_list.pop(2)
deleted_item = changed_list.pop()
removing_items = changed_list.remove('213')
print(deleted_item)
print(removing_items)
# method sort and copy

number_list = [1, 3, 2, 54353, -2312, 534345]
letter_list = ['v', 'd', 'g', 'ds']
sort_number_list = number_list.copy()
sort_letter_list = letter_list.copy()

sort_number_list.sort()
sort_letter_list.sort()

print(number_list)
print(sort_number_list)
print(letter_list)
print(sort_letter_list)

# reverse
number_list.reverse()

print(number_list)
print(sort_number_list)
print(letter_list)
print(sort_letter_list)


print(changed_list)


home_list = [123, 213.23, 'abc', True, 10+4j]
print(home_list)
new_home_list = home_list[1:3]
print(new_home_list)
