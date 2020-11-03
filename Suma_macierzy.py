#Zadanie Suma macierzy
import random
import numpy as np

random.seed()
A = np.random.randn(128, 128)
B = np.random.randn(128, 128)
C = np.zeros((128, 128))

for i in range(0, 128):
    for j in range(0, 128):
        C[i][j] = A[i][j] + B[i][j]

print("Macierz A:")
print(A)
print("Macierz B:")
print(B)
print("Macierz C = A + B")
print(C)

