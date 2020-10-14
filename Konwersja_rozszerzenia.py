#Zadanie Konwersja rozszerzenia

###file1, file2, file3, file4 -> dowolne pliki .jpg do konwersji na .png###
from PIL import Image

picture1 = Image.open(r'C:\Users\karol\Desktop\file1.jpg')
picture1.save(r'C:\Users\karol\Desktop\file1_converted.png')

picture2 = Image.open(r'C:\Users\karol\Desktop\file2.jpg')
picture2.save(r'C:\Users\karol\Desktop\file2_converted.png')

picture3 = Image.open(r'C:\Users\karol\Desktop\file3.jpg')
picture3.save(r'C:\Users\karol\Desktop\file3_converted.png')

picture4 = Image.open(r'C:\Users\karol\Desktop\file4.jpg')
picture4.save(r'C:\Users\karol\Desktop\file4_converted.png')
