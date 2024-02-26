def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Mengembalikan indeks elemen yang ditemukan
    return -1  # Mengembalikan -1 jika elemen tidak ditemukan


# Contoh penggunaan:
data = [10, 23, 4, 67, 18, 45, 27, 6, 34]
target_element = 4

result = linear_search(data, target_element)

if result != -1:
    print(f"Elemen {target_element} ditemukan di indeks {result}")
else:
    print(f"Elemen {target_element} tidak ditemukan dalam array.")
