#Zadanie Struktura katalogu
import os

def listing(catalog):
    print(catalog)

    list_of_files = os.listdir(catalog)

    for element in list_of_files:
        full_path = os.path.join(catalog, element)

        if os.path.isdir(full_path):
            listing(full_path)
        else:
            print(full_path)



path = input(print("Podaj sciezke katalogu od ktorego zaczac :"))

print("Znalezione pliki w drzewie katalogów: ")

listing(path)
