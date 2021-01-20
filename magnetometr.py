#Laboratorium 2-magnetometr
import csv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from scipy import optimize
import math

#listy danych z pliku "magneto_data_X.csv"
current_x = []
magx_x = []
magy_x = []
magz_x = []
#listy danych z pliku "magneto_data_Y.csv"
current_y = []
magx_y = []
magy_y = []
magz_y = []
#listy danych z pliku "magneto_data_Z.csv"
current_z = []
magx_z = []
magy_z = []
magz_z = []

#odczyt pierwszego pliku "magneto_data_X.csv"
with open("magneto_data_X.csv", "r") as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        current_x.append(float(row[0]))
        magx_x.append(float(row[1]))
        magy_x.append(float(row[2]))
        magz_x.append(float(row[3]))

#odczyt drugiego pliku "magneto_data_Y.csv"
with open("magneto_data_Y.csv", "r") as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        current_y.append(float(row[0]))
        magx_y.append(float(row[1]))
        magy_y.append(float(row[2]))
        magz_y.append(float(row[3]))
        
#odczyt trzeciego pliku "magneto_data_Z.csv"
with open("magneto_data_Z.csv", "r") as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        current_z.append(float(row[0]))
        magx_z.append(float(row[1]))
        magy_z.append(float(row[2]))
        magz_z.append(float(row[3]))

def func(x, a, b):              #definicja liniowej funkcji do fitowania
    return a * x + b


#wykres dla magneto_data_X
plt.plot(current_x, magx_x,  "ro")
plt.ylabel("Odczyt X[LSB]")
plt.xlabel("Prąd[A]")
plt.title("Wykres magx(I)")
plt.grid(True)
plt.show()

#wykres dla magneto_data_Y
plt.plot(current_y, magy_y, "ro")
plt.ylabel("Odczyt Y[LSB]")
plt.xlabel("Prąd[A]")
plt.title("Wykres magy(I)")
plt.grid(True)
plt.show()

#wykres dla magneto_data_Z
plt.plot(current_z, magz_z, "ro")
plt.ylabel("Odczyt Z[LSB]")
plt.xlabel("Prąd[A]")
plt.title("Wykres magz(I)")
plt.grid(True)
plt.show()

