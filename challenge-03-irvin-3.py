n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

first = lst[0]
second = -1
first_count = second_count = 1

for item in lst[1:]:
    if item == first:
        first_count += 1
    elif item == second:
        second_count += 1
    elif item > first:
        first, second = item, first
        first_count, second_count = 1, first_count
    elif item > second:
        second = item
        second_count = 1

if second == -1:
    print ('tidak ada nilai tertinggi ke-2')
else:
    print (second, second_count)
