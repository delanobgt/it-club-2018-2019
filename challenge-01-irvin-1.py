a = input()
b = input()

# cara 1
#print ('Anagram' if sorted(a) == sorted(b) else 'Bukan Anagram')

# cara 2
print ('Anagram' if set(a) == set(b) else 'Bukan Anagram')