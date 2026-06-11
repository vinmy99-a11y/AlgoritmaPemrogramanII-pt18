import os

nama_file = "data_mahasiswa.txt"

# Cek apakah file sudah ada
if not os.path.exists(nama_file):
    # Jika file tidak ada, buat file baru dan tulis tiga nama
    with open(nama_file, "w") as f:
        f.write("Andi Pratama\n")
        f.write("Budi Santoso\n")
        f.write("Citra Dewi\n")
    print(f"File {nama_file} berhasil dibuat!")
else:
    # Jika file sudah ada, tambahkan tulisan
    with open(nama_file, "w") as f:
        f.write("Andi Pratama\n")
        f.write("Budi Santoso\n")
        f.write("Citra Dewi\n")
    print(f"File {nama_file} sudah ada, data ditulis ulang!")