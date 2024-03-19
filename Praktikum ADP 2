#program order paket makanan
print("Selamat Datang")
print("==============")
print("Daftar Paket Hemat :")
print("_________________________________________________")
print("| Paket			| Harga			|")
print("_________________________________________________")
print("| Paket A		| Rp. 25.000		|")
print("| Paket B		| Rp. 30.000		|")
print("| Paket C		| Rp. 45.000		|")
print("_________________________________________________")
Nama = str(input("Masukkan Nama Anda : "))
pilih_paket = str(input("Pilih Jenis Paket (A/B/C) :"))
jumlah_paket = int(input("Masukkan Jumlah Paket :"))
harga_paket = 0
#Menentukan harga paket
if pilih_paket.upper() == "A" :
	harga_paket = 25000
elif pilih_paket.upper() == "B" :
	harga_paket = 30000
elif pilih_paket.upper() == "C" :
	harga_paket = 45000
else :
	print("Pilihan Anda tidak valid, mohon masukkan sesuai jenis paket A, B atau C.")
total_harga_paket = harga_paket*jumlah_paket
print("Total harga paket = Rp.",total_harga_paket)
print()
#ongkir
print("Pesar-Antar Makanan")
print("Daftar Ongkir :")
print("_________________________________________________")
print("| Jarak Rumah-Restoran	| Ongkir		|")
print("_________________________________________________")
print("| 1. <500m		| Gratis		|")
print("| 2. 500m-1,5km		| Rp. 10.000		|")
print("| 3. >1,5km		| Rp. 20.000		|")
print("_________________________________________________")
pilih_jarak = int(input("Pilih jarak rumah Anda (1/2/3) :"))
ongkir = 0
#Menentukan ongkir berdasarkan jarak
if pilih_jarak == 1 : 
	ongkir = 0
elif pilih_jarak == 2 :
	ongkir = 10000
elif pilih_jarak == 3 : 
	ongkir = 20000
else :
	print("Pilihan Anda tidak valid, mohon pilih 1, 2, atau 3")
print("Total harga ongkir = Rp",ongkir)
print()
#Total biaya
total_biaya = total_harga_paket + ongkir 
print("Total biaya yang harus dibayar : Rp.",total_biaya)
