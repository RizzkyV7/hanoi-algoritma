def hanoi(n, asal, tujuan, bantuan):
    if n == 1:
        print(f"Pindahkan piringan 1 dari {asal} ke {tujuan}")
    else:
        # Pindahkan piringan yang lebih kecil ke tiang bantuan
        hanoi(n - 1, asal, bantuan, tujuan)

        # Pindahkan piringan terbesar ke tiang tujuan
        print(f"Pindahkan piringan {n} dari {asal} ke {tujuan}")

        # Pindahkan piringan dari tiang bantuan ke tujuan
        hanoi(n - 1, bantuan, tujuan, asal)


# Program utama
jumlah_piringan = 3

print("Solusi Hanoi:")
hanoi(jumlah_piringan, "A", "C", "B")
