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

 #Main Function
sampah = ["Plastik", "Organik", "Kertas", "Kaleng"]
berat = [1.2, 0.3, 2.2, 1.0]
harga = [3000, 500, 2500, 3500]
                                                                                     
user = ["superuser", "user1", "user2"]
password = ["admin", "abc", "def"]
                                                                                     
login = False 
y = ""
while y !="0"
    print("Program Sistem Informasi Bank Sampah")
    login = input("Login : ")
    if login == "Exit" or login == "Exit":
		y = "0"
        print("Program Shutting Down...")
    else:
        passw = input("Pass : ")
                                                                                     
        clearscreen()
        for i in range(len(user)):
            if login == user[i] and passwd == password[i]:
                if i == 0:
                    login = True 
                    adminMenu()
                else:
                    login = True 
                    adminMenu()             
            else:
                login == False
                                                                                     
         if login == False:
             print("User/Password not exist or match.")
