def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah buku: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []

    print("Masukkan judul buku:")
    for i in range(n):
        judul = input(f"Judul buku ke-{i + 1}: ")
        arr.append(judul)

    print(f"\nDaftar judul buku sebelum diurutkan: {arr}")

    bubble_sort(arr, n)

    print("\nDaftar judul buku setelah diurutkan:")
    for i in range(n):
        print(arr[i])


if __name__ == "__main__":
    main()