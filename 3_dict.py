dct = {
    'Ular': 'Python',
    'Tikus': 'Mouse',
    'Anjing': 'Dog',
    'Kucing': 'Cat',
}
print (dct)

# get
print (dct['Ular'])
# print (dct['Kuda']) # error
print (dct.get('Kuda', 'memang gaada')) # error

# set
dct['Ular'] = 'Snake' # overwrite
dct['Naga'] = 'Dragon' # new
print (dct)

print('Keys: ')
for key in dct.keys():
    print (key, end=' ')
print('\n')

print('Values: ')
for value in dct.values():
    print (value, end=' ')
print('\n')

print('Items: ')
for key, value in dct.items():
    print (key, value)
print('\n')
