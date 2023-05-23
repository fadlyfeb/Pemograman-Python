import datetime as dt, os, sys, time
from collections import deque
Time = dt.datetime.now()
#Set / Dictionary
Lokasi = {
            'Kebon Jeruk': {
                'Kemanggisan': 5,
                'Palmerah': 3,
                'SukabumiUtara': 2
            },
            'Kemanggisan': {
                'Slipi': 4,
                'Petamburan': 4,
                'BendunganHilir': 5
            },
            'Palmerah' : {
                'Slipi': 5,
                'Petamburan': 3,
                'BendunganHilir': 2
            },
            'SukabumiUtara':{
                'Slipi': 5,
                'Petamburan': 5,
                'BendunganHilir': 5
            },
            'Slipi':{
                'MedanMerdeka': 4,
                'Sudirman': 6
            },
            'Petamburan':{
                'MedanMerdeka': 4,
                'Sudirman': 3
            },
            'BendunganHilir':{
                'MedanMerdeka':7,
                'Sudirman':4
            },
            'MedanMerdeka':{
                'Menteng':4
            },
            'Sudirman':{
                'Menteng':9
            },
            'Menteng':{}
        }
#List
Lokasi2 = ['Kebon Jeruk','Kemanggisan','Palmerah','SukabumiUtara','Slipi','Petamburan','BendunganHilir','MedanMerdeka','Sudirman','Menteng']
animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
Pelanggan = []
Waktu = []
Transaksi = []
#queue
queue = deque()
#Class
class TampilanAntrian:
    '''Tampilan Antrian'''

    def __init__(self, nama):
        self.nama = nama

    def tampilkan_profil(self):
        print("\t\t\t\tNama   :", self.nama)

class TampilanHistory:
    '''Histori Transaksi'''

    def __init__(self, nama, pembayaran,timenow):
        self.nama = nama
        self.pembayaran = pembayaran
        self.timenow = timenow

    def tampilkan_profil(self):
        print("\t\t\t\t===========================")
        print("\t\t\t\tNama   :", self.nama)
        print("\t\t\t\tWaktu  :", self.timenow)
        print("\t\t\t\tTotal  : Rp", self.pembayaran)
        print("\t\t\t\t===========================")

def animasi():
    for i in range(len(animation)):
        time.sleep(0.2)
        sys.stdout.write("\r\t\t\t\t" + animation[i % len(animation)])
        sys.stdout.flush()

def gerak(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1/10)

def menu():
    gerak("\t\t\t\t====================================")
    gerak("\t\t\t\t| PROGRAM PEMESANAN LAUNDRY ONLINE |")
    gerak("\t\t\t\t|             OLEH                 |")
    gerak("\t\t\t\t|          KELOMPOK DUA            |")
    gerak("\t\t\t\t====================================")
    input("\t\t\t\t       PRESS ENTER TO START")

def menu1():
    print("\t\t\t\t====================================")
    print("\t\t\t\t|         SELAMAT DATANG           |")
    print("\t\t\t\t|               DI                 |")
    print("\t\t\t\t|         LAUNDRY ARAMITA          |")
    print("\t\t\t\t====================================")
    print("\t\t\t\t| 1.Melakukan Pemesanan            |")
    print("\t\t\t\t| 2.Menampilkan antrian            |")
    print("\t\t\t\t| 3.Mengeluarkan antrian           |")
    print("\t\t\t\t| 4.Pencarian Pemesanan            |")
    print("\t\t\t\t| 5.Menampilkan Histori Transaksi  |")
    print("\t\t\t\t| 6.Menampilkan Saldo toko         |")
    print("\t\t\t\t| 7.Exit                           |")
    print("\t\t\t\t====================================")

def menu2():
    print("\t\t\t\t===========================")
    print("\t\t\t\t|     SILAHKAN MEMILIH    |")
    print("\t\t\t\t===========================")
    print("\t\t\t\t| 1.Jas     : Rp30000/pcs |")
    print("\t\t\t\t| 2.Karpet  : Rp40000/pcs |")
    print("\t\t\t\t| 3.Pakaian : Rp15000/kg  |")
    print("\t\t\t\t| 4.Jaket   : Rp25000/pcs |")
    print("\t\t\t\t===========================")

