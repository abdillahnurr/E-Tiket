import csv
import time
import os
akun = {"idad" : "admin", 
        "pwad" : "admin",
        "idu" : {0 :"user" ,1 :"user1",2 : "user2",3: "user3",4 : "user4"},
        "pwu" : {0 :"user" ,1 :"user1",2 : "user2",3: "user3",4 : "user4"},
        "saldo" : {0 : 5000000, 1 : 7500000, 2 : 5000000,3 : 6000000, 4 : 5500000},
        "nama" :{0 : "Abdillah",1 : "Irwansyah",2 : "Agnestia",3 : "Fahreza",4 : "Ridho"},
        "nomor":{0 : 6285247566970, 1 : 6287886185821, 2 : 6285262648170, 3 : 6281350272464, 4 : 6282153759702},
        "email" :{0: "abdillahnurr12@gmail.com",1 :"irwnsyh0812@gmail.com",2:"agnestia930@gmail.com",3: "fahrezamf77@gmail.com",4:"ridhofahriza1203@gmail.com"},
        "riwayat" :{0: [], 1 :[], 2 : [], 3 :[],4 :[]
                    }
        }

def kota():
    print("Select a City")
    print("Keberangkatan \t Kedatangan")
    print("▶ Samarinda  \t ▶ Samarinda")
    print("▶ Balikpapan \t ▶ Balikpapan")
    print("▶ Berau      \t ▶ Berau")
    print("▶ Surabaya   \t ▶ Surabaya")

def date():
    from time import sleep
    import datetime
    waktu = datetime.datetime.now()
    print("Anda masuk pada : ")
    sleep(0.5)
    jam = int(waktu.strftime("%H"))
    mnt = int(waktu.strftime("%M"))
    dtk = int(waktu.strftime("%S"))
    day = waktu.day
    month = waktu.month
    year = waktu.year
    
    print(day,"/",month,"/",year)
    print(jam,":",mnt,":",dtk)
    global tahun
    try:
        tahun = int(input ("Masukkan tahun              : "))
        while tahun < 2020:
            print ("Masukkan tahun yang benar")
            tahun = int(input ("Masukkan tahun : "))
    except ValueError:
        print ("Masukkan tahun yang benar")
        tahun = int(input ("Masukkan tahun : "))
        while tahun < 2020:
            print ("Masukkan tahun yang benar")
            tahun = int(input ("Masukkan tahun : "))
        
    if tahun == year:
        global bulan
        try:
            bulan = int(input("Masukkan Bulan (1-12)       : "))
            while bulan not in range(1,13) or bulan < month:
                print("Masukkan bulan yang sesuai")
                bulan = int(input("Masukkan Bulan (1-12): "))
        except ValueError:
            print("Masukkan bulan yang sesuai")
            bulan = int(input("Masukkan Bulan (1-12): "))
        
        if bulan == month :
            if int(bulan) == 1:   
                global tanggal
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            elif int(bulan) == 2 :
                try:
                    tanggal = int(input("Masukkan tanggal (1-28)     : "))
                    while tanggal not in range(1,28) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-28)     : "))  
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-28)     : "))  
            elif int(bulan) ==3 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            elif int(bulan) == 4 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 5 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 6 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 7 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 8 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) ==  9 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 10 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 11  :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)    : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)    : "))
            elif int(bulan) == 12 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) or tanggal < day:
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
        elif bulan > month :
            if int(bulan) == 1:   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            elif int(bulan) == 2 :
                try:
                    tanggal = int(input("Masukkan tanggal (1-28)     : "))
                    while tanggal not in range(1,28):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-28)     : "))  
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-28)     : "))  
            elif int(bulan) ==3 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            elif int(bulan) == 4 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 5 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 6 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 7 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32):
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 8 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) ==  9 :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
            elif int(bulan) == 10 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
            elif int(bulan) == 11  :
                try: 
                    tanggal = int(input("Masukkan tanggal (1-30)     : "))
                    while tanggal not in range(1,31) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-30)    : ")) 
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)    : "))
            elif int(bulan) == 12 :   
                try:
                    tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                    while tanggal not in range(1,32) :
                        print("Masukkan tanggal yang sesuai")
                        tanggal = int(input("Masukkan tanggal (1-31)     : "))   
                except ValueError:
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))
    elif tahun > year:
        try:
            bulan = int(input("Masukkan Bulan (1-12)       : "))
            while bulan not in range(1,13) :
                print("Masukkan bulan yang sesuai")
                bulan = int(input("Masukkan Bulan (1-12): "))
        except ValueError:
            print("Masukkan bulan yang sesuai")
            bulan = int(input("Masukkan Bulan (1-12): "))
        if int(bulan) == 1:   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))   
        elif int(bulan) == 2 :
            try:
                tanggal = int(input("Masukkan tanggal (1-28)     : "))
                while tanggal not in range(1,28):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-28)     : "))  
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-28)     : "))  
        elif int(bulan) ==3 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))   
        elif int(bulan) == 4 :
            try: 
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
                while tanggal not in range(1,31):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
        elif int(bulan) == 5 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))
        elif int(bulan) == 6 :
            try: 
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
                while tanggal not in range(1,31) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
        elif int(bulan) == 7 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32):
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))
        elif int(bulan) == 8 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))
        elif int(bulan) ==  9 :
            try: 
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
                while tanggal not in range(1,31) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)     : ")) 
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
        elif int(bulan) == 10 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))
        elif int(bulan) == 11  :
            try: 
                tanggal = int(input("Masukkan tanggal (1-30)     : "))
                while tanggal not in range(1,31) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-30)    : ")) 
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-30)    : "))
        elif int(bulan) == 12 :   
            try:
                tanggal = int(input("Masukkan tanggal (1-31)     : ")) 
                while tanggal not in range(1,32) :
                    print("Masukkan tanggal yang sesuai")
                    tanggal = int(input("Masukkan tanggal (1-31)     : "))   
            except ValueError:
                print("Masukkan tanggal yang sesuai")
                tanggal = int(input("Masukkan tanggal (1-31)     : "))

    
