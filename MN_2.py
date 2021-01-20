import math


E = 5                   #[V]
R1 = 100                #[Ohm]
R2 = 1000               #[Ohm]
R3 = 100                #[Ohm]      ->pierwszy przypadek
#R3 = 0                 #[Ohm]      ->drugi przypadek
Is = 10 ** (-15)        #[A]
Ut = 0.025              #[V]


def funkcja(Ud):
    return (E-((R1*Ud)/R2)-Ud)/(((R1*R3)/R2)+R1+R3)-Is*(math.exp(Ud/Ut)-1)          


def bisekcja(a, b, eps):        
    i = 0
    if funkcja(a) * funkcja(b) > 0:
        print("Rownanie nie ma rozwiazania")
    else:
        while (abs(b-a)/2.0) > eps:
            i = i+1
            X0 = (a+b)/2.0
            if funkcja(X0) == 0:
                return (X0)
            elif funkcja(a) * funkcja(X0) < 0:
                b = X0
            else:
                a = X0
        return (X0)


Ud = bisekcja(0, 1, 0.00000000000001)
id = (E-((R1*Ud)/R2)-Ud)/(((R1*R3)/R2)+R1+R3)
i1 = (Ud+R3*id)/R2
i = i1+id


print("Obliczone prady: ")
print("i1 = ", i1*1000, "[mA]")
print("id = ", id*1000, "[mA]")
print("i = i1 + id = ", i*1000, "[mA]")
