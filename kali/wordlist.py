#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI")
print("""
Worldlist Aracina Hosgeldiniz.
""")

minimum = raw_input("Minimum Karakter Sayisi Giriniz: ")
maximum = raw_input("Maximum Karakter Sayisi Giriniz: ")
karekter = raw_input("Istediginiz Karakter Sayisi: ")


os.system("crunch " + minimum + " " + maximum + " " + karekter)
print("Basari ile Tamamlandi..")
