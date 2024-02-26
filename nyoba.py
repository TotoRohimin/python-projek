import cv2
import numpy as np
from matplotlib import pyplot as plt

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak dapat diakses.")
    exit()

# Membaca frame dari kamera
ret, frame = cap.read()

if not ret:
    print("Gagal membaca frame dari kamera.")
    exit()

# Menyimpan frame sebagai gambar
cv2.imwrite('captured_image.jpg', frame)

# Menghitung histogram
histogram = cv2.calcHist([frame], [0], None, [256], [0, 256])

# Menampilkan gambar yang diambil
cv2.imshow('Captured Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menampilkan histogram
plt.plot(histogram)
plt.title('Histogram Gambar')
plt.xlabel('Intensitas Pixel')
plt.ylabel('Frekuensi')
plt.show()

# Menutup kamera
cap.release()
