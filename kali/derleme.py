#!/usr/bin/env python
import os
import py_compile
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet DERLEME ")
print("""
Derleme Aracina Hosgeldiniz.

""")

derle = raw_input("Program Ismini Giriniz: ")

py_compile.compile(derle)



