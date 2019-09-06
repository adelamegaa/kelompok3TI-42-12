print("\nGiveaway Telkom University\n")

ipk = float(input("IPK : "))
provider = input("Provider : ")

if ipk >= 3 and provider == "telkomsel":
    print("Mendapatkan Iphone X")
elif ipk >= 3 and provider != "telkomsel":
    print("Mendapatkan Samsung J Series")
elif (ipk < 3 or ipk >= 2.5) and provider == "telkomsel":
    print("Mendapatkan PS4")
elif (ipk < 3 or ipk >= 2.5) and provider != "telkomsel":
    print("Mendapatkan Voucher Menginap Gratis di IBIS Trans Studio Mall")
elif (ipk < 2.5 or ipk >= 2) and provider == "telkomsel":
    print("Mendapatkan Voucher Gratis Menginap di Pesantren Darul")
elif (ipk < 2.5 or ipk >= 2) and provider != "telkomsel":
    print("Mendapatkan Voucher Konsultasi Psikolog Gratis")
else:
    print("Mendapatkan Surat Ucapan Selamat dan Terima Kasih")