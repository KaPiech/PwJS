#Zadanie 5
import matplotlib.pyplot as plt
import numpy as np

#listy danych
data = []
data_conv = []
cursors = []

#funkcja odczytująca dane z pliku
def read_file():
    with open("ADC_data.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            data.append(i)

#funkcja konwertująca hex na float
def conversion():
    for i in range(0, len(data)-1, 1):
        data_conv.append(float.fromhex(data[i]))

#klasa kursora wraz z metodami
class Cursor(object):
    def __init__(self, k, x, y):
        self.ax = k
        self.ly = k.axvline(color='b', alpha=0.4)
        self.marker, = k.plot([0], [0], marker="o", color="b")
        self.x = x
        self.y = y
        self.txt = k.text(0.7, 0.9, '')

    def move(self, event):                      #przesuwanie myszy
        if not event.inaxes: return
        x, y = event.xdata, event.ydata
        n = np.searchsorted(self.x, [x])[0]
        x = self.x[n]
        y = self.y[n]
        self.ly.set_xdata(x)
        self.marker.set_data([x], [y])
        self.txt.set_text('x=%1.4f, y=%1.4f' % (x, y))
        self.txt.set_position((x, y))
        self.ax.figure.canvas.draw_idle()

    def press(self, event):                     #kliknięcie myszy
        if (len(cursors) == 0):
            print('Pozycja kursora1: x1=', event.xdata, '   y1=', event.ydata)
            cursors.append(event.xdata)
            cursors.append(event.ydata)
        elif(len(cursors) == 2):
            print('Pozycja kursora1: x2=', event.xdata, '   y2=', event.ydata)
            cursors.append(event.xdata)
            cursors.append(event.ydata)
        elif  (len(cursors) == 4):
            print('Różnica kursorów: x1-x2=', cursors[0]-cursors[2], '   y1-y2=', cursors[1]-cursors[3])
            cursors.pop()
            cursors.pop()
            cursors.pop()
            cursors.pop()
            print('')

##########  program główny  ##########
read_file()
conversion()
time = np.arange(0.0, 1, 1/len(data_conv))      #generowanie danych dla osi czasu

fig, ax = plt.subplots()
cursor = Cursor(ax, time, data_conv)

#reakcje na mysz
cid = plt.connect('motion_notify_event', cursor.move)
cid = plt.connect('button_press_event', cursor.press)

#tworzenie charakterystyki
plt.plot(time, data_conv, 'r')
plt.title("Wykres danych ADC_data")
plt.xlabel("t")
plt.ylabel("Amplituda")
plt.grid()
plt.xlim(0, 0.005)      #ograniczony zakres aby można było wygodnie zaobserwować sinusoide i użyć kursorów
plt.show()


#####   obliczanie FFT #####
spectrum = np.fft.fft(data_conv)
frequency = np.fft.fftfreq(len(time), len(data_conv))

for i in range(0, len(frequency), 1):
    frequency[i] = frequency[i] + 1/len(data_conv)

#tworzenie charakterystyki amplitudowej
plt.plot(frequency, abs(spectrum), 'r')
plt.title("FFT")
plt.ylabel("Amplituda")
plt.xlabel("f")
plt.show()