def cocokkan_produk(kode1, kode2, kode3):
    # Mengambil digit terakhir dari setiap kode produk
    last_digit1 = kode1 % 10
    last_digit2 = kode2 % 10
    last_digit3 = kode3 % 10

    # Memeriksa apakah minimal dua digit terakhir sama
    return (last_digit1 == last_digit2) or (last_digit1 == last_digit3) or (last_digit2 == last_digit3)

# Test cases
print(cocokkan_produk(900, 10, 38))  # Output: True
print(cocokkan_produk(276, 6, 75))   # Output: True
print(cocokkan_produk(63, 391, 108))  # Output: False
print(cocokkan_produk(654, 24, 74))   # Output: True
