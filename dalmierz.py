#Laboratorium 1-dalmierze

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt

#listy danych z plikow
odleglosc = []
czas = []
ultrad = []
laserowy = []
temperatura = []

#odczyt pierwszego pliku
with open("dalmierz_pomiar_1.txt", "r") as pomiary:
    lines = pomiary.readlines()
lines.pop(0)
lines.pop(0)
for i in lines:
    odleglosc.append(float(i.split("\t")[1]))
    czas.append(float(i.split("\t")[2]))
    laserowy.append(float(i.split("\t")[3]))
    ultrad.append(float(i.split("\t")[4]))
    temperatura.append(float(i.split("\t")[6].rstrip("\n")))

#odczyt drugiego pliku
with open("dalmierz_pomiar_2.txt", "r") as pomiary:
    lines = pomiary.readlines()
lines.pop(0)
lines.pop(0)
for i in lines:
    odleglosc.insert(0,float(i.split("\t")[1]))
    czas.insert(0,float(i.split("\t")[2]))
    laserowy.insert(0,float(i.split("\t")[3]))
    ultrad.insert(0,float(i.split("\t")[4]))
    temperatura.insert(0,float(i.split("\t")[6].rstrip("\n")))

#regresja liniowa dla dalmierza ultradzwiekowego
x = np.array(ultrad).reshape((-1,1))
y = np.array(czas)
model = LinearRegression()
model.fit(x, y)
slope = float(model.coef_)
intercept = float(model.intercept_)
abline_values = [model.coef_ * i + model.intercept_ for i in x]

#wykres ultra dzwiekowego -pomiarow oraz prostej regresji
plt.plot(x, abline_values, '-', label="y={0:.4f}x + {1:.4f}".format(slope, intercept)) #prosta regresji
plt.plot(ultrad, czas, "ro")                                                           #pomiary
plt.grid(True)
plt.xlabel("Położenie obiektu[mm]")
plt.ylabel("Czas impulsu[ms]")
plt.title("Wykres Czas impulsu(Położenie obiektu)")
plt.legend(fontsize=13)
plt.show()

#niepewnosc czulosci(slope)
rmse = sqrt(mean_squared_error(y, abline_values))

#zakres
n = len(odleglosc)
FS = odleglosc[n-1]-odleglosc[0]

#rozdzielczosc(z dokumentacji)
rozdzielczosc = 30

#obszar martwy(zwykresu)
martwy = 20

#dokladnosc
blad = []
for i in range(0, n-1):
    blad.append((ultrad[i])/(odleglosc[i]))
dokladnosc = max(blad)

#przesuniecie
offset = intercept

#predkosc (bez pierwszych 3 punktow z obszaru martwego)
s = 0
for i in range(3, n-1):
    s = s + ((2*ultrad[i])/czas[i])
vsrednia = s/(n-3)

#wyswietlenie obliczonych parametrow
print("Czulosc: ",slope)
print("Niepewnosc czulosci: ",rmse )
print("Zakres: ", FS)
print("Rozdzielczosc: ", rozdzielczosc )
print("Obszar martwy: ", martwy)
print("Dokladnosc: ", dokladnosc)
print("Przesuniecie: ", offset)
print("Predkosc: ", vsrednia)


#regresja liniowa dla dalmierza laserowego
x = np.array(odleglosc).reshape((-1,1))
y = np.array(laserowy)
model = LinearRegression()
model.fit(x, y)
slope = float(model.coef_)
intercept = float(model.intercept_)
abline_values = [model.coef_ * i + model.intercept_ for i in x]

#wykres dalmierza laserowego wraz z prosta regresji
plt.plot(x, abline_values, '-', label="y={0:.4f}x + {1:.4f}".format(slope, intercept)) #prosta regresji
plt.plot(odleglosc, laserowy, "ro")                                                    #pomiary
plt.xlabel("Położenie obiektu[mm]")
plt.ylabel("Odległość zmierzona[mm]")
plt.title("Wykres Odległość zmierzona(Położenie obiektu)")
plt.grid(True)
plt.legend(fontsize=13)
plt.show()

#niepewnosc
rmse = sqrt(mean_squared_error(y, abline_values))

#wyswietlenie obliczonych parametrow
print("Czulosc: ",slope)
print("Niepewnosc: ",rmse )