#Zadanie Wyznacznik macierzy
import random
import numpy as np

random.seed()
A = np.random.randn(3, 3)

detA = np.linalg.det(A)

print("Macierz A:")
print(A)
print("detA =", detA)
