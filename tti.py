magassag = int(input('add meg a magasságod (cm): ')) / 100
testtomeg = float(input('add meg a testsúlyod (kg): '))

tti = testtomeg / magassag ** 2

print('a testsúlyosztályod:', end=' ')
if tti < 16: print('súlyos soványság')
elif tti < 17: print('mérsékelt soványság')
elif tti < 18.5: print('enyhe soványság')
elif tti < 25: print('normál testsúly')
elif tti < 30: print('túlsúlyos')
elif tti < 35: print('I. fokú elhízás')
elif tti < 40: print('II. fokú elhízás')
else: print('súlyos elhízás')