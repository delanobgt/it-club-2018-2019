n = int(input('n: '))
lst = []

for i in range(n):
    lst.append(int(input(f'data ke-{i+1}: ')))

print ('maximum value: ', max(lst))
print ('maximum value count: ', lst.count(max(lst)))
