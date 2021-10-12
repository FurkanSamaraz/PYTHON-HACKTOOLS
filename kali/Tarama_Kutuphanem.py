#! /usr/bin/env python 
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
						Tarama Aracina Hos Geldiniz :)

-PORT TARAMA ARACI
1) Hizli Tarama
2) Servis ve Version Bilgisi
3) Isletim Sistemi Bilgisi

-ZAFIYET ANALIZI ARACI
4) Zafiyet Analizi

-GUVENLIK DUVARI TESPIT ARACI
5) Guvenlik Duvari Tespit

-EXPLOIT TARAMA ARACI
6)Exploit Tarama

-ROOTKIT TARAMA ARACI
7) Rootkit Tarama

-KABA KUVVET TARAMA ARACI
8) FTP 
9) SSH
10) Telnet
11) HTTP
12) SMB
13) ROP
14) SIP
15) Redis
16) VNC
17) PostgreSQL
18) MySQL

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
                os.system("nmap -O " + hedefip)
                
elif(islemno=="4"):           
                hedefip = raw_input("Hedef Ip Giriniz: ")
		os.system("nikto -h " + hedefip)
		
elif(islemno=="5"):    	
		site= raw_input("Hedef Adres: ")
		os.system("wafw00f " + site)

elif(islemno=="6"):    	
                anahtarkelime = raw_input("Anahtar Kelime Giriniz: ")
		os.system("searchsloit " + anahtarkelime)
                
elif(islemno=="7"):
		os.system("chkrootkit")              
                
elif(islemno=="8"):
      		os.system("nrack -p 21 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
      
elif(islemno=="9"):          
                os.system("ncrack -p 22 -u " + kullaniciadi + " -P " + sifre + " " + hedefip)
                
                
else:
                print("Hatali Secim.!")
                
                
                
istek = raw_input("Yeni Arama Yapmak Ister Misiniz ? (y/n): ")

if(istek=="y"):
		os.system("python Tarama_Kutuphanem.py ")

elif(istek=="n"):
		print("Gorusuruz..")

else:
		print("yes var no var ?!!")


