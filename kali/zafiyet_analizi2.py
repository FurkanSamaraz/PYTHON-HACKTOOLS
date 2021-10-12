#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet ZAFIYET ANALIZI")
print("""
Zafiyet Analizi - 2 Aracina Hosgeldiniz.
""")
os.system("lynis audit system")
print("""
Aciklama Bolumu
""")
