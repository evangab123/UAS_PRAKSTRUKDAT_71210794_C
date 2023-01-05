class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None
class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0
    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False
    
    def printAll(self):
        if self.isEmpty():
            print("Tugas Habis")
        else:
            helper = self._head
            print("=== Prioritas : Tugas ===")
            while helper != self._tail:
                print("[",helper._priority,"] :", helper._data)
                helper = helper._next
                
    def _addHead(self, newNode):
        if newNode._priority > self._head._priority:
            newNode._next =self._head 
            self._head._prev = newNode
            self._head = newNode
    def _addTail(self, newNode):
        if newNode._priority <= self._head._priority:
            self._tail._next = newNode
            newNode._prev = self._tail
            self._tail = newNode
            self._tail._next = None
    def _addMiddle(self, newNode):
        bantu = self._head
        while bantu._priority < newNode._priority:
            bantu = bantu._next
        bantu2 = bantu._prev
        newNode._next = bantu
        bantu._prev = newNode
        bantu2._next = newNode
        newNode._prev = bantu2

    def add(self, data, priority):
        baru = Node(data,priority)
        if self.isEmpty():
            self._head = baru
            self._tail = baru
        elif self._size == 1:
            if self._head._priority > priority:
                self._addHead(baru)
            else:
                self._addTail(baru)
        else:
            if self._head._priority > priority:
                self._addHead(baru)
            elif self._tail._priority <= priority:
                self._addTail(baru)
            else:
                self._addMiddle(baru)
        
        self._size = self._size + 1
            
        
        
    def remove(self) -> None:
        # if self.isEmpty() == False:
        #     hapus = self._head
        #     if self._size == 1:
        #         self._head = None
        #     else:
        #         self._head = self._addHead
        pass
            
    def removePriority(self, priority) -> None:
         #isi kode anda
        pass

if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()
#  tugasKu.remove()
#  tugasKu.printAll()
#  tugasKu.removePriority(2)
#  tugasKu.removePriority(4)
#  tugasKu.printAll()