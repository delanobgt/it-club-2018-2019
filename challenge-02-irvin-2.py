n = int(input('n: '))
lst = []

for i in range(n):
    lst.append(int(input(f'data ke-{i+1}: ')))

max_value = lst[0]
max_count = 1
for item in lst[1:]:
    if item > max_value:
        max_value = item
        max_count = 1
    elif max_value == item:
        max_count += 1

print ('maximum value: ', max_value)
print ('maximum value count: ', max_count)
