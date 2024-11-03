# Fungsi lambda untuk mengonversi Celsius ke Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

# Fungsi lambda untuk mengonversi Fahrenheit ke Celsius
fahrenheit_to_celsius = lambda f: (f - 32) * 5/9

# Contoh penggunaan
celsius = 25
fahrenheit = 77

print(f"{celsius}°C ke Fahrenheit: {celsius_to_fahrenheit(celsius)}°F")
print(f"{fahrenheit}°F ke Celsius: {fahrenheit_to_celsius(fahrenheit)}°C")
