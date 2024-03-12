#hitung_volume_dan_luas_balok(panjang,lebar,tinggi,faktor_konversi)
print()
panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))
faktor_konversi = float(input("Masukkan faktor konversi balok: "))
print()
Volume_balok = panjang*lebar*tinggi*faktor_konversi 
Luas_balok = 2*((panjang*lebar)+(panjang*tinggi)+(lebar*tinggi))*faktor_konversi
print()
print("volume balok adalah: ",Volume_balok)
print("luas balok adalah: ",Luas_balok)
