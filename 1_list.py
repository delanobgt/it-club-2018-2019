lst = [50, 60, 70, 80, 90]

# indexing
print (lst[0]) # first item
print (lst[0], lst[1], lst[2], lst[3], lst[4]) # all items
# print (lst[5]) # index out of range
print (lst[-1]) # last item
print (lst[-2]) # second last item

# mutating
lst[0] = 99
print (lst)

# list length
print (len(lst))

# slicing
print (lst[2:4]) # index 2, 3
print (lst[:2]) # index 0, 1
print (lst[2:]) # index 2, 3, 4
print (lst[:]) # all item
print (lst[1:4:2]) # index 1, 3 (2 step)

print (lst[4:2:-1]) # index 4, 3 (reversed)
print (lst[4:1:-2]) # index 4, 2 (reversed, 2 step)

# concat list
lst = [1, 2, 3] + [4, 5, 6]
print (lst)
lst = [1, 2, 3]
lst.extend([4, 5, 6])
print (lst)

# append last
lst = [1, 2, 3]
lst.append(4)
print (lst)

# pop last
lst.pop()
print (lst)

# list multiplying
lst = [1] * 5
print (lst)
lst = [4, 5, 6] + [1] * 5
print (lst)

# iterating
for item in lst:
    print (item, end=' ')
print()