def menu3():
    print("\t\t\t\t====================================")
    print("\t\t\t\t|        SILAHKAN MEMILIH          |")
    print("\t\t\t\t====================================")
    print("\t\t\t\t| 1.Kebon Jeruk  | 6.Petamburan    |")
    print("\t\t\t\t| 2.Kemanggisan  | 7.BendunganHilir|")
    print("\t\t\t\t| 3.Palmerah     | 8.MedanMerdeka  |")
    print("\t\t\t\t| 4.SukabumiUtara| 9.Sudirman      |")
    print("\t\t\t\t| 5.Slipi        | 10.Menteng      |")
    print("\t\t\t\t====================================")

def menu4():
    print("\t\t\t\t================================")    
    print(f"\t\t\t\t Harga Pemesanan  : Rp{Harga}  ")
    print(f"\t\t\t\t Biaya Pengiriman : Rp{Ongkos} ")
    print("\t\t\t\t================================")
    print(f"\t\t\t\t Total Pembayaran : Rp{Total}  ")
    print("\t\t\t\t================================")

def struk():
    print("\t\t\t\t===========================")
    print("\t\t\t\t----------STRUK------------")
    print("\t\t\t\t===========================")
    print(f"\t\t\t\t Waktu           : {jam}")
    print(f"\t\t\t\t Antrian         :",len(queue))
    print(f"\t\t\t\t Nama            : {Pemesan}")
    print(f"\t\t\t\t Tujuan          : {berhenti}")
    print(f"\t\t\t\t Jarak Tempuh    :",distance[berhenti],"Km")
    print(f"\t\t\t\t Biaya Pemesanan : Rp{Harga}")
    print(f"\t\t\t\t Biaya Pengiriman: Rp{Ongkos}")
    print(f"\t\t\t\t Total           : Rp{Total}")
    print(f"\t\t\t\t Tunai           : Rp{Bayar}")
    print(f"\t\t\t\t Kembalian       : Rp{Kembalian}")
    print("\t\t\t\t===========================")
    print("\t\t\t\t--------TERIMAKASIH---------")
    print("\t\t\t\t===========================")
    input("\t\t\t\tPress Enter to continue")

def terimakasih():
    gerak("\t\t\t\t====================================")
    gerak("\t\t\t\t|   TERIMKASIH TELAH MENGGUNAKAN   |")
    gerak("\t\t\t\t|    PROGRAM PEMESANAN LAUNDRY     |")
    gerak("\t\t\t\t|         (KELOMPOK DUA)           |")
    gerak("\t\t\t\t====================================")
    input("\t\t\t\t       PRESS ENTER TO END")

def searching():
    Nama=input("\t\t\t\tMasukan Nama : ")
    d = 0
    e = 0
    if len(queue) > 0:
        a = 0
        while a < len(queue):
            if Nama == queue[a]:
                Antri = TampilanAntrian(queue[a])
                Antri.tampilkan_profil()
                print("\t\t\t\tStatus : Belum Terkirim")
                d = 1
                break;
            a+=1
    if len(Pelanggan) > 0 and d == 0:
        a = 0
        while a < len(Pelanggan):
            if Nama == Pelanggan[a]:
                Antri = TampilanAntrian(Pelanggan[a])
                Antri.tampilkan_profil()
                print("\t\t\t\tStatus : Terkirim")
                e = 1
            a+=1
    if d == 0 and e == 0:
        print("\t\t\t\tNama yang anda masukkan tidak terdaftar")
    a=0
    d=0
    e=0

