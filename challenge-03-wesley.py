nm_bln = ('Januari', 'Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember')
repeat = 'y'
 
while repeat == 'y':
    print('Zodiak Determinator')
    tgl = int(input('Input tanggal : '))
    bln = int(input('Input bulan : '))
 
    if (20 <= tgl <= 31 and bln == 1) or (1 <= tgl <= 18 and bln == 2):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Aquarius')
    elif (19 <= tgl <= 29 and bln == 2) or (1 <= tgl <= 20 and bln == 3):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Pisces')
    elif (21 <= tgl <= 31 and bln == 3) or (1 <= tgl <= 19 and bln == 4):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Aries')
    elif (20 <= tgl <= 30 and bln == 4) or (1 <= tgl <= 20 and bln == 5):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Taurus')
    elif (21 <= tgl <= 31 and bln == 5) or (1 <= tgl <= 20 and bln == 6):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Gemini')
    elif (21 <= tgl <= 30 and bln == 6) or (1 <= tgl <= 22 and bln == 7):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Cancer')
    elif (23 <= tgl <= 31 and bln == 7) or (1 <= tgl <= 22 and bln == 8):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Leo')
    elif (23 <= tgl <= 31 and bln == 8) or (1 <= tgl <= 22 and bln == 9):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Virgo')
    elif (23 <= tgl <= 30 and bln == 9) or (1 <= tgl <= 22 and bln == 10):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Libra')
    elif (23 <= tgl <= 31 and bln == 10) or (1 <= tgl <= 21 and bln == 11):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Scorpio')
    elif (22 <= tgl <= 30 and bln == 11) or (1 <= tgl <= 21 and bln == 12):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Sagittarius')
    elif (22 <= tgl <= 31 and bln == 12) or (1 <= tgl <= 19 and bln == 1):
        print('Zodiak pada tanggal '+ str(tgl)+' '+nm_bln[bln-1]+' adalah : Capricorn')
    else:
        print('Tanggal anda salah, coba lagi :)')
       
    repeat=input('Continue?(y/n) : ')
    print()