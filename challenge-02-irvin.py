n = int(input('n: '))

print()

for r in range(1, n+1):
    for c in range(1, r+1):
        print (n-c+1, end='')
    print()

print()

for r in range(n, 0, -1):
    for c in range(1, r+1):
        print (n-c+1, end='')
    print()

print()

for r in range(n, 0, -1):
    for c in range(1, n+1):
        if c >= r: print (n-c+1, end='')
        else: print (' ', end='')
    print()

print()

for r in range(1, n+1):
    for c in range(1, n+1):
        if c >= r: print (n-c+1, end='')
        else: print (' ', end='')
    print()
