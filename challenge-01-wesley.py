n = int(input('Berapa: ')) 
m = n * 2 - 1
for i in range(1,m+1):
    for j in range(1,m+1):
        if (i <= n and j <= n-i) or (i <= n and j >= n + i) or (i > n and j <= i - n) or (i > n and j >= 2 * n - (i - n)):
            print(' ', end='')
        else:
            print('*', end='')
    print()