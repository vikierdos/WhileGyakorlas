def feladat_1():
    letszam = float(input("Létszám: "))
    szintido = float(input("Szint idő: "))
    a = 0
    osszeg = 0
    db = 0
    teljesitett = 0
    while letszam > a:
        nev = input("Név: ")
        ido = float(input("Idő: "))
        if ido == 0:
            print("Lesérült")
        elif ido < 0:
            print("Érvénytelen adat!")
        else:
            osszeg += ido
            db += 1
        if ido <= szintido:
            teljesitett += 1
        a += 1
    atlag = osszeg / db
    szazalek = teljesitett*100/letszam
    print(f"{db} személy ért be sérülés nélkül és érvényes adattal.")
    print(f"{szazalek}% személy teljesítette az adott szintet")
    print(f"{atlag} az átlaguk azoknak akik érvényesen beértek")


def feladat_2():
    ertek = 0
