import cv2
import numpy as np


def rgb_to_xyz(rgb):
    # Matriks transformasi RGB ke XYZ
    matrix = np.array([[0.4124564, 0.3575761, 0.1804375],
                       [0.2126729, 0.7151522, 0.0721750],
                       [0.0193339, 0.1191920, 0.9503041]])

    # Normalisasi nilai RGB
    rgb_normalized = rgb / 255.0

    # Transformasi RGB ke XYZ
    xyz = np.dot(rgb_normalized, matrix.T)

    return xyz


def main():
    # Baca citra RGB
    img_path = 'captured_image.jpg'
    img = cv2.imread(img_path)

    if img is None:
        print(f"File {img_path} tidak ditemukan.")
        return

    # Ubah citra ke format float32
    img_float32 = img.astype(np.float32)

    # Pisahkan saluran warna RGB
    b, g, r = cv2.split(img_float32)

    # Gabungkan saluran warna ke dalam array
    rgb = np.dstack((r, g, b))

    # Ubah RGB ke XYZ
    xyz = rgb_to_xyz(rgb)

    # Tampilkan hasil
    print("Hasil Transformasi RGB ke XYZ:")
    print(xyz)


if __name__ == "__main__":
    main()
