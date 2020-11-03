#Zadanie Kalkulator
import math

class Complex:
 def __init__(self, realpart, imagpart):
  self.r = realpart
  self.i = imagpart

 def show_complex(self):
   print("Wynik = ", self.r, " + ", self.i, "i")

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



while(1):
 print("_________Kalkulator liczb zespolonych_________")
 print("| 1.Dodawanie")
 print("| 2.Odjmowanie")
 print("| 3.Mnożenie")
 print("| 4.Sprzężenie")
 print("| 5.Moduł")
 print("| 6.Zakończ")
 n = int(input("Wybierz działanie: "))

 if(n == 1):
  r, i = input('Podaj część rzeczywistą i urojoną pierwszej liczby, oddzielone spacją: ').split()
  z1 = Complex(float(r), float(i))
  r, i = input('Podaj część rzeczywistą i urojoną drugiej liczby, oddzielone spacją: ').split()
  z2 = Complex(float(r), float(i))
  z3 = z1.add(z2)
  z3.show_complex()
 elif(n == 2):
  r, i = input('Podaj część rzeczywistą i urojoną liczby, oddzielone spacją: ').split()
  z1 = Complex(float(r), float(i))
  r, i = input('Podaj część rzeczywistą i urojoną drugiej liczby, oddzielone spacją: ').split()
  z2 = Complex(float(r), float(i))
  z3 = z1.subtract(z2)
  z3.show_complex()
 elif(n == 3):
  r, i = input('Podaj część rzeczywistą i urojoną pierwszej liczby, oddzielone spacją: ').split()
  z1 = Complex(float(r), float(i))
  r, i = input('Podaj część rzeczywistą i urojoną drugiej liczby, oddzielone spacją: ').split()
  z2 = Complex(float(r), float(i))
  z3 = z1.multiplicate(z2)
  z3.show_complex()
 elif(n == 4):
  r, i = input('Podaj część rzeczywistą i urojoną pierwszej liczby, oddzielone spacją: ').split()
  z1 = Complex(float(r), float(i))
  z1.conjugate()
  z1.show_complex()
 elif(n == 5):
  r, i = input('Podaj część rzeczywistą i urojoną pierwszej liczby, oddzielone spacją: ').split()
  z1 = Complex(float(r), float(i))
  print("Wynik = ", z1.module())
 elif(n == 6):
  break