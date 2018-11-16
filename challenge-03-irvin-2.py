n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

first = -1
second = -1
first_count = second_count = 1

for item in lst:
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

print (second, second_count)
