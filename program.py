import json
with open('mahasiswa.json','r') as file:
    data =  json.load(file)
jumlah = int(input('Masukan jumlah mahasiswa baru : '))
list = []
dict = {}
hobitotal = []
for i in range(jumlah):
    nama = input('Masukan nama Anda : ')
    list.append(nama)
    hobi = int(input('Masukan Jumlah hobi : '))
    for x in range (1,hobi+1):

        hobi = (input('Masukan Hobi ke-'+ str(x) + ' : '))
        hobitotal.append(hobi)
    prestasi = input('Masukan Prestasi Anda : ')
    print('=== DATA berhasil ditambahkan === \n')

    list.append({"BioData":{"Hobi":hobitotal,"Prestasi":prestasi}})
data[nama] = list

with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)