def HistoriTransaksi():
    print("\t\t\t\tHistori Transaksi")
    if len(queue) > 0 or len(Pelanggan) > 0 and len(Transaksi) > 0 and len(Waktu) > 0:
        a = 0
        while a < len(queue) and a < len(Transaksi) and a < len(Waktu):
            print("")
            if len(Pelanggan) > 0:
                print('\t\t\t\tTransaksi ke-',a+1+len(Pelanggan))
                History = TampilanHistory(queue[a],Transaksi[a+len(Pelanggan)],Waktu[a+len(Pelanggan)])
                History.tampilkan_profil()
                print("\t\t\t\tStatus : Belum Terkirim")
            else :
                print('\t\t\t\tTransaksi ke-',a+1)
                History = TampilanHistory(queue[a],Transaksi[a],Waktu[a])
                History.tampilkan_profil()
                print("\t\t\t\tStatus : Belum Terkirim")
            a += 1
        a = 0
        if len(Pelanggan) > 0:
            while a < len(Pelanggan) and a < len(Transaksi) and a < len(Waktu):
                print("")
                print('\t\t\t\tTransaksi ke-',a+1)
                History = TampilanHistory(Pelanggan[a],Transaksi[a],Waktu[a])
                History.tampilkan_profil()
                print("\t\t\t\tStatus : Sudah Terkirim")
                a += 1
            a = 0
    else :
        print("\t\t\t\tTidak ada history transaksi")
    input("\t\t\t\tPress Enter to continue")

#Variabel
Total = 0 #Total pembayaran
Harga = 0 #Harga pemesanan laundry
ulang = 0
Saldo = 0 #Saldo Laundry
Kembalian = 0 
a = 0
#Pemesan -> orang yang memesan
#Berhenti -> Tempat tujuan pengiriman
#Banyak -> Jumlah barang misalnya 1kg, 1 buah baju
#Jam -> waktu pemesanan
#PASSWORD DAN ID
Id = 'Laundry'
Pw = '010203'
while(a<=7):
    print("")
    a+=1
