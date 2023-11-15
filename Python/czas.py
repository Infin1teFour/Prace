import time

rok, miesiac, dzien, godzina, minuta, sekunda, dzienTygodnia, dniRoku, isDst = time.localtime()
epoch = time.time()

dni = {
    0: "poniedziałek",
    1: "wtorek",
    2: "środa",
    3: "czwartek",
    4: "piątek",
    5: "sobota",
    6: "niedziela"
}

miesiace = {
    1: "Styczeń",
    2: "Luty",
    3: "Marzec",
    4: "Kwiecień",
    5: "Maj",
    6: "Czerwiec",
    7: "Lipiec",
    8: "Sierpień",
    9: "Wrzesień",
    10: "Październik",
    11: "Listopad",
    12: "Grudzień"
    
}

print("Dzisiaj jest "+dni[dzienTygodnia]+
" roku pańskiego "+str(rok)+
". Miesiąc to "+miesiace[miesiac]+
". Do końca roku zostało "+str(365-dniRoku)+
" dni. Od początku roku mineło "+str(dniRoku)+
" dni. Od daty 1.1.1970 minęło "+str(round(epoch))+
" sekund.")