# uklad rownan Ax = B
# macierz A przedstawiamy za pomoca macierzy L oraz U
# nastepnie rozwiazujemy dwa rownania LZ = B oraz UX = Z => skad otrzymujemy macierz X

import scipy
import scipy.linalg

############
# METODA LU
############
A = scipy.array([[0.2425, 0, -0.9701], [0, 0.2425, -0.9701], [-0.2357, -0.2357, -0.9428]])
B = scipy.array([[247], [248], [239]])

print "A: "
print A

print "B: "
print B

print "############"
print "Metoda LU"
print "############"
P, L, U = scipy.linalg.lu(A)

print "P: "
print P

print "L: "
print L

print "U: "
print U

invL = scipy.linalg.inv(L) #macierz odwrotna
print "inv L: "
print invL

invU = scipy.linalg.inv(U)
print "inv U: "
print invU

# Z = L^-1 * B
Z = scipy.dot(invL, B)

print "Z: "
print Z

X = scipy.dot(invU, Z)
print "X: "
print X

a = scipy.array([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
print "#########"
print "Metoda QR"
print "#########"

# a = QR
# R - macierz trojkatna gorna
# Q - Q macierz ortogonalna


Q, R = scipy.linalg.qr(a)

print "Q:"
print Q

print "R:"
print R
