import json
with open('mahasiswa.json','r') as file:
    data =  json.load(file)
jumlah = int(input('Masukan jumlah mahasiswa baru : '))
for i in range(jumlah):
    nama = input('Masukan nama Anda : ')
    hobi = int(input('Masukan Jumlah hobi : '))
    for x in range (1,hobi+1):
        hobitotal = []
        hobi = (input('Masukan Hobi ke-'+ str(x) + ' : '))
        hobitotal.append(hobi)
    prestasi = input('Masukan Prestasi Anda : ')
    print('=== DATA berhasil ditambahkan === \n')

with open('mahasiswa.json', 'w') as file:
    json.dump(data, file)