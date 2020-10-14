#Zadanie Ilość plików
import os

list_of_files = list(os.listdir(r'/dev'))
print("Ilosc plikow w katalogu /dev = ", len(list_of_files))
