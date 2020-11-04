#Zadanie Histogram
import imageio
import matplotlib.pyplot as plt

pic = imageio.imread("picture1.jpg")
RGB = []
R = []
G = []
B = []
RGB_counter = []
R_counter = []
G_counter = []
B_counter = []
color_tones = []

for j in range(0, len(pic[0])):
    for i in range(0, len(pic)):
        R.append(pic[i, j, 0])
        G.append(pic[i, j, 1])
        B.append(pic[i, j, 2])

for i in range(0, len(R)):
    RGB.append(R[i] + G[i] + B[i])

for i in range(0, 255):
    RGB_counter.append(RGB.count(i))
    R_counter.append(R.count(i))
    G_counter.append(G.count(i))
    B_counter.append(B.count(i))
    color_tones.append(i)

plt.title("Histogram")
plt.plot(color_tones, RGB_counter, 'y', label="RGB")
plt.plot(color_tones, R_counter, 'r', label="R")
plt.plot(color_tones, G_counter, 'g', label="G")
plt.plot(color_tones, B_counter, 'b', label="B")
plt.legend(fontsize=10)
plt.grid(True)
plt.show()