from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=500, szobaszam=szobaszam)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(ar=800, szobaszam=szobaszam)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szobaszam, datum):
        szobaszam = int(szobaszam)
        for szoba in self.szalloda.szobak:
            if szoba.szobaszam == szobaszam:
                foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
                if foglalas_datum < datetime.now():
                    print("A foglalás dátuma nem lehet múltbeli!")
                    return None
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum.date() == foglalas_datum.date():
                        print("Ez a szoba már foglalt ezen a napon!")
                        return None
                self.foglalasok.append(Foglalas(szoba, foglalas_datum))
                print("Sikeres foglalás!")
                return szoba.ar  # Visszaadja az árat a sikeres foglalás esetén
        print("Nincs ilyen szoba!")
        return None

    def lemondas(self, szobaszam, datum):
        szobaszam = int(szobaszam)
        foglalas_datum = datetime.strptime(datum, "%Y-%m-%d")
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum.date() == foglalas_datum.date():
                self.foglalasok.remove(foglalas)
                print("Foglalás sikeresen törölve!")
                return
        print("Nincs ilyen foglalás!")

    def listaz(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum.strftime('%Y-%m-%d')}")
        else:
            print("Nincs foglalás.")

# Szálloda, szobák és foglalások létrehozása
hotel = Szalloda("Teszt Hotel")
hotel.add_szoba(EgyagyasSzoba(szobaszam=11))
hotel.add_szoba(EgyagyasSzoba(szobaszam=12))
hotel.add_szoba(KetagyasSzoba(szobaszam=20))
hotel.add_szoba(KetagyasSzoba(szobaszam=22))
hotel.add_szoba(KetagyasSzoba(szobaszam=23))

foglalas_kezelo = FoglalasKezelo(hotel)
foglalas_kezelo.foglalas(szobaszam=11, datum="2024-05-15")
foglalas_kezelo.foglalas(szobaszam=20, datum="2024-05-20")
foglalas_kezelo.foglalas(szobaszam=23, datum="2024-05-25")
foglalas_kezelo.foglalas(szobaszam=11, datum="2024-05-18")
foglalas_kezelo.foglalas(szobaszam=20, datum="2024-06-13")
foglalas_kezelo.listaz()

# Felhasználói interfész
while True:
    print("\nVálassz egy műveletet:")
    print("1 - Foglalás")
    print("2 - Lemondás")
    print("3 - Foglalások listázása")
    print("4 - Kilépés")
    valasztas = input("Művelet kiválasztása: ")

    if valasztas == "1":
        szobaszam = input("Kérem a foglalandó szoba számát: ")
        datum = input("Kérem a foglalás dátumát (YYYY-MM-DD formátumban): ")
        foglalas_ar = foglalas_kezelo.foglalas(szobaszam, datum)
        if foglalas_ar is not None:
            print(f"A foglalás ára: {foglalas_ar} Ft")
    elif valasztas == "2":
        szobaszam = input("Kérem a lemondandó foglalás szoba számát: ")
        datum = input("Kérem a lemondandó foglalás dátumát (YYYY-MM-DD formátumban): ")
        foglalas_kezelo.lemondas(szobaszam, datum)
    elif valasztas == "3":
        foglalas_kezelo.listaz()
    elif valasztas == "4":
        break
    else:
        print("Érvénytelen művelet!")
