# Fungsi untuk input dengan validasi
def get_input(prompt, valid_fn, error_message):
    while True:
        try:
            value = float(input(prompt))  # Gunakan float untuk menangani angka desimal
            if valid_fn(value):
                return value
            else:
                print(error_message)
        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang sesuai.")

# Fungsi untuk menampilkan total biaya
def print_cost(final_cost):
    print("="*60)
    print(f"{'Total Biaya Pengiriman':<40}{'Rp ' + format(final_cost, ','):>20}")
    print("="*60)

# Fungsi untuk menampilkan informasi pembuat
def print_footer():
    
    print(f"Nama: Muhammad Said Abimanyu".center(60))
    print(f"Tugas: Logika Informatika".center(60))
    print(f"NIM: {312410145}".center(60))

# Header program
print("="*60)
print(" " * 20 + "~ Program Biaya Pengiriman ~" + " " * 20)
print("="*60)

# Input berat dan jarak dengan validasi
weight = get_input("Masukkan berat paket anda [kg]: ", lambda w: w > 0, "Berat paket harus lebih dari 0.")
distance = get_input("Masukkan jarak pengiriman anda [km]: ", lambda d: d > 0, "Jarak pengiriman harus lebih dari 0.")

# Pilih jenis layanan
service_type = ""
while service_type not in ['express', 'reguler']:
    service_type = input("Pilih jenis layanan anda (express/reguler): ").strip().lower()
    if service_type not in ['express', 'reguler']:
        print("Jenis layanan tidak valid. Pilih 'express' atau 'reguler'.")

# Pilih status pelanggan (setia atau tidak)
loyalty_status = ""
while loyalty_status not in ['ya', 'tidak']:
    loyalty_status = input("Apakah Anda member disini? (Ya/Tidak): ").strip().lower()
    if loyalty_status not in ['ya', 'tidak']:
        print("Pilihan tidak valid. Pilih 'Ya' atau 'Tidak'.")

# Biaya dasar
base_cost = 10000

# Menghitung biaya berdasarkan berat, jarak, dan layanan
final_cost = base_cost
if weight * 1000 > 5000:  # Berat lebih dari 5 kg
    final_cost += 5000
if distance * 1000 > 10000:  # Jarak lebih dari 10 km
    final_cost += 8000
if service_type == 'express':  # Layanan Express
    final_cost += 20000

# Diskon untuk member (10%)
if loyalty_status == 'ya':
    final_cost *= 0.90  # Diskon 10%

# Tampilkan biaya pengiriman
print_cost(final_cost)

# Tampilkan informasi pembuat
print_footer()
