# típusok

# egész (integer) int
# lebegőpontos számok (floating point number) float
#( +, -, *, /, **, //, %)

# logika (bool) bool
# and, or, not
# and -> akkor igaz, ha mindkét operandus igaz
# or  -> akkor igaz, ha legalább az egyik operandus igaz
# not -> egyoperandusú -> az "ellenkezője" lesz az érték
# "not True" == "False" "not False" == True

# karakterlánc (string) str
# str + str -> konkatenáció
# str * int -> többszörös konkatenáció

# compare aka. 'összehasonlító operátorok':
# <, >, <=, >=, ==, !=

# -----------------

# input -> "bevitel", vagy "bekérés" -> input()
# output -> "kimenet" -> print()

# nev = input('Hogy hívnak? ')
# print(f'Szia {nev}!')
# kor = int(input('Hány éves vagy? '))

# minden algoritmus leírható ezekkel:
# - szekvencia (egymás után történnek dolgok [nem "egyszerre"])
# - szelekció 'elágazás'
# - iteráció 'ciklus' (ezekről majd később)

# if <condition>:
#   [indent] kódrészlet, ami akkor fut le, ha a <condition> -> True
# else:
#   [indent] kódrészlet, ami akkor fut le, ha a <condition> -> False

# az 'else' rész opcionális (vem kötelező)
#  "feltétel" <- ha ezt kiértékelem, akkor a vége bool (vagy igaz, vagy hamis)

valasz:str = input('elmegyek este berúgni? ')

if valasz == 'igen':
  print('akkor készülj!')
  print('sor, ha igaz')
else:
  print('akármi')
  print('sor, ha hamis')
print('sor, ha vége az elágazásnak')