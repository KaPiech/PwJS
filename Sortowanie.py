#Zadanie Sortowanie
import random

random_numbers_list = []
numbers_list = []

random.seed()
for i in range(0, 50, 1):
    {
        random_numbers_list.append(random.random())
    }
print("Wylosowane liczby: ", random_numbers_list)

for i in range(49, 0, -1):
    {
       numbers_list.append(sorted(random_numbers_list)[i])
    }

for i in range(0, len(random_numbers_list)-1, 1):
    for j in range(len(random_numbers_list)-1):
            if random_numbers_list[j] < random_numbers_list[j+1]:
                    k = random_numbers_list[j+1]
                    random_numbers_list[j+1] = random_numbers_list[j]
                    random_numbers_list[j] = k

print("Posortowane malejaco liczby: ", random_numbers_list)
print("Sprawdzenie sortowania: ", numbers_list)