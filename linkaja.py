print("\n----------Selamat Datang Pengguna Link Aja!-----------")

print("\nBerikut merupakan layanan yang tersedia:\n")

print("a. Cek Saldo\nb. Top Up\nc. Pembelian")
menu = input("\nPilih Menu:").lower()
saldo_sekarang = 1500000

if menu == "a":
        print("\nSaldo Anda: ", saldo_sekarang)
elif menu == "b":
    saldo_topup = eval(input("\nNominal Topup: "))
    yakin = input("\nApakah sudah yakin: (y/n)\n").lower()
    if  yakin == "y":
        saldo_total = saldo_sekarang + saldo_topup
        print("\nTotal Saldo Anda Sekarang adalah", saldo_total)
elif menu == "c":
    pembelian = input("\nMasukkan nominal pulsa yang akan dibeli: ")
    if int (pembelian) <= saldo_sekarang:
        print("\nPembelian Pulsa Anda Berhasil!")
    else:
        print("\nMaaf, Saldo Tidak Mencukupi. Silahkan Top Up Terlebih Dahulu.")
else:
    print("\n-------    Pilihan Tidak Ada Pada Menu    -------")