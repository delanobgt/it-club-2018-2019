n = int(input('n: '))

print()

for r in range(n):
    for c in range(r+1):
        print ('*', end='')
    print()

print()

for r in range(n, 0, -1):
    for c in range(r):
        print ('*', end='')
    print()

print()

for r in range(n, 0, -1):
    for c in range(1, n+1):
        if c >= r: print ('*', end='')
        else: print (' ', end='')
    print()

print()

for r in range(1, n+1):
    for c in range(1, n+1):
        if c >= r: print ('*', end='')
        else: print (' ', end='')
    print()
