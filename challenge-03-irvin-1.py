n = int(input())
lst = []

for i in range(n):
    lst.append(int(input()))

first_max = max(lst)

# list comprehension
lst = [e for e in lst if e != first_max]

# for
# for e in lst:
#     if e != first_max:
#         lst.append(e)

second_max = max(lst)
print (second_max, lst.count(second_max))
