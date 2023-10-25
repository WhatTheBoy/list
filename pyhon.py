rainbow_colors = {'red', 'orange', 'yellow', 'green', 'blue',
                  'indigo', 'violet'}
print(rainbow_colors)
print(type(rainbow_colors))
empty_set = set()


number_list = [1, 43, 231]
# there are repeating elements in this list using 'set' we remove them because in
# a set all objects are unique and cannot be repeated
text_tuples = ('abc', 'def', 'gk', 'gk', 'gk')
number_list = tuple(number_list)
set_text = (set(number_list+text_tuples))
print(type(set_text))
print(set_text)

# Adding
set_text.add('fgf')
set_text.add(12.32)
print(set_text)

# random deleted
pop_element = set_text.pop()
print(pop_element)
# removing
removing_element = set_text.remove('abc')
print(removing_element)
# discard
set_text.discard('def')
set_text.discard(1)
print(set_text)
