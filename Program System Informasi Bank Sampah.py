# Algoritma-dan-Pemrograman-Program-System-Informasi-Bank-Sampah
#program Triana Salsabila
#Program Bank Sampah

import os

def clearscreen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
        
def mainMenu():
    x = ""
    while x != "0":
        print("Program Sistem Informasi Bank Sampah")
        print("[1] Tampilkan Buku Tabungan")
        print("[0] Logout")
        print()
        
        x = input("Opt : ")
        clearscreen()
        
        if x == "1":
            BukuTabungan()
            
        elif x == "0":
            print("Logging Out...")
            print()
            
        elif x == "2":
            tabung()
            
        elif x == "Admin":
            admin()
         
        else:
            clearscreen("Option not found.")
            print()
