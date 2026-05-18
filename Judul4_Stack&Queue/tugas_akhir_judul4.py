class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, player):
        new_node = Node(player)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Player {player} masuk ke matchmaking")

    def dequeue(self):
        if self.is_empty():
            print("Tidak ada player dalam matchmaking")
            return

        temp = self.front_ptr
        print(f"Player {temp.data} berhasil menemukan match")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Matchmaking kosong")
            return

        print(f"Player paling depan: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Matchmaking kosong")
            return

        print("Antrean matchmaking:")
        current = self.front_ptr

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
            
        print("None")

def main():
    matchmaking = QueueLinkedList()
    pilih = 0

    while pilih != 5:
        print("\n=== MATCHMAKING GAME ONLINE ===")
        print("1. Player Masuk Matchmaking")
        print("2. Cari Match (Dequeue)")
        print("3. Lihat Player Terdepan")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            player = input("Masukkan username player: ")
            matchmaking.enqueue(player)
        elif pilih == 2:
            matchmaking.dequeue()
        elif pilih == 3:
            matchmaking.peek()
        elif pilih == 4:
            matchmaking.display()
        elif pilih == 5:
            print("Program matchmaking selesai")
        else:
            print("Menu tidak valid!")


if __name__ == "__main__":
    main()