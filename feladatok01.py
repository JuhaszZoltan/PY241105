# --- feladatok 01 / 1 (lakcím) ----------------
# print('add meg a következő adatokat:')
# irsz = input('irányítószám: ')
# varos = input('telpülés: ')
# kt_nev = input('közterület neve: ')
# kt_jelleg = input('közterület jellege: ')
# hsz = input('házszám: ')

# print(irsz + ' ' + varos + ' ' + kt_nev + ' ' + kt_jelleg + ' ' + hsz + '.')
# print(f'{irsz} {varos} {kt_nev} {kt_jelleg} {hsz}.')

# --- feladatok 01 / 2 (nevek) ----------------
# vn1 = input('első vezetéknév: ')
# vn2 = input('második vezetéknév: ')
# kn1 = input('első keresztnév: ')
# kn2 = input('második keresztnév: ')

# print('képezhető nevek:')
# print(f'{vn1} {kn1}')
# print(f'{vn1} {kn2}')
# print(f'{vn2} {kn1}')
# print(f'{vn2} {kn2}')

# --- feladatok 01 / 3 (fizetes) ----------------
# havi_fizetes = int(input('írd be a havi fizetésed (HUF): '))
# print(f'éves fizetésed: {12 * havi_fizetes:,} HUF')

# --- feladatok 01 / 5 (teglalap_ker_ter) ----------------
# print('add meg egy téglalap oldalainak hosszát (cm):')
# a = int(input('a:= '))
# b = int(input('b:= '))
# print(f'téglalap kerülete: {2 * (a + b)} cm')
# print(f'téglalap területe: {a * b} cm^2')

# --- feladatok 01 / 6 (kor_ker_ter) ----------------
# import math
# from math import sin, cos, pi
# print('add meg egy körsugarának hosszát (cm):')
# r = float(input('r:= '))
# print(f'kör kerülete: {2 * r * pi:.4f} cm')
# print(f'kör területe: {round(r ** 2 * pi, 4)} cm^2')

# --- feladatok 01 / 7 (pitagorasz) ----------------
# from math import sqrt
# print('add egy derégszögű 3szög két befogóját (cm):')
# a = float(input('a:= '))
# b = float(input('b:= '))

# print(f'c:= {(a**2 + b**2)**.5:.2f} cm')
# print(f'c:= {sqrt(a**2 + b**2):.2f} cm')