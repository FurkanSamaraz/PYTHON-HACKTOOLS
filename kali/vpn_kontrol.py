#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VPN KONTROL ")
print("""
VPN Kontrol Aracina Hosgeldiniz.

""")

hedefip = raw_input("Hedef Ip Giriniz: ")
os.system("ike-scan " + hedefip)

