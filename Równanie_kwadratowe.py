#Zadanie Rownanie kwadratowe
import math

a = float(input("Podaj wspolczynnik a = "))
b = float(input("Podaj wspolczynnik b = "))
c = float(input("Podaj wspolczynnik c = "))

print("Wzor podanej funkcji: f(x) = ", a, "x^2 +", b, "x +", c)

delta = ((b*b) - (4*a*c))

if(delta < 0):
    {
        print("Brak rozwiazan")
    }
elif(delta == 0):
    {
        print("Jedno rozwiazanie x =", ((-b)/(2*a)))
    }
elif(delta > 0):
    {
        print("Dwa rozwiazania x1 =", ((-b-math.sqrt(delta))/2), "  x2 =", ((-b+math.sqrt(delta))/2))
    }