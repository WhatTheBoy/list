x = 5
while x >= 2:
    print(x)
    x -= 1  # x = x - 1

while x < 10:
    print(x)
    x += 1  # x = x + 1
print('Next code')

while x < 10:
    print(str(x)+' x is less than 10')
    x += 1
else:
    print(str(x)+' x is not more than 10')
# ===
# ===
for x in range(0, 10):
    print(str(x)+' x is less than 10')
else:
    x += 1
    print(str(x)+' x is not more than 10')

# break ,continue,  pass
my_list = [1, 2, 3]

for item in my_list:
    pass
print(item)
for item in my_list:
    if item == 2:
        break
    print(item)
print('another code')
for item in my_list:
    if item == 2:
        continue
    print(item)
print('another code')
