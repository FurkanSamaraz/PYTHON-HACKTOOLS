#!/usr/bin/env python
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet MAC DEGISTIRME ")
print("""
Mac Degistirme Aracina Hosgeldiniz.


1) MAC Adresi Random Belirle
2) MAC Adresi elle Belirle
3) MAC Adresi Orijinale Dondur

""")

islemno = raw_input("Islem Numarasi Giriniz: ")

if(islemno=="1"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -r eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Adresi Elle Belirlendi.")
		
if(islemno=="2"):
		macadres = raw_input("Yeni MAC Adresi Giriniz: ")
		os.system("ifconfig eth0 down")
		os.system("macchanger --mac " + macadres + " eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Adresi Elle Belirlendi.")
		
if(islemno=="3"):
		os.system("ifconfig eth0 down")
		os.system("macchanger -p eth0")
		os.system("ifconfig eth0 up")
		print("\033[92mYeni MAC Orijinale Donduruldu.")
		
else:
		print("Hatali Tuslama Yaptiniz.")
		os.system("python mac.py")

	
