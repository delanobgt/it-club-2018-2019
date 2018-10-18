n = int(input('Berapa: '))
for i in list(reversed(range(n))) + list(range(1, n)):
    print (' '*i + '*'*((n-i)*2-1))
