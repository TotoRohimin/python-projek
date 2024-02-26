import cv2
import numpy as np


def rgb_to_hs(rgb):
    # Ubah RGB ke bentuk float32
    rgb_float32 = rgb.astype(np.float32) / 255.0

    # Hitung nilai maksimum dan minimum dari setiap saluran
    max_val = np.max(rgb_float32, axis=2)
    min_val = np.min(rgb_float32, axis=2)

    # Hitung nilai Delta (selisih antara maksimum dan minimum)
    delta = max_val - min_val

    # Inisialisasi saluran Hue
    h = np.zeros_like(max_val)

    # Hitung Hue
    h[max_val == min_val] = 0  # Jika delta = 0, Hue = 0
    h[max_val != min_val] = 60 * (((rgb_float32[max_val != min_val, 1] -
                                  rgb_float32[max_val != min_val, 2]) / delta[max_val != min_val] + 6) % 6)

    # Inisialisasi saluran Saturation
    s = np.zeros_like(max_val)
    s[max_val != 0] = delta[max_val != 0] / max_val[max_val != 0]

    # Hitung nilai luminansi (brightness)
    v = max_val

    # Gabungkan saluran Hue, Saturation, dan Luminance
    hs = np.dstack((h, s, v))

    return hs


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

    # Ubah RGB ke HS
    hs = rgb_to_hs(rgb)

    # Tampilkan hasil
    print("Hasil Transformasi RGB ke HS:")
    print(hs)


if __name__ == "__main__":
    main()
