#Zadanie CSV/JSON

position = []
title = []
review = []
mark = []

def show_data(position, title, review, mark):
    for i in range(0, len(position)):
        print("{0}      |       {1}     |       {2}        |       {3}".format(position[i], title[i], review[i], mark[i]))

def delete_row(i):
    del title[i]
    del review[i]
    del mark[i]
    position.pop()

def input_row():
    position.append(str(len(position)))
    title.append(str(input("Podaj tytuł filmu: ")))
    review.append(str(input("Podaj recenzje filmu: ")))
    mark.append(str(input("Podaj ocenę filmu x/10: ")))


### import from file ###
with open("movie_data_base.csv", "r") as file:
    lines = file.readlines()
    for i in lines:
        position.append(i.split(",")[0])
        title.append(i.split(",")[1])
        review.append(i.split(",")[2])
        mark.append(i.split(",")[3].strip("\n"))
file.close()

#### default header ###
position[0] = "Pozycja"
title[0] = "Tytuł"
review[0] = "Recenzja"
mark[0] = "Ocena"

while(1):
    print("\nAktualna baza recenzji filmów:")
    show_data(position, title, review, mark)

    decision = int(input("\nCo chcesz zrobić ?\n1.Usuń wiersz\n2.Wpisz nowy wiersz\n3.Zakończ\n"))
    if (decision == 1):
        show_data(position, title, review, mark)
        i = int(input("\nKtórą pozycje usunąć ?"))
        delete_row(i)
    elif (decision == 2):
        input_row()
    elif (decision == 3):
        break
    else:
        print("Nie ma takiej opcji")


### save to file ###
new_data_row = []
for i in range(0, len(position)):
    new_data_row.append(position[i] + "," + title[i] + "," + review[i] + "," + mark[i])

new_data = "\n".join(new_data_row)

with open("movie_data_base.csv", "w") as file:
    file.write(new_data)
file.close()

