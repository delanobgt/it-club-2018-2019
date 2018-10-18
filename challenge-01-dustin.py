n = int(input('Please input a number: '))
for i in range(1, 2*n+1):
    print ((n - (i - 2 * (i // n) * (i - n))) * ' ' + ((2 * (i - 2 * (i // n) * (i-n))) - 1) * '*')