def jumlahpenumpang(i):
    global penumpang
    try:
        penumpang = int(input("Jumlah Penumpang     : "))
    except ValueError:
        print("\nTolong masukkan jumlah penumpang yang sesuai")
        penumpang = int(input("Jumlah Penumpang     : "))

def balikpapan_berau():
    flights = []
    with open("balikpapan_berau.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def balikpapan_samarinda():
    flights = []
    with open("balikpapan_samarinda.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)

def balikpapan_surabaya():
    flights = []
    with open("balikpapan_surabaya.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")    
        
def berau_balikpapan():
    flights = []
    with open("berau_balikpapan.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def berau_samarinda():
    flights = []
    with open("berau_samarinda.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def berau_surabaya():
    flights = []
    with open("berau_surabaya.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def samarinda_balikpapan():
    flights = []
    with open("samarinda_balikpapan.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def samarinda_berau():
    flights = []
    with open("samarinda_berau.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def samarinda_surabaya():
    flights = []
    with open("samarinda_surabaya.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)
    
def surabaya_balikpapan():
    flights = []
    with open("surabaya_balikpapan.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)

def surabaya_berau():
    flights = []
    with open("surabaya_berau.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)

def surabaya_samarinda():
    flights = []
    with open("surabaya_samarinda.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            flights.append(row)
    print("KODE \t AIRLINES \t\t WAKTU \t\t\t HARGA")
    print("=" * 45)
    for data in flights:
        print(f"{data['KODE']} \t {data['AIRLINES']} \t {data['WAKTU']} \t {data['HARGA']}")
    print("=" * 45)

def pesan(i):
    
    print("Ditambahkan ke Pemesanan")
    asuransi_perjalanan = input("Asuransi Perjalanan Rp 37.000/orang? (ya/tidak) : ")
    while asuransi_perjalanan not in ["ya","tidak"]:
        print("Masukkan data yang sesuai")
        asuransi_perjalanan = input("Asuransi Perjalanan Rp 37.000/orang? (ya/tidak) : ")
    tiket = penumpang
    print("")
    
    global asuransi
    if asuransi_perjalanan == "ya":
        asuransi = 37000
    elif asuransi_perjalanan == "tidak":
        asuransi = 0
    else:
        print ("Silakan coba lagi")


    global totalharga
    totalharga = penumpang * (int(flights[pilih]['HARGA']) + asuransi)
    global totalharga2
    totalharga2 = (tiket * int(flights[pilih]['HARGA']))
    global total_asuransi
    total_asuransi = (tiket * asuransi)

def totalHarga(i): 
    print("Total Harga Asli         : Rp ", totalharga2)
    print("Asuransi                 : Rp ", total_asuransi)
    print("Harga yang Anda Bayar    : Rp ", totalharga)

      
def dtpenumpang(i):
    print("\nDetail Penumpang")
    global datapenumpang
    datapenumpang =[]
    i = 1
    while i <= penumpang:
        dtpenumpang = {}
        print("Penumpang ", i)
              
        title = input("Title (Mr/Mrs/Ms) : ")
        while title not in ['Mr', 'Mrs', 'Ms']:
            print("Silakan pilih Title penumpang")
            title = input("Title (Mr/Mrs/Ms) : ")
              
        name  = input("Nama              : ")
        while name == "":
            print("Silakan masukkan nama penumpang")
            name  = input("Nama              : ")              
              
        dtpenumpang['Name'] = name
        dtpenumpang['Title'] = title
        datapenumpang.append(dtpenumpang)
        i += 1
            
def dtTraveller(i):
    c = 0
    while c < penumpang:
        dt = datapenumpang[c]
        c += 1
        print(f"Penumpang {c} : ", dt['Title'], dt['Name'])
def pembayaran(i):
    if akun["saldo"][i] < totalharga :
        print("Mohon maaf saldo anda tidak cukup")
        input("Tekan enter untuk lanjut >>>")
        time.sleep(2)
        user(i)
    else :
        print("Total yang harus anda bayar adalah Rp ",totalharga)
        print("Total saldo anda saat ini Rp ",akun["saldo"][i])
        bayar = input("Anda yakin ingin melakukan pembayaran (ya/tidak) :")
        if bayar == "ya" :
            akun["saldo"][i] -= totalharga
            print("Pembayaran anda sedang diproses")
            time.sleep(4)
            print("Saldo anda tersisa Rp ",akun["saldo"][i])
        else : 
            user(i)
             
def flight_detail(i):
    print("\n============  FLIGHT DETAILS  ============")
    print("Harap pastikan bahwa semua informasi \nyang tertulis di bawah ini benar")
    print("")
    print(flights[pilih]['AIRLINES'])
    global y
    y = "{}/{}/{}". format(tanggal, bulan, tahun)
    print("🛫", dari, "\t ", y)
    print(" | ", flights[pilih]['WAKTU'][0:5])
    print(" | ")
    print(" | ")
    print("🛬", ke)
    print("   ", flights[pilih]['WAKTU'][8:13])
    print("")
    print("DETAIL KONTAK")
    print("Nama lengkap     : ", akun["nama"][i])
    print("Nomor handphone : ", akun["nomor"][i])
    print("Email         : ", akun["email"][i])
    print("\nDetail Penumpang")
    dtTraveller(i)
    print("\nDETAIL HARGA")
    totalHarga(i)
    print("Sisa saldo anda sebanyak   : Rp ",akun["saldo"][i])
    print("")
    print("Kami akan mengirimkan konfirmasi pemesanan Anda ke detail kontak di atas, \ yang juga akan digunakan untuk tujuan pengembalian dana atau penjadwalan ulang.")
    
        

def menu_awal(i):    
 
    print("\n==================================")
    print(" TRAVELOKE 🛫 BOOK FLIGHT TICKET ")
    print("==================================")
    print("")
        
    kota()
    global dari          
    dari = input("Keberangkatan      : ")
    while dari not in ['Berau', 'Balikpapan', 'Samarinda', 'Surabaya']:
        print("Masukkan kota keberangkatan")
        dari = input("Keberangkatan      :")
    global ke          
    ke = input("Kedatangan          : ")
    while ke not in ['Berau', 'Balikpapan', 'Samarinda', 'Surabaya']:
        print("Masukkan kota tujuan")
        ke = input("Kedatangan        : ")       
    if dari != ke :          
        date()
                      
        jumlahpenumpang(i)
        
        
        os.system("cls")
        
        print("Mencari semua penerbangan yang tersedia ...")
        time.sleep(4)
        
        os.system("cls")
        
        global flights
        global pilih
        if dari not in ['Berau', 'Balikpapan', 'Samarinda', 'Surabaya']:
            print("")
            print("Penerbangan tidak tersedia")
            
                
        elif ke not in ['Berau', 'Balikpapan', 'Samarinda', 'Surabaya']:
            print("")
            print("Penerbangan tidak tersedia")
            
            
                
            
        elif dari == "Balikpapan" and ke == "Berau":
            balikpapan_berau()
            f = open('balikpapan_berau.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
                
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
                    
        elif dari == "Balikpapan" and ke == "Samarinda":
            balikpapan_samarinda()
            f = open('balikpapan_samarinda.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
            
        elif dari == "Balikpapan" and ke == "Surabaya":
            balikpapan_surabaya()
            f = open('balikpapan_surabaya.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
                    
        elif dari == "Berau" and ke == "Balikpapan":
            berau_balikpapan()
            f = open('berau_balikpapan.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
                      
        elif dari == "Berau" and ke == "Samarinda":
            berau_samarinda()
            f = open ('berau_samarinda.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
            
        elif dari == "Berau" and ke == "Surabaya":
            berau_surabaya()
            f = open ('berau_surabaya.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
            
        elif dari == "Samarinda" and ke == "Balikpapan":
            samarinda_balikpapan()
            f = open ('samarinda_balikpapan.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
                    
        elif dari == "Samarinda" and ke == "Berau":
            samarinda_berau()
            f = open ('samarinda_berau.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
        elif dari == "Samarinda" and ke == "Surabaya":
            samarinda_surabaya()
            f = open('samarinda_surabaya.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
                      
        elif dari == "Surabaya" and ke == "Balikpapan":
            surabaya_balikpapan()
            f = open('surabaya_balikpapan.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
            
        elif dari == "Surabaya" and ke == "Berau":
            surabaya_berau()
            f = open('surabaya_berau.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
        
        elif dari == "Surabaya" and ke == "Samarinda":
            surabaya_samarinda()
            f = open('surabaya_samarinda.csv', 'r')
            reader = csv.reader(f)
            flights = {}
            for row in reader:
                flights[row[0]] = {'AIRLINES':row[1],'WAKTU':row[2],'HARGA':row[3]}
            pilih = input("\nPilih Penerbangan : ")
            if pilih in flights:
                print("Airline : ", flights[pilih]['AIRLINES'])
                print("Waktu   : ", flights[pilih]['WAKTU'])
                print("Harga   : ", flights[pilih]['HARGA'])
            else:
                print("Penerbangan tidak tersedia")
                time.sleep(0.5)
                print("Silahkan input kembali")
                time.sleep(0.5)
                menu_awal(i)
                
        else :
            print("")
            print("Penerbangan tidak tersedia")
            time.sleep(0.5)
            print("Silahkan input kembali")
            time.sleep(0.5)
            menu_awal(i)
            
        pesan(i)
        totalHarga(i)
        pembayaran(i)
        dtpenumpang(i)
        print("Tunggu sebentar. Data Anda sedang diproses")
        time.sleep(4)
        os.system("cls")
        flight_detail(i)
        akun["riwayat"][i].append(datapenumpang)
        akun["riwayat"][i].append(flights[pilih]['AIRLINES'])
        akun["riwayat"][i].append(y)
        akun["riwayat"][i].append(flights[pilih]['WAKTU'])     
        input("Tekan enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        user(i)
 
def cekdata():
    print("Data apa yang ingin anda cek")
    print("1. ID Login ")
    print("2. Passw0rd Login")
    print("3. Saldo User")
    print("4. Daftar nama")
    print("5. Daftar Telepon")
    print("6. Daftar email")
    try :
        pilih = int(input("Pilih Menu yang ingin anda cek : "))
        while pilih not in range (1,7):
            print("Pilihan tidak tersedia")
            pilih = int(input("Masukkan kembali pilihan anda : "))
    except ValueError :
        pilih = int(input("Pilih Menu yang ingin anda cek : "))
        while pilih not in range (1,7):
            print("Pilihan tidak tersedia")
            pilih = int(input("Masukkan kembali pilihan anda : "))
    if pilih == 1:
        print("Berikut data ID user :")
        for i in akun["idu"].keys():
            print(f"{i}.",akun["idu"][i])
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
    elif pilih == 2 :
        for i in akun["pwu"].keys():
            print(f"{i}.",akun["pwu"][i])
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
    elif pilih == 3 :
        for i in akun["saldo"].keys():
            print(f"{i}.",akun["saldo"][i])
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
    elif pilih == 4 :
        for i in akun["nama"].keys():
            print(f"{i}.",akun["nama"][i])
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
    elif pilih == 5 :
        
        for i in akun["nomor"].keys():
            x = str(akun["nomor"][i])

                                  
            if x[0] == "8":
                print(f"{i}.","62"+str(akun["nomor"][i]))
                continue
            else :
                print(f"{i}.",akun["nomor"][i]) 
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
    elif pilih == 6 :
        for i in akun["email"].keys():
            print(f"{i}.",akun["email"][i])
        input("Enter untuk lanjut >>>")
        time.sleep(2)
        os.system("cls")
        admin()
        
def hapusdata():
    print("Pilih ID yang ingin anda hapus")
    for i in akun["idu"].keys():
        print(f"{i}.",akun["idu"][i])
    print("Note : Jika menghapus ID maka semua data akan terhapus juga")
    try :
        pilih = int(input("Pilih ID        :"))
        while pilih not in akun["idu"].keys():
            print("Masukkan pilihan yang sesuai")
            pilih = int(input("Pilih ID        :"))
    except ValueError:
        print("Masukkan pilihan yang sesuai")
        pilih = int(input("Pilih ID        :"))
    for i in akun["idu"].keys():
        
        if pilih == i :

            akun["idu"].pop(i)
            akun["pwu"].pop(i)
            akun["saldo"].pop(i)
            akun["nama"].pop(i)
            akun["nomor"].pop(i)
            akun["email"].pop(i)
            akun["riwayat"].pop(i)
        
            print("Data berhasil di hapus")
            break
    
        
        
    input("Enter untuk lanjut >>>")
    time.sleep(2)
    os.system("cls")
    admin()
        
def datapenerbangan():
    print("")
    for i in akun["riwayat"].keys():
        while len(akun["riwayat"][i]) < 1:
            print(f"{i}.", "Data tidak ditemukan")
            break
        for j in range(0,len(akun["riwayat"][i])):
            print(f"{i}.", akun["riwayat"][i][j])
    input("Tekan enter untuk kembali ke menu >>>")
    time.sleep(1)
    os.system("cls")
    admin()
    
def editakun():
    print("Berikut data ID user :")
    for i in akun["idu"].keys():
        print(f"{i}.",akun["idu"][i])
    try:
        z = int(input("Pilih ID user yang datanya ingin anda ubah :"))
        while z not in akun["idu"].keys():
            print("Masukkan pilihan yang sesuai")
            z = int(input("Pilih ID user yang datanya ingin anda ganti :"))
    except ValueError:
        print("Masukkan pilihan yang sesuai")
        z = int(input("Pilih ID user yang datanya ingin anda ubah :"))
        while z not in akun["idu"].keys():
            print("Masukkan pilihan yang sesuai")
            z = int(input("Pilih ID user yang datanya ingin anda ganti :"))
    while z in akun["idu"].keys():
        print("1. Id login")
        print("2. Password Login")
        print("3. Nama")
        print("4. Nomor Telpon")
        print("5. E-Mail")
        try:
            pilih = int(input("Data apa yang ingin anda ubah : "))
            while pilih not in range (1,6):
                print("Masukkan menu yang sesuai")
                pilih = int(input("Data apa yang ingin anda ubah : "))
        except ValueError:
            print("Masukkan menu yang sesuai")            
            pilih = int(input("Data apa yang ingin anda ubah : "))
            while pilih not in range (1,6):
                print("Masukkan menu yang sesuai")
                pilih = int(input("Data apa yang ingin anda ubah : "))
        if pilih == 1:
            idbaru = input("Masukkan ID baru : ")
            akun["idu"][z] = idbaru
            time.sleep(2)
            print("Data berhasil diubah")
            time.sleep(2)
            input("Enter untuk lanjut >>> ")
            time.sleep(1)
            os.system("cls")
            admin()
        elif pilih == 2:
            pwbaru = input("Masukkan password baru : ")
            akun["pwu"][z] = pwbaru   
            time.sleep(2)
            print("Data berhasil diubah")
            time.sleep(2)
            input("Enter untuk lanjut >>> ")
            time.sleep(1)
            os.system("cls")
            admin()
        elif pilih == 3:
            namabaru = input("Masukkan nama baru : ")
            akun["nama"][z] = namabaru
            time.sleep(2)
            print("Data berhasil diubah")
            time.sleep(2)
            input("Enter untuk lanjut >>> ")
            time.sleep(1)
            os.system("cls")
            admin()
        elif pilih == 4:
            nomorbaru = input("Masukkan nomor telepon baru : ")
            akun["nomor"][z]= nomorbaru  
            time.sleep(2)
            print("Data berhasil diubah")
            time.sleep(2)
            input("Enter untuk lanjut >>> ")
            time.sleep(1)
            os.system("cls")
            admin()
        elif pilih == 5 :
            emailbaru = input("Masukkan e-Mail baru : ")
            akun["email"][z] = emailbaru
            time.sleep(2)
            print("Data berhasil diubah")
            time.sleep(2)
            input("Enter untuk lanjut >>> ")
            time.sleep(1)
            os.system("cls")
            admin()

        break

def editdata(i):
    print("1. Id login")
    print("2. Password Login")
    print("3. Nama")
    print("4. Nomor Telpon")
    print("5. E-Mail")
    try:
        pilih = int(input("Data apa yang ingin anda ubah : "))
        while pilih not in range (1,6):
            print("Masukkan menu yang sesuai")
            pilih = int(input("Data apa yang ingin anda ubah : "))
    except ValueError:
        print("Masukkan menu yang sesuai")
        pilih = int(input("Data apa yang ingin anda ubah : "))
    
    if pilih == 1:
        idbaru = input("Masukkan ID baru : ")
        akun["idu"][i] = idbaru
        input("Enter untuk lanjut >>> ")
        time.sleep(2)
        os.system("cls")
        user(i)
    elif pilih == 2:
        pwbaru = input("Masukkan password baru : ")
        akun["pwu"][i] = pwbaru   
        input("Enter untuk lanjut >>> ")
        time.sleep(2)
        os.system("cls")
        user(i)
    elif pilih == 3:
        namabaru = input("Masukkan nama baru : ")
        akun["nama"][i] = namabaru
        input("Enter untuk lanjut >>> ")
        time.sleep(2)
        os.system("cls")
        user(i)
    elif pilih == 4:
        nomorbaru = input("Masukkan nomor telepon baru : ")
        akun["nomor"][i]= nomorbaru  
        input("Enter untuk lanjut >>> ")
        time.sleep(2)
        os.system("cls")
        user(i)
    elif pilih == 5 :
        emailbaru = input("Masukkan e-Mail baru : ")
        akun["email"][i] = emailbaru
        input("Enter untuk lanjut >>> ")
        time.sleep(2)
        os.system("cls")
        user(i)
        
def isisaldo(i):
    print("Saldo anda saat ini Rp", akun["saldo"][i])
    try:
        x = int(input("Masukkan jumlah saldo yang ingin anda isi : Rp"))
        while x not in range (0,10000001) :
            print("Saldo terlalu banyak atau format tidak sesuai")
            x = int(input("Masukkan jumlah saldo yang ingin anda isi : Rp"))
            
    except ValueError:
        print("Masukkan saldo yang sesuai")
        x = int(input("Masukkan jumlah saldo yang ingin anda isi : Rp"))
        while x not in range (0,10000001) :
            print("Saldo terlalu banyak atau format tidak sesuai")
            x = int(input("Masukkan jumlah saldo yang ingin anda isi : Rp"))
    
    akun["saldo"][i] += x
    print("Dalam proses pengisian")
    time.sleep(2)
    print("Saldo anda berhasil ditambahkan")
    print("Saldo anda saat ini Rp ", akun["saldo"][i])
    time.sleep(2)
    user(i)
    
def regist():
    newid = input("Masukkan ID anda : ")    
    while newid in akun["idu"].values() or newid == akun["idad"]:
        print("ID sudah terdaftar")
        newid = input("Masukkan ID anda : ")
    akun["idu"][len(akun["idu"])] = newid
    newpw = input("Masukkan Password : ")
    akun["pwu"][len(akun["pwu"])] = newpw
    try:
        newsaldo = int(input("Masukkan Jumlah saldo (Minimal Rp 1.000.000):"))
        while newsaldo < 1000000:
            print("Saldo terlalu sedikit")
            newsaldo = int(input("Masukkan Jumlah saldo (Minimal Rp 1.000.000):"))
    except ValueError:
        print("Masukkan data yang sesuai")
        newsaldo = int(input("Masukkan Jumlah saldo (Minimal Rp 1.000.000):"))
        while newsaldo < 1000000:
            print("Saldo terlalu sedikit")
            newsaldo = int(input("Masukkan Jumlah saldo (Minimal Rp 1.000.000):"))
        
    akun["saldo"][len(akun["saldo"])] = newsaldo
    newnama = input("Masukkan nama lengkap : ")
    akun["nama"][len(akun["nama"])] = newnama
    
    try:        
        newnomor = int(input("Masukkan nomor telpon : "))
        
    except ValueError:
        print("Masukkan nomor telpon anda")
        newnomor = int(input("Masukkan nomor telpon : "))


    akun["nomor"][len(akun["nomor"])] = newnomor
    newemail = input("Masukkan E-Mail : ")
    akun["email"][len(akun["email"])] = newemail
    
    akun["riwayat"][len(akun["riwayat"])] = []
    time.sleep(0.25)
    print("Dalam proses pembuatan")
    time.sleep(2)
    print("Akun berhasil dibuat")
    time.sleep(4)
    os.system("cls")
    launch()

def ceksaldo(i):
    saldo = akun["saldo"][i]
    print("Saldo anda sebanyak Rp", saldo)
    
    input("Tekan enter untuk lanjut >>>")
    time.sleep(2)
    os.system("cls")
    user(i)
    
def login():
    idlogin = input ("Masukkan ID           : ")


    for i in akun["idu"].keys():
        if idlogin == akun["idu"][i] :
            break
        elif idlogin == akun["idad"] :
            break
        elif i >= len(akun["idu"]):
            print("Data tidak ditemukan")
            

            
    pwlogin = input ("Masukkan Password     : ")
    if pwlogin == akun["pwu"][i]:
        time.sleep(2)
        os.system("cls")
        user(i)
    elif pwlogin == akun["pwad"]:
        time.sleep(2)
        os.system("cls")
        admin()
    else:
        print("ID atau Password mungkin salah")
        print("Silahkan melakukan login kembali atau melakukan registrasi")
        time.sleep(2)
        os.system("cls")
        launch()
        
def user(i):
    print("MENU USER")
    print("1. Cek saldo akun")
    print("2. Pembelian tiket")
    print("3. Isi saldo")
    print("4. Ubah data pribadi")
    print("5. LogOut")

    try :
        pilih = int(input("Silahkan pilih menu :"))
        while pilih not in range(1,6):
            print("Masukkan menu yang sesuai")
            pilih = int(input("Silahkan pilih menu :"))
    except ValueError:  
        print("Masukkan menu yang sesuai")
        pilih = int(input("Silahkan pilih menu :"))
        while pilih not in range(1,6):
            print("Masukkan menu yang sesuai")
            pilih = int(input("Silahkan pilih menu :"))
    if pilih == 1:
        time.sleep(1)
        os.system("cls")
        ceksaldo(i)
    elif pilih == 2:
        time.sleep(1)
        os.system("cls")
        menu_awal(i)
    elif pilih == 3:
        time.sleep(1)
        os.system("cls")
        isisaldo(i)
    elif pilih == 4:
        time.sleep(1)
        os.system("cls")
        editdata(i)
    elif pilih == 5:
        time.sleep(2)
        os.system("cls")
        launch()

   
def admin():
    print("Selamat datang")
    print("1. Cek data akun user")
    print("2. Hapus data akun user")
    print("3. Cek daftar pembelian user")
    print("4. Ubah data Login user")
    print("5. LogOut")
    try :
        pilih = int(input("Silahkan pilih menu :"))
        while pilih not in range(1,6):
            print("Masukkan menu yang sesuai")
            pilih = int(input("Silahkan pilih menu :"))
    except ValueError:
        print("Masukkan menu yang sesuai")
        pilih = int(input("Silahkan pilih menu :"))
        while pilih not in range(1,6):
            print("Masukkan menu yang sesuai")
            pilih = int(input("Silahkan pilih menu :"))
    if pilih == 1:
        time.sleep(1)
        os.system("cls")
        cekdata()
    elif pilih == 2:
        time.sleep(1)
        os.system("cls")
        hapusdata()
    elif pilih == 3:
        time.sleep(1)
        os.system("cls")
        datapenerbangan()
    elif pilih == 4:
        time.sleep(1)
        os.system("cls")
        editakun()
    elif pilih == 5 :
        time.sleep(2)
        os.system("cls")
        launch()
       
def launch():
    print("\n=============================================")
    print("       TRAVELOKE 🛫 BOOK FLIGHT TICKET      ")
    print("=============================================")
    print("")
    print("1. Login")
    print("2. Registrasi")
    print("3. Exit")
    print("=============================================")
    try :
        pilih = int(input("Pilih menu : "))
        while pilih not in range(1,4):
            print("Masukkan pilihan yang sesuai")
            pilih = int(input("Pilih menu : "))
    
    except ValueError:
        print("Masukkan pilihan yang sesuai")
        pilih = int(input("Pilih menu : "))
        while pilih not in range(1,4):
            print("Masukkan pilihan yang sesuai")
            pilih = int(input("Pilih menu : "))
    if pilih == 1:
        login()
    elif pilih == 2:
        time.sleep(2)
        os.system("cls")
        regist()
        
    elif pilih == 3:
        while True :
            print ("\n=============================================")
            print ("        TERIMA KASIH TELAH BERKUNJUNG        ")
            print (" |^^| |^>^| SAMPAI BERTEMU LAGI |^<^| |^^| ")
            print ("=============================================")
            time.sleep(3)
            break

launch()