#! /usr/bin/env python 
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port Tarama Aracina Hos Geldiniz :)

1) Hizli Tarama
2) Servis ve Version Bilgisi
3) Isletim Sistemi Bilgisi


""")
islemno = raw_input("Islem Numarasini Giriniz: ")

if(islemno=="1"):
                hedefip = raw_input("Hedef Ip Giriniz: ")
                
                os.system("nmap " + hedefip)
elif(islemno=="2"): 
                hedefip = raw_input("Hedef Ip Giriniz: ")
                
                os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"): 
                hedefip = raw_input("Hedef Ip Giriniz: ")
                
                os.system("nmap -0 " + hedefip)
else:
                print("Hatali Secim.!")
