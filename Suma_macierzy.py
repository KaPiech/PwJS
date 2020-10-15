#Zadanie Suma macierzy
import random
import numpy as np

random.seed()
A = np.random.randn(128, 128)
B = np.random.randn(128, 128)

C = A + B

print("Macierz A:")
print(A)
print("Macierz B:")
print(B)
print("Macierz C = A + B")
print(C)

