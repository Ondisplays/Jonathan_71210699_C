class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
       self._data = []
       self._capacity = Kasir.DEFAULT_CAPACITY
       
    def __len__(self): #mengembalikan ukuran Queue
        pass
        return len(self._data)

    def isEmpty(self): #mengecek apakah Queue kosong ?
        pass
        return len(self._data) == 0

    def dequeue(self): #menghapus data paling depan (front)
        pass
        datanya = self._data[0]
        self._data.remove(datanya)
        print()
        print(f"### Pelanggan {datanya} Selesai Membayar ### \n")

    def enqueue(self, namaPelanggan): #menambah data ke list
        pass
        self._data.append(namaPelanggan)


    def resize(self, cap): #mengubah ukuran queue pada list
        pass
        print()
        print(f"### Melakukan Resize ### \n")
        self._capacity = self._capacity * cap
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        if len(self._data) > self._capacity:
                self.resize(2)
        print("=== Kasir ===")
        c = len(self._data)-1
        n = 1
        for i in range(0, (self._capacity)):            
            if i <= c:
                print(n,".",self._data[i], end=' ')
                print()
            else:
                print(n,". Kosong")
            n += 1

        print()

        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

