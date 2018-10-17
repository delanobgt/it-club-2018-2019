n = int(input('Berapa: '))
m = n*2-1
for i in range(m):
    space = abs(n-1-i)
    for j in range(m):
        if space <= j and j <= m-space-1: print('*', end='')
        else: print (' ', end='')
    print()