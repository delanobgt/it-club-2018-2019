month_names = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
pivots = [21, 19, 21, 21, 21, 22, 23, 24, 24, 24, 23, 22, 21, 19]
zodiac_names = ['Aquarius', 'Pisces', 'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn']

print('Zodiak Determinator')
day = int(input('Input tanggal: '))
month = int(input('Input bulan: ')) - 1

if day < pivots[month]: 
    print(f'Zodiak pada tanggal {day} {month_names[month]} adalah : {zodiac_names[(month-1)]}')
else: 
    print(f'Zodiak pada tanggal {day} {month_names[month]} adalah : {zodiac_names[month]}')