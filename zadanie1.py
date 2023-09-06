#Pobierz imie, nazwisko, wiek
#dł. imienia + nazwiska > 10 to napisz długie
#>18 lat piwo, <18 lat mleko


#Pobierz zmienne
imie = input("Podaj swoje imie: ")
nazwisko = input("Podaj swoje nazwisko: ")
wiek = int(input("Podaj swój wiek: "))

#Sprawdzenia długości imiona i nazwiska
if len(imie)+ len(nazwisko) > 10:
    print("Długie")

#Sprawdzenie wieku
if wiek >= 18:
    print("Piwo")
else:
    print("mleko")