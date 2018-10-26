n = int(input('n: '))
lst = []

for i in range(n):
    lst.append(int(input(f'data ke-{i+1}: ')))

m = max(lst)
print ('maximum value: ', m)
print ('maximum value count: ', lst.count(m))
