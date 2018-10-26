n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

first_max = max(lst)
lst.remove(first_max)
second_max = max(lst)
print (second_max, lst.count(second_max))
