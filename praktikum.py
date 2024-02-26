import cv2
import numpy as np

# 1. Membaca Citra
# Gantilah 'input.jpg' dengan nama file citra Anda
image = cv2.imread('captured_image.jpg')

# 2. Operasi Titik (Misalnya, mengubah ke tingkat keabuan)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Operasi Spasial (Misalnya, deteksi tepi dengan filter Sobel)
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
edge_image = cv2.magnitude(sobel_x, sobel_y)

# 4. Operasi Transformasi (Misalnya, rotasi)
rows, cols = gray_image.shape
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (cols, rows))

# 5. Menampilkan Hasil
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)
cv2.imshow('Edge Image', edge_image)
cv2.imshow('Rotated Image', rotated_image)

# Tunggu tombol keyboard dan kemudian tutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
