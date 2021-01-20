#Laboratorium 3-akcelerometr
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
"""
########################## punkt 1 ##########################
#listy danych z pliku "dane_animacja_v2.csv"
time_d = []
roll_d = []
pitch_d = []
#odczyt danych z pliku
with open("dane_animacja_v2.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        time_d.append(float(i.split(",")[0]))
        roll_d.append(float(i.split(",")[1]))
        pitch_d.append(float(i.split(",")[2]))

############### wizualizacja 3D ################
def get_params(time):
    i = int(time-1)
    Pitch_deg = pitch_d[i]
    Roll_deg = roll_d[i]
    Yaw_deg = 0
    x = 0
    y = 0
    z = 0
    return Yaw_deg, Pitch_deg, Roll_deg, x, y, z

def plot_IMU(time):
    Yaw_deg, Pitch_deg, Roll_deg, X, Y, Z = get_params(time)
    Yaw = Yaw_deg*np.pi/180
    Pitch = Pitch_deg*np.pi/180
    Roll = Roll_deg*np.pi/180

    fig.clf()
    ax = fig.add_subplot(111, projection='3d', title='Karol Piech '+'\n' +'Pitch= '+str(Pitch)+' [rad]'+'\n'+'Roll= '+str(Roll)+' [rad]')

    ##### układ danych #####
    euler_Rx = np.array([[1, 0, 0], [0, np.cos(Roll), -np.sin(Roll)], [0, np.sin(Roll), np.cos(Roll)]])
    euler_Ry = np.array([[np.cos(Pitch), 0, np.sin(Pitch)], [0, 1, 0], [-np.sin(Pitch), 0, np.cos(Pitch)]])
    euler_Rz = np.array([[np.cos(Yaw), -np.sin(Yaw), 0], [np.sin(Yaw), np.cos(Yaw), 0], [0, 0, 1]])
    euler_Rzyx = np.dot(np.dot(euler_Rz, euler_Ry), euler_Rx)

    x_s = np.dot(euler_Rzyx, np.array([[1, 0, 0]]).T)
    y_s = np.dot(euler_Rzyx, np.array([[0, 1, 0]]).T)
    z_s = np.dot(euler_Rzyx, np.array([[0, 0, 1]]).T)
    #strzałki
    ax.quiver(X, Y, Z, x_s[0], x_s[1], x_s[2], pivot='tail', color='green')
    ax.quiver(X, Y, Z, y_s[0], y_s[1], y_s[2], pivot='tail', color='red')
    ax.quiver(X, Y, Z, z_s[0], z_s[1], z_s[2], pivot='tail', color='blue')
    #podpisy strzałek
    ax.text(float(x_s[0]), float(x_s[1]), float(x_s[2]), "Xs", color="green", size="15")
    ax.text(float(y_s[0]), float(y_s[1]), float(y_s[2]), "Ys", color="red", size="15")
    ax.text(float(z_s[0]), float(z_s[1]), float(z_s[2]), "Zs", color="blue", size="15")

    ##### układ odniesienia #####
    #strzałki
    ax.quiver(-2, -2, -2, 1, 0, 0, pivot='tail', color='green')
    ax.quiver(-2, -2, -2, 0, 1, 0, pivot='tail', color='red')
    ax.quiver(-2, -2, -2, 0, 0, 1, pivot='tail', color='blue')
    # podpisy strzałek
    ax.text(-1, -2, -2, "Xo", color="green", size="15")
    ax.text(-2, -1, -2, "Yo", color="red", size="15")
    ax.text(-2, -2, -1, "Zo", color="blue", size="15")

    #wykres
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.xticks(np.linspace(-2, 2, num=5))
    plt.yticks(np.linspace(-2, 2, num=5))
    ax.set_zticks(np.linspace(-1, 1, num=5))
    ax.view_init(30, -115)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ani = FuncAnimation(fig, plot_IMU, frames=np.linspace(1, 998, 998), interval=100)
#ani.save('animacja.gif', writer="imagemagick", fps=5)      #zapis gifa

plt.show()
"""



from scipy import signal
from scipy import optimize

########################## punkt 2 ##########################
#listy danych z pliku "dane_sprezyna.csv"
t = []
z_acc = []
#wczytywanie danych z pliku
with open("dane_sprezyna.csv", "r") as data:
    lines = data.readlines()
    lines.pop(0)
    for i in lines:
        t.append(float(i.split(",")[0]))
        z_acc.append(float(i.split(",")[1])/16384)

######### punkt  2a ##########
z_acc_mean = np.mean(z_acc)
for i in range(0, len(z_acc)):
    z_acc[i] = z_acc[i] - z_acc_mean

plt.plot(t, z_acc, 'or', markersize=1)
plt.title("a_x(t)")
plt.xlabel("t[s]")
plt.ylabel("a_x[m/s^2]")
plt.show()

######### punkt  2b ##########
def integral(t, z):
    result = []
    result.append(0)
    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        result.append(result[i-1] + z[i]*dt)
    return result

T_pr = t[1] - t[0]
f_pr = 1 / T_pr
v = integral(t, z_acc)

for i in range(0, len(v)-1, 1):
    v[i] = v[i] * 9.81
filtr_v = signal.butter(4, 0.8, 'highpass', output='sos', fs=f_pr)
v_filter = signal.sosfilt(filtr_v, v)

plt.plot(t, v_filter, 'og', markersize=1, label='Po filtracji')
plt.plot(t, v, 'or', markersize=1, label='Bez filtracji')
plt.title("V(t)")
plt.xlabel("t[s]")
plt.ylabel("V[m/s]")
plt.legend(fontsize=11)
plt.show()

######### punkt  2c ##########
filtr_s = signal.butter(10, 0.8, 'highpass', output='sos', fs=f_pr)
s_filter = signal.sosfilt(filtr_s, integral(t, v_filter))

plt.plot(t, s_filter, 'og', markersize=1, label='Po filtracji')
plt.plot(t, integral(t, v_filter), 'or', markersize=1, label='Bez filtracji')
plt.title("Położenie(t)")
plt.xlabel("t[s]")
plt.ylabel("Położenie[m]")
plt.legend(fontsize=12)
plt.show()

######### punkt  2d ##########
spectrum = np.fft.fft(s_filter)
frequency = np.fft.fftfreq(len(t), T_pr)

for i in range(0, len(frequency), 1):
    frequency[i] = frequency[i] + f_pr

plt.plot(frequency, abs(spectrum), 'r')
plt.title("FFT dla funkcji Położenie(t)")
plt.ylabel("Amplituda")
plt.xlabel("f[Hz]")
plt.show()

######### punkt  2e ##########
def function(x, a, b, c, d, e):                                  #funkcja sinus tłumiony do fitowania
    return a * np.sin(b * 100 * x + c) * np.exp(-d * 100 * x) + e

fit_params, covariance_matrix = optimize.curve_fit(function, t, s_filter)
plt.plot(t, s_filter, 'og', markersize=1, label='Położenie(t) po filtracji')
plt.plot(t, function(np.array(t), fit_params[0], fit_params[1], fit_params[2], fit_params[3], fit_params[4]), 'b', label="y={0:.3f} * sin(-{1:.3f}*x +{2:.3f}) * exp(-{3:.3f}*x) + {4:.3f}".format(fit_params[0], fit_params[1]*100, fit_params[2], fit_params[3]*100, fit_params[4]))
plt.ylabel("Położenie[m]")
plt.xlabel("t[s]")
plt.title("Fitowanie funkcji Położenie(t)")
plt.legend(fontsize=10)
plt.show()


