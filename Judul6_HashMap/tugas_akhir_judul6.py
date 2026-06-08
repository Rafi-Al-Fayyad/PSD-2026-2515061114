class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value   
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\n=== Data Pemain ===")
        for i in range(self.SIZE):
            print(f"Server {i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(
                    f"[ID:{current.key}, Nama:{current.value['nama']}, "
                    f"Level:{current.value['level']}, Gold:{current.value['gold']}] -> ",
                    end=""
                )
                current = current.next

            print("NULL")


def main():
    game_server = HashMapSeparateChaining()

    game_server.insert(1001, {"nama": "Ranger Hitam", "level": 67, "gold": 67000})
    game_server.insert(1011, {"nama": "Noctifer", "level": 15, "gold": 17000})
    game_server.insert(1021, {"nama": "Mixie", "level": 25, "gold": 32000})
    game_server.insert(1002, {"nama": "Ilyna", "level": 10, "gold": 9000})
    game_server.insert(1005, {"nama": "Lucius", "level": 7, "gold": 5500})
    game_server.insert(1015, {"nama": "Lihh", "level": 30, "gold": 39000})
    game_server.insert(1007, {"nama": "Liquescit", "level": 5, "gold": 1000})

    game_server.display()

    pemain = game_server.search(1011)

    if pemain is not None:
        print("\nPemain ditemukan:")
        print("ID    :", pemain.key)
        print("Nama  :", pemain.value["nama"])
        print("Level :", pemain.value["level"])
        print("Gold  :", pemain.value["gold"])
    else:
        print("\nPemain tidak ditemukan")

    game_server.remove_key(1011)

    print("\nSetelah pemain ID 1011 logout:")
    game_server.display()


if __name__ == "__main__":
    main()