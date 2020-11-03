#Zadanie Mnożenie macierzy
import random
import numpy as np

random.seed()
A = np.random.randn(8, 8)
B = np.random.randn(8, 8)
C = np.zeros((8, 8))

for i in range(len(A)):
       for j in range(len(B[0])):
           for k in range(len(B)):
               C[i][j] += A[i][k] * B[k][j]

print("Macierz A =")
print(A)
print("Macierz B =")
print(B)
print("Macierz C = A * B =")
print(C)
