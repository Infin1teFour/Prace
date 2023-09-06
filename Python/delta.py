import math as m

#Zmienne
a = int(input("Podaj wartość a: "))
b = int(input("Podaj wartość b: "))
c = int(input("Podaj wartość c: "))

#Obliczenie Delty
delta = b**2 - (4*(a*c))

#Sprawdzanie ilości rozwiązań
print("Delta wynosi ",delta)

if delta > 0:
    print("Ta funkcja ma 2 rozwiązania")
    print("Te rozwiązania wynoszą: \n",(-b - m.sqrt(delta))/(2*a), "\n", (-b + m.sqrt(delta))/(2*a))
elif delta == 0:
    print("Ta funkcja ma 1 rozwiązanie")
    print("To rozwiązanie wynosi: \n",(-b)/(2*a))
else:
    print("Ta funkcja nie ma rozwiązań")