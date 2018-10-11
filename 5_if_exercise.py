
# if statement

n = int(input('masukkan nilai (satuan-jutaan): '))

if n <= 9:
    print ('satuan')
elif n <= 99:
    print ('puluhan')
elif n <= 999:
    print ('ratusan')
elif n <= 9999:
    print ('ribuan')
elif n <= 99999:
    print ('puluhan ribuan')
elif n <= 999999:
    print ('ratusan ribuan')
elif n <= 9999999:
    print ('jutaan')
else:
    print ('out of range! (^.^)')
