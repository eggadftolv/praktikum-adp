#program perulangan
print("Perulangan angka kelipatan 4 = DOR sebanyak 80")
print()
counter = 1
for i in range(0, 80, 8):
    for j in range(i, i + 8):
        if counter % 4 == 0:
            print('DOR', end=' ')
        else:
            print(counter, end=' ')
        counter += 1
    print()
