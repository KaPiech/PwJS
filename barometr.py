#Laboratorium 4-barometr
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

########################## punkt 1 ##########################
#listy danych z pliku "cisnienie_wysokosc.csv"
time = []
pressure = []
#odczyt danych z pliku
with open("cisnienie_wysokosc.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        time.append(float(i.split(",")[0]))
        pressure.append(float(i.split(",")[1]))

########## Punkt 1 ##########
plt.plot(time, pressure, 'or', markersize=1)
plt.title("Wykres P(t)")
plt.xlabel("t[s]")
plt.ylabel("P[Pa]")
plt.grid()
plt.show()

#obliczenie liczby pięter
p_hi = 0
p_low = 0
for i in range(946, 998, 1):
    p_hi = p_hi + pressure[i]
p_hi = p_hi/52

for i in range(509, 655, 1):
    p_low = p_low + pressure[i]
p_low = p_low/146

x = ((p_hi - p_low)/10)/3
print("Ilosc pieter: ", x)

#obliczenie wysokości bezwzględnej
t = ((17 - 32) / 1.8) + 273                            #17 stopni farenheita zamienione na kelwiny
h = (-(8.31 * t) / (9.81 * 0.029)) * np.log(p_hi/101000)
print("Wysokosc bezwzgledna: ", h)

########################## punkt 2 ##########################
#listy danych z pliku "cisnienie_temperatura.csv"
time_temp = []
pressure_temp = []
temp_temp = []
#odczyt danych z pliku
with open("cisnienie_temperatura.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        time_temp.append(float(i.split(",")[0]))
        pressure_temp.append(float(i.split(",")[1]))
        temp_temp.append(float(i.split(",")[2]))

#schładzanie
temp_cool = []
time_cool = []
for i in range(0, 4272, 1):
    temp_cool.append(temp_temp[i])
    time_cool.append(time_temp[i])

plt.plot(time_cool, temp_cool, 'or', markersize=2)
plt.title("Wykres T(t) - schładzanie")
plt.xlabel("t[s]")
plt.ylabel("T[C]")
plt.ylim(-15, 30)
plt.grid()
plt.show()

#ogrzewanie
temp_heat = []
time_heat = []
for i in range(4273, len(time_temp)-1, 1):
    temp_heat.append(temp_temp[i])
    time_heat.append(time_temp[i])

plt.plot(time_heat, temp_heat, 'or', markersize=2)
plt.title("Wykres T(t) - ogrzewanie")
plt.xlabel("t[s]")
plt.ylabel("T[C]")
plt.grid()
plt.ylim(-15, 30)
plt.show()


##########  fitowanie charakterystyk    ##########
def function(x, a, b, c):                               #funkcja do fitowania
    return a * np.log(x + b) + c

def function2(x, a, b, c):                               #funkcja do fitowania
    return a * np.exp(-b*x) + c

fit_params, covariance_matrix = optimize.curve_fit(function2, time_cool, temp_cool)
plt.plot(time_cool, function2(np.array(time_cool), fit_params[0], fit_params[1], fit_params[2]), 'b', label="y={0:.3f} * exp({1:.3f} * x) + {2:.3f}".format(fit_params[0], -fit_params[1], fit_params[2]))
plt.plot(time_cool, temp_cool, 'or', markersize=2)
plt.title("Fitowanie T(t) - schładzanie")
plt.xlabel("t[s]")
plt.ylabel("T[C]")
plt.ylim(-15, 30)
plt.grid()
plt.legend()
plt.show()

fit_params, covariance_matrix = optimize.curve_fit(function, time_heat, temp_heat)
plt.plot(time_heat, function(np.array(time_heat), fit_params[0], fit_params[1], fit_params[2]), 'b', label="y={0:.3f} * log(x + {1:.3f}) + {2:.3f}".format(fit_params[0], fit_params[1], fit_params[2]))
plt.plot(time_heat, temp_heat, 'or', markersize=2)
plt.title("Fitowanie T(t) - ogrzewanie")
plt.xlabel("t[s]")
plt.ylabel("T[C]")
plt.ylim(-15, 30)
plt.grid()
plt.legend()
plt.show()


#sprawdzenie czy spełnione jest równanie Clapeyrona
plt.plot(temp_temp, pressure_temp, 'or', markersize=1)
plt.title("Wykres P(T)")
plt.xlabel("T[C]")
plt.ylabel("P[Pa]")
plt.grid()
plt.show()
