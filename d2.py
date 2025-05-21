from insightface.app import FaceAnalysis
import cv2

app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=-1)  # CPU için -1, CUDA düzgün çalışıyorsa 0

img = cv2.imread("test.jpg")
faces = app.get(img)

print(f"Bulunan yüz sayısı: {len(faces)}")
if faces:
    print("Yüz başarıyla algılandı.")
else:
    print("Yüz algılanamadı.")
