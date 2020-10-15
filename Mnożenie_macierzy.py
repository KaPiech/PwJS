#Zadanie Mnożenie macierzy
import random
import numpy as np

random.seed()
A = np.random.randn(8, 8)
B = np.random.randn(8, 8)

C = A.dot(B)

print("Macierz A:")
print(A)
print("Macierz B:")
print(B)
print("Macierz C = A * B")
print(C)