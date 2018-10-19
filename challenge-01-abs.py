n = int(input('Berapa: '))
m = n*2-1
for i in range(m):
    space = abs(n-1-i)
    for j in range(m):
        if space <= j and j <= m-space-1: print('*', end='')
        else: print (' ', end='')
    print()

# abs(-7) => 7
# abs(5) => 5
# abs(2) => 2
# abs(0) => 0