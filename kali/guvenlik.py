#!/usr/bin/evn python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet GUVENLIK DUVARI TESPIT")
print("""
Guvenlik Duvari Tespit Aracina Hosgeldiniz...
""")

site= raw_input("Hedef Adres: ")
os.system("wafw00f " + site)

istek = raw_input("Yeni Arama Yapmak Ister Misiniz ? (y/n): ")

if(istek=="y"):
		os.system("python guvenlik.py ")

elif(istek=="n"):
		print("Gorusuruz..")

else:
		print("yes var no var ?!!")


