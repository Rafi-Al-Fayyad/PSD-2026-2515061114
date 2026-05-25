class Node:
    def __init__(self, score, player):
        self.score = score
        self.player = player
        self.left = None
        self.right = None

class GameLeaderboard:
    def __init__(self):
        self.root = None

    def insert_node(self, root, score, player):
        if root is None:
            return Node(score, player)

        if score < root.score:
            root.left = self.insert_node(root.left, score, player)
        else:
            root.right = self.insert_node(root.right, score, player)

        return root

    def insert(self, score, player):
        self.root = self.insert_node(self.root, score, player)

    def descending_order(self, root):
        if root is not None:
            self.descending_order(root.right)
            print(f"{root.player} : {root.score}")
            self.descending_order(root.left)

    def highest_score(self):
        current = self.root

        if current is None:
            return None

        while current.right is not None:
            current = current.right

        return current

    def lowest_score(self):
        current = self.root

        if current is None:
            return None

        while current.left is not None:
            current = current.left

        return current

    def search_score(self, root, score):
        if root is None:
            return None

        if score == root.score:
            return root

        elif score < root.score:
            return self.search_score(root.left, score)

        else:
            return self.search_score(root.right, score)

    def delete_node(self, root, score):
        if root is None:
            return None

        if score < root.score:
            root.left = self.delete_node(root.left, score)

        elif score > root.score:
            root.right = self.delete_node(root.right, score)

        else:
            if root.left is None and root.right is None:
                return None

            elif root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = root.right
            while temp.left is not None:
                temp = temp.left

            root.score = temp.score
            root.player = temp.player

            root.right = self.delete_node(root.right, temp.score)

        return root

    def delete(self, score):
        self.root = self.delete_node(self.root, score)


def main():
    game = GameLeaderboard()

    while True:
        print("\n=== LEADERBOARD GAME ===")
        print("1. Tambah skor pemain")
        print("2. Tampilkan leaderboard")
        print("3. Lihat skor tertinggi")
        print("4. Lihat skor terendah")
        print("5. Cari pemain berdasarkan skor")
        print("6. Hapus pemain")
        print("7. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            player = input("Nama pemain: ")
            score = int(input("Masukkan skor: "))
            game.insert(score, player)
            print("Skor berhasil ditambahkan!")

        elif pilih == "2":
            print("\n=== LEADERBOARD ===")
            game.descending_order(game.root)

        elif pilih == "3":
            top = game.highest_score()

            if top:
                print(f"Top Player : {top.player} ({top.score})")
            else:
                print("Leaderboard kosong")

        elif pilih == "4":
            low = game.lowest_score()

            if low:
                print(f"Skor Terendah : {low.player} ({low.score})")
            else:
                print("Leaderboard kosong")

        elif pilih == "5":
            score = int(input("Masukkan skor yang dicari: "))
            result = game.search_score(game.root, score)

            if result:
                print(f"Pemain ditemukan: {result.player}")
            else:
                print("Skor tidak ditemukan")

        elif pilih == "6":
            score = int(input("Masukkan skor yang dihapus: "))
            game.delete(score)
            print("Data berhasil dihapus")

        elif pilih == "7":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()