#Fitowanie dla magneto_data_X
linear_current_x = []
linear_magx_x = []
for i in range(0, len(current_x)-44, 1):
    linear_current_x.append(float(current_x[i]))
    linear_magx_x.append(float(magx_x[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_x, linear_magx_x)          #fit_params
a = float(fit_params[0])
b = float(fit_params[1])

plt.plot(linear_current_x, linear_magx_x, 'ro')
plt.plot(linear_current_x, func(np.array(linear_current_x), a, b), 'r', label="y={0:.4f}x + {1:.4f}".format(a, b))
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt X[LSB]")
plt.title("Fitowanie w liniowym zakresie")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()

# Fitowanie dla magneto_data_Y
linear_current_y = []
linear_magy_y = []
for i in range(0, len(current_y) - 50, 1):
    linear_current_y.append(float(current_y[i]))
    linear_magy_y.append(float(magy_y[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_y, linear_magy_y)  # fit_params
a = float(fit_params[0])
b = float(fit_params[1])

plt.plot(linear_current_y, linear_magy_y, 'ro')
plt.plot(linear_current_y, func(np.array(linear_current_y), a, b), 'r', label="y={0:.4f}x + {1:.4f}".format(a, b))
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt Y[LSB]")
plt.title("Fitowanie w liniowym zakresie")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()

# Fitowanie dla magneto_data_Z
linear_current_z = []
linear_magz_z = []
for i in range(0, len(current_z) - 43, 1):
    linear_current_z.append(float(current_z[i]))
    linear_magz_z.append(float(magz_z[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_z, linear_magz_z)  # fit_params
a = float(fit_params[0])
b = float(fit_params[1])

plt.plot(linear_current_z, linear_magz_z, 'ro')
plt.plot(linear_current_z, func(np.array(linear_current_z), a, b), 'r', label="y={0:.4f}x + {1:.4f}".format(a, b))
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt Z[LSB]")
plt.title("Fitowanie w liniowym zakresie")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()

# cross-talk wzdłuż osi X
s_y = 0
s_z = 0
for i in range(0, len(magx_x)-44, 1):
    s_y = s_y + (magy_x[i]/magx_x[i])
    s_z = s_z + (magz_x[i]/magx_x[i])
crossy_x = s_y/(len(magx_x)-43)             #dla Y
crossz_x = s_z/(len(magx_x)-43)             #dla Z

print("Wzdłuż osi X:")
print("Cross-talk dla Y: "+str(crossy_x))
print("Cross-talk dla Z: "+str(crossz_x))
print("Średnia: "+str((crossy_x+crossz_x)/2))

# cross-talk wzdłuż osi Y
s_x = 0
s_z = 0
for i in range(0, len(magy_y)-50, 1):
    s_x = s_x + (magx_y[i]/magy_y[i])
    s_z = s_z + (magz_y[i]/magy_y[i])
crossx_y = s_x/(len(magy_y)-49)             #dla X
crossz_y = s_z/(len(magy_y)-49)             #dla Z

print("Wzdłuż osi Y:")
print("Cross-talk dla X: "+str(crossx_y))
print("Cross-talk dla Z: "+str(crossz_y))
print("Srednia: "+str((crossx_y+crossz_y)/2))

# cross-talk wzdłuż osi Z
s_x = 0
s_y = 0
for i in range(0, len(magz_z)-43, 1):
    s_x = s_x + (magx_z[i]/magz_z[i])
    s_y = s_y + (magy_z[i]/magz_z[i])
crossx_z = s_x/(len(magz_z)-42)             #dla X
crossy_z = s_y/(len(magz_z)-42)             #dla Y

print("Wzdłuż osi Z:")
print("Cross-talk dla X: "+str(crossx_z))
print("Cross-talk dla Y: "+str(crossy_z))
print("Średnia: "+str((crossx_z+crossy_z)/2))



#listy danych z pliku "magneto_data_histereza.csv"
current_histereza = []
magx_histereza = []
magy_histereza = []
magz_histereza = []

#odczyt pliku "magneto_data_histereza.csv"
with open("magneto_data_histereza.csv", "r") as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        current_histereza.append(float(row[0]))
        magx_histereza.append(float(row[1]))
        magy_histereza.append(float(row[2]))
        magz_histereza.append(float(row[3]))

##################  Fitowanie dla histerezy X   #######################
linear_current_histerezax_h = []
linear_current_histerezax_l = []
linear_magx_histereza_h = []
linear_magx_histereza_l = []

#segregacja danych dla "dolnej" funkcji
for i in range(170, 129, -1):
    linear_current_histerezax_l.append(float(current_histereza[i]))
    linear_magx_histereza_l.append(float(magx_histereza[i]))

#segregacja danych dla "górnej" funkcji
for i in range(280, 299, 1):
    linear_current_histerezax_h.append(float(current_histereza[i]))
    linear_magx_histereza_h.append(float(magx_histereza[i]))
for i in range(0, 21, 1):
    linear_current_histerezax_h.append(float(current_histereza[i]))
    linear_magx_histereza_h.append(float(magx_histereza[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_histerezax_l, linear_magx_histereza_l)  # fit_params
al = float(fit_params[0])
bl = float(fit_params[1])
fit_params, covariance_matrix = curve_fit(func, linear_current_histerezax_h, linear_magx_histereza_h)  # fit_params
ah = float(fit_params[0])
bh = float(fit_params[1])

plt.plot(linear_current_histerezax_l, linear_magx_histereza_l, 'ro')
plt.plot(linear_current_histerezax_l, func(np.array(linear_current_histerezax_l), al, bl), 'g', label="y_l={0:.4f}x + {1:.4f}".format(al, bl))
plt.plot(linear_current_histerezax_h, linear_magx_histereza_h, 'ro')
plt.plot(linear_current_histerezax_h, func(np.array(linear_current_histerezax_h), ah, bh), 'b', label="y_h={0:.4f}x + {1:.4f}".format(ah, bh))
plt.plot
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt X[LSB]")
plt.title("Fitowanie histerezy X")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()

##################  Fitowanie dla histerezy Y   #######################
linear_current_histerezay_h = []
linear_current_histerezay_l = []
linear_magy_histereza_h = []
linear_magy_histereza_l = []

#segregacja danych dla "dolnej" funkcji
for i in range(215, 84, -1):
    linear_current_histerezay_l.append(float(current_histereza[i]))
    linear_magy_histereza_l.append(float(magy_histereza[i]))

#segregacja danych dla "górnej" funkcji
for i in range(235, 299, 1):
    linear_current_histerezay_h.append(float(current_histereza[i]))
    linear_magy_histereza_h.append(float(magy_histereza[i]))
for i in range(0, 66, 1):
    linear_current_histerezay_h.append(float(current_histereza[i]))
    linear_magy_histereza_h.append(float(magy_histereza[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_histerezay_l, linear_magy_histereza_l)  # fit_params
al = float(fit_params[0])
bl = float(fit_params[1])
fit_params, covariance_matrix = curve_fit(func, linear_current_histerezay_h, linear_magy_histereza_h)  # fit_params
ah = float(fit_params[0])
bh = float(fit_params[1])

plt.plot(linear_current_histerezay_l, linear_magy_histereza_l, 'ro')
plt.plot(linear_current_histerezay_l, func(np.array(linear_current_histerezay_l), al, bl), 'g', label="y_l={0:.4f}x + {1:.4f}".format(al, bl))
plt.plot(linear_current_histerezay_h, linear_magy_histereza_h, 'ro')
plt.plot(linear_current_histerezay_h, func(np.array(linear_current_histerezay_h), ah, bh), 'b', label="y_h={0:.4f}x + {1:.4f}".format(ah, bh))
plt.plot
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt Y[LSB]")
plt.title("Fitowanie histerezy Y")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()

##################  Fitowanie dla histerezy Z   #######################
linear_current_histerezaz_h = []
linear_current_histerezaz_l = []
linear_magz_histereza_h = []
linear_magz_histereza_l = []

#segregacja danych dla "dolnej" funkcji
for i in range(170, 129, -1):
    linear_current_histerezaz_l.append(float(current_histereza[i]))
    linear_magz_histereza_l.append(float(magz_histereza[i]))

#segregacja danych dla "górnej" funkcji
for i in range(280, 299, 1):
    linear_current_histerezaz_h.append(float(current_histereza[i]))
    linear_magz_histereza_h.append(float(magz_histereza[i]))
for i in range(0, 21, 1):
    linear_current_histerezaz_h.append(float(current_histereza[i]))
    linear_magz_histereza_h.append(float(magz_histereza[i]))

fit_params, covariance_matrix = curve_fit(func, linear_current_histerezaz_l, linear_magz_histereza_l)  # fit_params
al = float(fit_params[0])
bl = float(fit_params[1])
fit_params, covariance_matrix = curve_fit(func, linear_current_histerezaz_h, linear_magz_histereza_h)  # fit_params
ah = float(fit_params[0])
bh = float(fit_params[1])

plt.plot(linear_current_histerezaz_l, linear_magz_histereza_l, 'ro')
plt.plot(linear_current_histerezaz_l, func(np.array(linear_current_histerezaz_l), al, bl), 'g', label="y_l={0:.4f}x + {1:.4f}".format(al, bl))
plt.plot(linear_current_histerezaz_h, linear_magz_histereza_h, 'ro')
plt.plot(linear_current_histerezaz_h, func(np.array(linear_current_histerezaz_h), ah, bh), 'b', label="y_h={0:.4f}x + {1:.4f}".format(ah, bh))
plt.plot
plt.xlabel("Prąd[A]")
plt.ylabel("Odczyt Z[LSB]")
plt.title("Fitowanie histerezy Z")
plt.legend(fontsize=13)
plt.grid(True)
plt.show()


##################  Fitowanie charakterystyk 1-4   #######################
#listy danych z pliku "charakterystyka1.csv"
angle1 = []
resistance1 = []
#listy danych z pliku "charakterystyka2.csv"
angle2 = []
resistance2 = []
#listy danych z pliku "charakterystyka3.csv"
angle3 = []
resistance3 = []
#listy danych z pliku "charakterystyka4.csv"
h = []
resistance4 = []

#odczyt pliku "charakterystyka1.csv"
with open("charakterystyka1.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        angle1.append(float(i.split(",")[0])*(np.pi/180))
        resistance1.append(float(i.split(",")[1]))

#odczyt pliku "charakterystyka2.csv"
with open("charakterystyka2.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        angle2.append(float(i.split(",")[0])*(np.pi/180))
        resistance2.append(float(i.split(",")[1]))

#odczyt pliku "charakterystyka3.csv"
with open("charakterystyka3.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        angle3.append(float(i.split(",")[0])*(np.pi/180))
        resistance3.append(float(i.split(",")[1]))

#odczyt pliku "charakterystyka4.csv"
with open("charakterystyka4.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        h.append(float(i.split(",")[0])*(np.pi/180))
        resistance4.append(float(i.split(",")[1]))

def function1(x, a, b, c):                                  #funkcja sinus do fitowania
    return a * np.sin(b * (np.pi/180) * x) + c

def function2(x, a, b, c):                                  #funkcja sinc do fitowania
    return a * np.sinc(b * pow(np.pi, 2) * x) + c

#fitowanie charakterystyki 1
fit_params, covariance_matrix = optimize.curve_fit(function1, angle1, resistance1)
plt.plot(angle1, resistance1, "ro")
plt.plot(angle1, function1(np.array(angle1), fit_params[0], fit_params[1], fit_params[2]), 'b', label="y={0:.3f}*sin({1:.3f}*x) + {2:.3f}".format(fit_params[0], fit_params[1] * (np.pi/180), fit_params[2]))
plt.ylabel("Resistance")
plt.xlabel("Angle[rad]")
plt.title("Charakterystyka 1")
plt.grid(True)
plt.legend(fontsize=13)
plt.show()

#fitowanie charakterystyki 2
fit_params, covariance_matrix = optimize.curve_fit(function1, angle2, resistance2)
plt.plot(angle2, resistance2, "ro")
plt.plot(angle2, function1(np.array(angle2), fit_params[0], fit_params[1], fit_params[2]), 'b', label="y={0:.3f}*sin({1:.3f}*x) + {2:.3f}".format(fit_params[0], fit_params[1] * (np.pi/180), fit_params[2]))
plt.ylabel("Resistance")
plt.xlabel("Angle[rad]")
plt.title("Charakterystyka 2")
plt.grid(True)
plt.legend(fontsize=13)
plt.show()


#fitowanie charakterystyki 3
fit_params, covariance_matrix = optimize.curve_fit(function2, angle3, resistance3)
plt.plot(angle3, resistance3, "ro")
plt.plot(angle3, function2(np.array(angle3), fit_params[0], fit_params[1], fit_params[2]), 'b', label="y={0:.3f}*sinc({1:.3f}*x) + {2:.3f}".format(fit_params[0], fit_params[1] * pow(np.pi, 2), fit_params[2]))
plt.ylabel("Resistance")
plt.xlabel("Angle[rad]")
plt.title("Charakterystyka 3")
plt.grid(True)
plt.legend(fontsize=13)
plt.show()


def function3(x, a, b, c, d, e, f, g, h, i):                           #funkcja wielomian 8 stopnia do fitowania
    return a*x*x*x*x*x*x*x*x + b*x*x*x*x*x*x*x + c*x*x*x*x*x*x + d*x*x*x*x*x + e*x*x*x*x + f*x*x*x + g*x*x + h*x + i

#fitowanie charakterystyki 4
h_h = []
resistance4_h = []
h_l = []
resistance4_l = []
for i in range(0, 201, 1):
    h_l.append(h[i])
    resistance4_l.append(resistance4[i])
for i in range(202, 400, 1):
    h_h.append(h[i])
    resistance4_h.append(resistance4[i])

fit_params_h, covariance_matrix = curve_fit(function3, h_h, resistance4_h)
fit_params_l, covariance_matrix = curve_fit(function3, h_l, resistance4_l)

plt.plot(h, resistance4, "ro")
plt.plot(h_l, function3(np.array(h_l), fit_params_l[0], fit_params_l[1], fit_params_l[2], fit_params_l[3], fit_params_l[4], fit_params_l[5], fit_params_l[6], fit_params_l[7], fit_params_l[8]), 'b', label="y_l")
plt.plot(h_h, function3(np.array(h_h), fit_params_h[0], fit_params_h[1], fit_params_h[2], fit_params_h[3], fit_params_h[4], fit_params_h[5], fit_params_h[6], fit_params_h[7], fit_params_h[8]), 'g', label="y_h")
plt.ylabel("Resistance")
plt.xlabel("Inductance[H]")
plt.title("Charakterystyka 4")
plt.grid(True)
plt.legend(fontsize=13)
plt.show()

print("y_l = {0:.1f}*x^8 + {1:.1f}*x^7 + {2:.1f}*x^6 + {3:.1f}*x^5 + {4:.1f}*x^4 + {5:.1f}*x^3 + {6:.1f}*x^2 + {7:.1f}*x + {8:.1f}".format(fit_params_l[0], fit_params_l[1], fit_params_l[2], fit_params_l[3], fit_params_l[4], fit_params_l[5], fit_params_l[6], fit_params_l[7], fit_params_l[8]))
print("y_h = {0:.1f}*x^8 + {1:.1f}*x^7 + {2:.1f}*x^6 + {3:.1f}*x^5 + {4:.1f}*x^4 + {5:.1f}*x^3 + {6:.1f}*x^2 + {7:.1f}*x + {8:.1f}".format(fit_params_h[0], fit_params_h[1], fit_params_h[2], fit_params_h[3], fit_params_h[4], fit_params_h[5], fit_params_h[6], fit_params_h[7], fit_params_h[8]))