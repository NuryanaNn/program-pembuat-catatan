from colorama import Fore, Style, init

init(autoreset=True)

# Inisialisasi dictionary untuk menyimpan catatan
catatan = {}

def clear_screen():
    print("\033c", end="")

def display_menu():
    clear_screen()
    print(Fore.CYAN + "Aplikasi Pembuat Catatan" + Style.RESET_ALL)
    print("-" * 24)
    print(Fore.GREEN + "1. Tambah Catatan")
    print("2. Lihat Catatan")
    print("3. Hapus Catatan")
    print(Fore.RED + "4. Keluar" + Style.RESET_ALL)

def tambah_catatan():
    clear_screen()
    print(Fore.CYAN + "Tambah Catatan" + Style.RESET_ALL)
    judul = input("Masukkan judul catatan: ")
    isi = input("Masukkan isi catatan: ")
    catatan[judul] = isi
    print(Fore.GREEN + f"Catatan '{judul}' telah ditambahkan." + Style.RESET_ALL)

def lihat_catatan():
    clear_screen()
    print(Fore.CYAN + "Lihat Catatan" + Style.RESET_ALL)
    if not catatan:
        print(Fore.YELLOW + "Tidak ada catatan saat ini." + Style.RESET_ALL)
    else:
        print("Daftar Catatan:")
        for judul, isi in catatan.items():
            print(Fore.GREEN + f"Judul: {judul}" + Style.RESET_ALL)
            print(f"Isi: {isi}")
            print("-" * 20)

def hapus_catatan():
    clear_screen()
    print(Fore.CYAN + "Hapus Catatan" + Style.RESET_ALL)
    judul = input("Masukkan judul catatan yang akan dihapus: ")
    if judul in catatan:
        del catatan[judul]
        print(Fore.GREEN + f"Catatan '{judul}' telah dihapus." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"Catatan dengan judul '{judul}' tidak ditemukan." + Style.RESET_ALL)

while True:
    display_menu()
    pilihan = input("Masukkan nomor menu (1/2/3/4): ")

    if pilihan == '4':
        print(Fore.RED + "Keluar dari aplikasi Pembuat Catatan." + Style.RESET_ALL)
        break

    if pilihan not in ('1', '2', '3'):
        input(Fore.YELLOW + "Pilihan tidak valid. Tekan Enter untuk melanjutkan." + Style.RESET_ALL)
        continue

    if pilihan == '1':
        tambah_catatan()
    elif pilihan == '2':
        lihat_catatan()
    elif pilihan == '3':
        hapus_catatan()

    input("Tekan Enter untuk melanjutkan...")
