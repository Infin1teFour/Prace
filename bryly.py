import math as m

class Bryly:
    #Walec
    def Pole_boczne_walca(r,h):
        return 2*m.pi()*r*h
    def Pole_podstawy_walca(r,h):
        return (2*m.pi())*(r*(r+h))
    def Objętość_Walca(r,h):
        return m.pi()*(r**2)*h
    
    #Stożek
    def Pole_boczne_stożka(r,l):
        return m.pi()*r*l
    def Pole_podstawy_stożka(r,l):
        return m.pi()*r(r+l)
    def Objętość_stożka(r,l):
        return (m.pi()/3)*(r**2)*h

    #Kula
    def Pole_kuli(r):
        return 4*m.pi()*(r**2)
    def Objętość_kuli(r):
        return m.pi()*(4/3)*(r**3)
