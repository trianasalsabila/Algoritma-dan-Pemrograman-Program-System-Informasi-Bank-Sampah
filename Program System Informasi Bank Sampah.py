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

def bukuTabungan():
    print("Daftar Tabungan : ")
    no = 1
    for i in range(len(sampah)):
        print(str(no)+". "+sampah[i]+":"+str(berat[i])+"kg \t = Rp"+ str(berat[i]*harga[i]))
        no += 1
    print()
    
def tabung():
    y = False
    tabung = input("Input Sampah yang ditabung : ")
    
    for i in range(len(sampah)):
        if tabung == sampah[i]:
            berattabung = float(input("Input Berat Sampah"))
            berattabung = berattabung + berat[i]
            print("berat tabung: "+ str(beratabung) +" + "+ str(berat[i]) +" = "+ str(berattabung)
            berat[i] = berattabung
            y = True
    if y == False:
        print("Sampah belum ditambahkan.")
    print()
                                                                                     
 def adminMenu():
    x = ""
    while x !="0":
        print("Program Sistem Informasi Bank Sampah")
        print("[1] Tampilkan Buku Tabungan Nasabah")
        print("[2] Tambahkan Tabungan Nasabah")
        print("[0] Log Out")
        print()
                                                                                     
        x = input("Opt : ")
        clearscreen()
                
        if x=="1":
            BukuTabungan()
        elif x=="2":
            Tabungan()  
        elif x=="0":
            print("Logging Out...")
            print()
        else:
            print("Option not found.")
            print()

 
