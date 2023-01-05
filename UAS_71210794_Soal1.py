class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
    
    def getNamaPelanggan(self):
        return self._namaPelanggan
class WarungMakan:
    DEFAULT_CAPACITY = 5

    def __init__(self): #tidak boleh mengganti / menambah metode init
        self._data = [None] * WarungMakan.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def dequeue(self): 
        old = self._data
        walk = 1
        if self.is_empty():
            print("Antrian Kosong")
        jawaban = self._data[self._front]
        print("###", jawaban.getNamaPelanggan(),"Selesai Membayar ###")
        self._data[self._front] = None
        for k in range (self._size):
            self._data[k] = old[walk]
            walk = (1+ walk)% len(old)
        self._size -= 1
        return jawaban
        

    def enqueue(self, namaPelanggan): #menambah data ke list
        new = NodePelanggan(namaPelanggan)
        if self._size >= self.DEFAULT_CAPACITY:
            self.resizeBy3()            
        helper = (self._front + self._size) % len(self._data)
        self._data[helper] = new
        self._size += 1
        
    
    def resizeBy3(self): #menambah ukuran queue sebesar 3
        old = self._data
        self._data = [None] * (self.DEFAULT_CAPACITY + 3)
        walk = self._front
        for k in range (self._size):
            self._data[k] = old[walk]
            walk = (1+ walk)% len(old)
        self._front = 0
        print()
    
    def printAll(self):
        print("\n=== WarungMakan ===")
        for i in range(len(self._data)):
            if self._data[i] != None:
                print(i+1,end=". ")
                print(self._data[i].getNamaPelanggan())
            else:
                print(i+1,end=". ")
                print("Kosong")
        print()

# test case program
wm = WarungMakan()
wm.enqueue("Pelanggan A")
wm.enqueue("Pelanggan B")
wm.enqueue("Pelanggan C")
wm.enqueue("Pelanggan D")
wm.enqueue("Pelanggan E")
wm.printAll()
wm.enqueue("Pelanggan F")
wm.enqueue("Pelanggan G")
wm.printAll()
wm.dequeue()
wm.dequeue()
wm.dequeue()
wm.printAll()
