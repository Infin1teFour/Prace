import math
class figury:
    #Trójkąty
    def obwod_rownoboczny(a):
        return 3*a
    def pole_rownoboczny(a, h):
        return (a/2) * h

    def obwod_roznoboczny(a, b, c):
        return a+b+c
    def pole_roznoboczny(a, h):
        return (a/2) * h

    #Czworokaty
    def obwod_kwadrat(a):
        return 4*a
    def pole_kwadrat(a):
        return a**2

    def obwod_romb(a):
        return 4*a
    def pole_romb(a, h):
        return a*h

    def obwod_deltoid(a,b):
        return (2*a)+(2*b)
    def pole_deltoid(d1, d2):
        return (d1/2)*d2

    def obwod_prostokat(a,b):
        return 2(a+b)
    def pole_prostokat(a,b):
        return a*b

    def obwod_rownoleglobok(a,b):
        return 2(a+b)
    def pole_rownoleglobok(a,h):
        return a*h

    def obwod_trapez(a,b,c,d):
        return a+b+c+d
    def pole_trapez(a,b,h):
        return ((a+b)/2)*h