#Zadanie Usuwanie słów

#użyłem swojego przykładowego pliku ponieważ w repozytorium były same angielskojęzyczne a zadanie polega na usuwaniu polskich słów

with open("C:\\Users\\karol\Desktop\\plik_tekstowy.txt", "r") as file:
    text = file.read()
file.close()

new_text = text.replace(" się", "")
new_text = new_text.replace(" i", "")
new_text = new_text.replace(" oraz", "")
new_text = new_text.replace(" nigdy", "")
new_text = new_text.replace(" dlaczego", "")

with open("C:\\Users\\karol\Desktop\\plik_tekstowy_zmodyfikowany.txt", "w") as file:
    file.write(new_text)
file.close()

