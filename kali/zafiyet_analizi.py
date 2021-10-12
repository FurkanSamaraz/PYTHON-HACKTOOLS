#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAAFIYET ANALIZI")
print("""


""")

hedefip = raw_input("Hedef Ip Giriniz: ")
os.system("nikto -h " + hedefip)
