# 1. Fungsi get_input:
Fungsi ini digunakan untuk meminta input dari pengguna dan memastikan input tersebut valid (sesuai dengan kriteria yang ditentukan). Misalnya, hanya menerima angka positif.
Jika input salah (misalnya bukan angka), maka akan muncul pesan kesalahan dan program akan meminta input lagi.
# 2. Fungsi print_cost:
Fungsi ini digunakan untuk menampilkan total biaya pengiriman dalam format yang rapi.
Biaya ditampilkan dalam format Rp xxxxx dan dibatasi agar hasilnya tampak rapi di layar.
# 3. Fungsi print_footer:
Fungsi ini digunakan untuk menampilkan informasi pembuat program, yaitu nama, tugas, dan NIM pembuat program.
Semua informasi ini ditampilkan di bagian bawah program setelah total biaya pengiriman.
# 4. Bagian Utama Program:
Minta input: Program meminta pengguna untuk memasukkan berat paket, jarak pengiriman, jenis layanan (express atau reguler), dan status keanggotaan (apakah member atau bukan).
Menghitung Biaya:
Biaya dasar sudah ditetapkan (Rp 10.000).
Kemudian, program menambahkan biaya berdasarkan berat dan jarak pengiriman, serta jenis layanan yang dipilih.
Jika pengguna adalah member (status "ya"), maka ada diskon 10%.
Menampilkan Hasil: Setelah biaya dihitung, program akan menampilkan total biaya pengiriman dengan format yang rapi, lalu diikuti dengan informasi pembuat program.
Penjelasan Singkat Proses:
Input: Pengguna diminta memasukkan berat, jarak, layanan, dan status member.
Perhitungan:
Biaya dasar: Rp 10.000
Tambahan biaya: Berdasarkan berat dan jarak pengiriman
Layanan: Jika memilih layanan express, ada biaya tambahan
Diskon: Jika member, ada diskon 10%
Output: Program menampilkan total biaya yang harus dibayar dan informasi pembuat program
# Input
~~~
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
~~~
# Ouput
~~~
============================================================
                    ~ Program Biaya Pengiriman ~
============================================================
Masukkan berat paket anda [kg]: 10
Masukkan jarak pengiriman anda [km]: 20
Pilih jenis layanan anda (express/reguler): express
Apakah Anda member disini? (Ya/Tidak): ya
============================================================
Total Biaya Pengiriman                           Rp 38,700.0
============================================================
                Nama: Muhammad Said Abimanyu
                 Tugas: Logika Informatika
                       NIM: 312410145

============================================================
                    ~ Program Biaya Pengiriman ~
============================================================
Masukkan berat paket anda [kg]: 10
Masukkan jarak pengiriman anda [km]: 20
Pilih jenis layanan anda (express/reguler): express
Apakah Anda member disini? (Ya/Tidak): tidak
============================================================
Total Biaya Pengiriman                             Rp 43,000
============================================================
                Nama: Muhammad Said Abimanyu
                 Tugas: Logika Informatika
                       NIM: 312410145
~~~
sekian dan terimakasih
