import cv2

cap = cv2.VideoCapture(0)  # Gerekirse 1 yap
ret, frame = cap.read()
cap.release()

if ret:
    cv2.imwrite("test.jpg", frame)
    print("Görüntü kaydedildi: test.jpg")
else:
    print("Kamera görüntüsü alınamadı.")
