def binary_search(arr, n, target):
    l = 0
    r = n - 1
    hasil = []

    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, Judul Lagu: {arr[m]}")

        if target.lower() in arr[m].lower():
            hasil.append(m)

            i = m - 1
            while i >= 0:
                if target.lower() in arr[i].lower():
                    hasil.append(i)
                i -= 1

            i = m + 1
            while i < n:
                if target.lower() in arr[i].lower():
                    hasil.append(i)
                i += 1

            break

        elif target.lower() > arr[m].lower():
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1

    return sorted(hasil)

def main():
    arr = [
        "Africa",
        "All of Me",
        "Always",
        "Beat It",
        "Billie Jean",
        "Blinding Lights",
        "Cincin",
        "Come and Get Your Love",
        "Dancing On The Edge",
        "Die For You",
        "Dream On",
        "Duvet",
        "Forever Young",
        "Human Nature",
        "Impossible",
        "I Will Survive",
        "Jane Doe",
        "Judas",
        "Kicau Mania",
        "Killbill",
        "Killer Queen",
        "Lonely",
        "Lost Kitten",
        "Monokrom",
        "No One Notice",
        "No Surprises",
        "Oddloop",
        "Payphone",
        "Penjaga Hati",
        "Perisai Jitu",
        "Rapsodi",
        "Rockstar",
        "Saat Bahagia",
        "Seandainya",
        "Seven Nation Army",
        "Take on Me",
        "The Wonder of You",
        "Thriller",
        "Umbrella",
        "Viva La Vida",
        "We Are Young"
    ]

    n = len(arr)

    print("Judul Lagu di Playlist:")
    for i in range(n):
        print(f"{i + 1}. {arr[i]}")

    target = input("\nMasukkan judul/kata lagu yang ingin dicari: ")

    hasil = binary_search(arr, n, target)

    if len(hasil) > 0:
        print(f"\nKata '{target}' ditemukan pada:")
        for i in hasil:
            print(f"Indeks ke-{i} : {arr[i]}")
    else:
        print(f"\n'{target}' tidak ditemukan")


if __name__ == "__main__":
    main()