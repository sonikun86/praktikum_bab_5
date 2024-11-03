def cek_trio_ajaib(a, b, c):
    # Menggunakan set untuk memastikan angka berbeda
    if len({a, b, c}) != 3:
        return False
    
    # Memeriksa apakah ada kombinasi dua angka yang dijumlahkan sama dengan angka ketiga
    return (a + b == c) or (a + c == b) or (b + c == a)

# Contoh penggunaan
print(cek_trio_ajaib(3, 4, 7))  # True
print(cek_trio_ajaib(1, 2, 3))  # True
print(cek_trio_ajaib(4, 6, 11)) # False
print(cek_trio_ajaib(1, 1, 3))  # False
