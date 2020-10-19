#Zadanie Liczby zespolone
import math

class Complex:
 def __init__(self, realpart, imagpart):
  self.r = realpart
  self.i = imagpart

 def show_complex(self):
  print(self.r, " + ", self.i, "i")

 def conjugate(self):
  self.i = -self.i

 def module(self):
   return math.sqrt((self.r * self.r) + (self.i * self.i))

 def add(self, y):
   return Complex(self.r + y.r, self.i + y.i)

 def subtract(self, y):
  return Complex(self.r - y.r, self.i - y.i)

 def multiplicate(self, y):
  return Complex(((self.r * y.r) - (self.i - y.i)), ((self.r * y.i) + (self.i * y.r)))


### przykład użycia ###
x = Complex(2.0, -2.0)
y = Complex(3, 5)

z1 = x.add(y)
z2 = x.subtract(y)
z3 = x.multiplicate(y)

z1.show_complex()
z2.show_complex()
z3.show_complex()
