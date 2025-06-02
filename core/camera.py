# core/camera.py
import cv2
import os
from datetime import datetime

OUTPUT_DIR = "assets/output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def capture_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        filename = f"{OUTPUT_DIR}/capture_{timestamp()}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Foto salva como: {filename}")
    else:
        print("❌ Erro ao capturar imagem.")
    cap.release()


def record_video(duration=5):
    cap = cv2.VideoCapture(0)
    width = int(cap.get(3))
    height = int(cap.get(4))
    filename = f"{OUTPUT_DIR}/video_{timestamp()}.avi"
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))

    print("🎥 Gravando...")
    frame_count = 20 * duration
    while frame_count > 0:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            frame_count -= 1
        else:
            break

    cap.release()
    out.release()
    print(f"🎬 Vídeo salvo como: {filename}")


def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")
  