a=0
menu()
while(ulang==0):
    os.system("cls")
    menu1()
    choice = input("\t\t\t\tEnter your choice : ")
    if choice == '1':
        os.system("cls")
        menu2()
        sys.stdout.flush()
        Pemesan = input("\t\t\t\tNama           : ")
        sys.stdout.flush()
        i = 0         
        Limit = int(input("\t\t\t\tBanyak pesanan : "))
        while(i < Limit):
            choice = input("\t\t\t\tPilihan Barang : ")
            if choice == '1':
                Banyak = int(input("\t\t\t\tJumlah Barang  : "))
                Harga += Banyak * 30000
            elif choice == '2':
                Banyak = int(input("\t\t\t\tJumlah Barang  : "))
                Harga += Banyak * 40000
            elif choice == '3':
                Banyak = int(input("\t\t\t\tJumlah Barang  : "))
                Harga += Banyak * 15000
            elif choice == '4':
                Banyak = int(input("\t\t\t\tJumlah Barang  : "))
                Harga += Banyak * 25000
            i += 1
        input("\t\t\t\tPress Enter to continue")
        os.system("cls")
        menu3()
        #Graph
        infinity = float("infinity")
        mulai = 'Kebon Jeruk'
        print("\t\t\t\tContoh Penulisan BendunganHilir")
        berhenti = input("\t\t\t\tMasukan tempat tujuan : ")
        a = 0
        while a < len(Lokasi2):
            if berhenti == Lokasi2[a]:
                distance = {}
                city = {}
                for node in Lokasi:
                    distance[node] = infinity
                    city[node] = {}
                    distance[mulai] = 0

                def find_cheapest_node(distance, not_checked):
                    lowest_dist = infinity
                    cheapest_node = ""
                    for node in distance:
                        if node in not_checked and distance[node] <= lowest_dist:
                            lowest_dist = distance[node]
                            cheapest_node = node
                    
                    return cheapest_node

                ### Algoritma Dijkstra
                not_checked = [node for node in distance]
                node = find_cheapest_node(distance, not_checked)
                while not_checked:
                    dist = distance[node]
                    child_dist = Lokasi[node]
                    for c in child_dist:
                        if distance[c] > dist + child_dist[c]:
                            distance[c] = dist + child_dist[c]
                            city[c] = node

                    not_checked.pop(not_checked.index(node))
                    node = find_cheapest_node(distance, not_checked)
                enter = " "
                print (enter)
                print(f"\t\t\t\tJarak dari {mulai} ke {berhenti} sejauh {distance[berhenti]} km!")

                if distance[berhenti] < infinity:
                    alur = [berhenti]
                    i = 0
                    while mulai not in alur:
                        alur.append(city[alur[i]])
                        i +=1

                    #barrier = ">"
                    #print(barrier*50)
                    print(f"\t\t\t{alur[::-1]}")
                else:
                    print("Alur tidak dapat ditemukan")
                    input("\t\t\t\tPress Enter to continue")
                #Perhitungan biaya total
                Ongkos = distance[berhenti] * 2000
                Total = Harga + Ongkos
                input("\t\t\t\tPress Enter to continue")
                os.system("cls")
                menu4()
                Bayar = int(input("\t\t\t\tMasukan uang :Rp"))
                if Bayar >= Total:
                    Kembalian = Bayar - Total
                    jam = Time.strftime('%H:%M:%S')
                    #Queue ->dequeue
                    queue.append(Pemesan)
                    Waktu.append(jam)
                    Transaksi.append(Total)

                    print("\t\t\t\tSilahkan menunggu struk akan dicetak")
                    time.sleep(1)
                    animasi()
                    #Pencetakan Struk
                    os.system("cls")
                    struk()
                else:
                    print("\t\t\t\tSaldo anda tidak mencukupi")
                    Harga=0
                    input("\t\t\t\tPress Enter to continue")
                Harga = 0
                break
            elif a==9 and berhenti != Lokasi2[a]:
                print("\t\t\t\tData yang anda masukan salah")
                Harga=0
                input("\t\t\t\tPress Enter to continue")
            a+=1
        a=0
    elif choice == '2':
        print("\t\t\t\tMenampilkan Antrian")
        if len(queue) > 0:
            a = 0
            while a < len(queue):
                print('\t\t\t\tAntrian ke-',a+1)
                Antrian = TampilanAntrian(queue[a])
                Antrian.tampilkan_profil()
                a += 1
            a = 0
        else:
            print("\t\t\t\tTidak ada antrian")
        input("\t\t\t\tPress Enter to continue")
    elif choice == '3':
        if len(queue) > 0:
            print(f"\t\t\t\tAntrian keluar :{queue[0]}")
            Pelanggan.append(queue[0])
            queue.popleft()
        else : 
            print("\t\t\t\tBelum ada antrian")
        input("\t\t\t\tPress Enter to continue")

    elif choice == '4':
        if len(queue) == 0 and len(Pelanggan) == 0:
            print("\t\t\t\tBelum ada pemesanan")
        else :
            searching()
        input("\t\t\t\tPress Enter to continue")
    elif choice == '5':
        Username = input("\t\t\t\tMasukan Username : ")
        Password = input("\t\t\t\tMasukan Password : ")
        if Username == Id and Password == Pw:
            print("\t\t\t\tBerhasil, dalam proses")
            time.sleep(1)
            animasi()
            print("")
            HistoriTransaksi()
        else :
            print("\t\t\t\tData yang anda masukan salah, Silahkan ulangi")
            input("\t\t\t\tPress Enter to continue")        
    elif choice == '6':
        Username = input("\t\t\t\tMasukan Username : ")
        Password = input("\t\t\t\tMasukan Password : ")
        if Username == Id and Password == Pw:
            print("\t\t\t\tBerhasil, dalam proses")
            time.sleep(1)
            animasi()
            print("")
            if len(Transaksi) > 0:
                a = 0
                while a < len(Transaksi):
                    Saldo += Transaksi[a]
                    a +=1
                a = 0
                print(f"\t\t\t\tSaldo Laundry : {Saldo}")
                Saldo = 0
                input("\t\t\t\tPress Enter to continue")
            else :
                Saldo = 0
                print(f"\t\t\t\tSaldo Laundry = {Saldo}")
                input("\t\t\t\tPress Enter to continue")
        else :
            print("\t\t\t\tData yang anda masukan salah, Silahkan ulangi")
            input("\t\t\t\tPress Enter to continue")
    elif choice == '7':
        ulang = 1
os.system("cls")
a = 0
while(a<=7):
    print("")
    a+=1
a=0
terimakasih()
    

