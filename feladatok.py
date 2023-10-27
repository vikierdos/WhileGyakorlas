# Írjuk ki 0-tól 150-ig a páros számokat!
def feladat_1():
    a = 0
    while a < 150:
        if a % 2 == 0:
            print(a, end="; ")
        a += 1
    print(a)

# Számold meg 10 bekért szám esetében a 3-mal osztható számokat!
def feladat_2():
    a = 0
    oszthato = 0
    while a < 10:
        szam = int(input("Írj be egy számot: "))
        if szam % 3 == 0:
            oszthato += 1
        a += 1
    print(oszthato, "szám osztható hárommal")

# Addig kérjünk be szám(ok)at, amíg 10-zel osztható nem lesz!*
def feladat_3():
    szam = int(input("Írj be egy számot: "))
    while not(szam % 10 == 0):
        szam = int(input("Rossz szám! Írj be egy számot: "))
    print("A nyereményed egy Gucci táska!")

# Addig kérjünk be számokat, amíg nem kapunk kétjegyű és páros számot!*
def feladat_4():
    parostizes = int(input("Írj be egy számot: "))
    if parostizes >= 0:
        while not(10 > parostizes // 10 > 0 and parostizes % 2 == 0):
            parostizes = int(input("Rossz szám! Írj be egy számot: "))
        print("A nyereményed egy Gucci táska!")
    else:
        while not(10 > parostizes*-1 // 10 > 0 and parostizes % 2 == 0):
            parostizes = int(input("Rossz szám! Írj be egy számot: "))
        print("A nyereményed egy Gucci táska!")

# Addig kérjünk be számokat, amíg pozitív páratlan számot nem kapunk.*
def feladat_5():
    pozitivparatlan = int(input("Írj be egy pozitív páratlan számot: "))
    while not(pozitivparatlan > 0 and pozitivparatlan % 2 != 0):
        pozitivparatlan = int(input("Rossz szám! Írj be egy pozitív páratlan számot: "))
    print("A nyereményed egy Gucci táska!")

# Addig kérjünk be számokat, amíg 3-mal osztható vagy négyzetszám nem lesz.*
def feladat_6():
    harmasnegyzet = int(input("Írj be egy hárommal osztható vagy négyzet számot: "))
    if harmasnegyzet > 0:
        while not(harmasnegyzet % 3 == 0 or harmasnegyzet**0.5 % 1 == 0):
            harmasnegyzet = int(input("Rossz szám! Írj be egy hárommal osztható vagy négyzet számot: "))
        print("A nyereményed egy Gucci táska!")
    else:
        while not(harmasnegyzet % 3 == 0):
            harmasnegyzet = int(input("Rossz szám! Írj be egy hárommal osztható vagy négyzet számot: "))
        print("A nyereményed egy Gucci táska!")

# Kérj be valós 3 számot, amíg szerkeszthető háromszög oldalait nem kapjuk!
def feladat_7():
    a = int(input("Szám 1: "))
    b = int(input("Szám 2: "))
    c = int(input("Szám 3: "))
    while not((a + b > c) and (a + c > b) and (b + c > a) and a > 0 and b > 0 and c > 0):
        a = int(input("Rossz! Szám 1: "))
        b = int(input("Rossz! Szám 2: "))
        c = int(input("Rossz! Szám 3: "))
    print("Jó számokat adtál meg!")

# Addig kérjünk be szöveget, amíg legalább 3 karakterest nem írnak be. Majd írjuk ki a szót csupa nagy betűvel!*
def feladat_8():
    szoveg = input("3 karakteres szó: ")
    while not(szoveg.isalpha() and len(szoveg) == 3):
        szoveg = input("Rossz! 3 karakteres szó: ")
    print(szoveg.upper())

# Addig kérjünk be szöveget, amíg csupa kis betűs és 4 karakteres szót nem adnak meg!*
def feladat_9():
    szoveg = input("4 karakteres, kisbetűs szó: ")
    while not (szoveg.isalpha() and len(szoveg) == 4 and szoveg.islower()):
        szoveg = input("Rossz! 4 karakteres, kisbetűs szó: ")
    print("A nyereményed egy Gucci táska!")

# Kérj a felhasználótól bizonyos számú egész számot (0-tól eltérő értékeket), és írasd ki az átlagukat 2 tizedes jegy pontossággal (a felhasználó úgy jelzi, hogy többet nem kíván beírni, hogy azt írja: 0)!
def feladat_10():
    szam = int(input("Írj be egy számot (ha végzetél írd be, hogy 0): "))
    osszeg = szam
    db = 0
    atlag = 0
    while not(szam == 0):
        szam = int(input("Írj be egy számot (ha végzetél írd be, hogy 0): "))
        osszeg += szam
        db += 1
    atlag = osszeg / db
    print(f"A számok átlaga: {atlag:.2f}")

# A fenti feladatot írd meg úgy, hogy csak pozitív számot fogadjon el (ha negatív, addig kérjen új számot, ameddig pozitív nem lesz), illetve ha 0-t ír, akkor legyen vége a bemeneteknek!
def feladat_11():
    szam = int(input("Írj be egy számot (ha végzetél írd be, hogy 0): "))
    atlag = 0
    while not (szam >= 0):
        szam = int(input("Rossz szám! Írj be egy számot (ha végzetél írd be, hogy 0): "))
    osszeg = szam
    db = 0
    while not (szam == 0):
        szam = int(input("Írj be egy számot (ha végzetél írd be, hogy 0): "))
        while not (szam >= 0):
            szam = int(input("Rossz szám! Írj be egy számot (ha végzetél írd be, hogy 0): "))
        osszeg += szam
        db += 1
    atlag = osszeg / db
    print(f"A számok átlaga: {atlag:.2f}")