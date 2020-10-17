#Zadanie Podmienianie słów

#użyłem swojego przykładowego pliku ponieważ w repozytorium były same angielskojęzyczne a zadanie polega na usuwaniu polskich słów

######################################
dictionary = {}
dictionary["i"] = "oraz"
dictionary["oraz"] = "i"
dictionary["nigdy"] = "prawie nigdy"
dictionary["dlaczego"] = "czemu"
######################################

new_words_lines = []
new_text_line = []

with open("C:\\Users\\karol\Desktop\\plik_tekstowy.txt", "r") as file:
    for line in file:
        words_line = line.split()
        for i in range(0, len(words_line)):
            if words_line[i] in dictionary:
                words_line[i] = dictionary[words_line[i]]
        new_words_lines.append(words_line)

file.close()

for i in range(0, len(new_words_lines)):
    new_text_line.append(' '.join(new_words_lines[i]))

new_text = "\n".join(new_text_line)

with open("C:\\Users\\karol\Desktop\\plik_tekstowy_zmodyfikowany.txt", "w") as file:
    file.write(new_text)
file.close()
