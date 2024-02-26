import cv2


def deteksi_wajah(foto):
    # Mengonversi gambar menjadi skala abu-abu (grayscale)
    foto_abu = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)

    # Menggunakan klasifikasi wajah pre-trained dari OpenCV
    klasifikasi_wajah = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Mendeteksi wajah dalam gambar
    wajah = klasifikasi_wajah.detectMultiScale(
        foto_abu, scaleFactor=1.1, minNeighbors=5)

    # Menggambar kotak pembatas di sekitar wajah yang terdeteksi
    for (x, y, w, h) in wajah:
        cv2.rectangle(foto, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Menampilkan gambar dengan kotak pembatas wajah
    cv2.imshow('Deteksi Wajah', foto)


# Inisialisasi objek VideoCapture untuk mengakses webcam
webcam = cv2.VideoCapture(0)

while True:
    # Membaca frame dari webcam
    ret, frame = webcam.read()

    # Menjalankan fungsi deteksi_wajah untuk setiap frame
    deteksi_wajah(frame)

    # Menghentikan loop jika pengguna menekan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepas sumber daya webcam dan menutup jendela tampilan
webcam.release()
cv2.destroyAllWindows()
