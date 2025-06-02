core/detector.py

import cv2 import numpy as np

Lista de classes COCO usadas pelo modelo MobileNet SSD (exemplo simplificado)

CLASSES = [ "background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor" ]

Caminho dos pesos pré-treinados do modelo MobileNet SSD

MODEL_PROTO = "assets/models/MobileNetSSD_deploy.prototxt" MODEL_WEIGHTS = "assets/models/MobileNetSSD_deploy.caffemodel"

net = cv2.dnn.readNetFromCaffe(MODEL_PROTO, MODEL_WEIGHTS)

def detect_objects(target_label=None): cap = cv2.VideoCapture(0) found = []

print("🔍 Procurando objetos...")
ret, frame = cap.read()
if not ret:
    print("❌ Erro ao acessar a câmera.")
    return []

h, w = frame.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                             0.007843, (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.4:
        idx = int(detections[0, 0, i, 1])
        label = CLASSES[idx]

        if (target_label is None) or (target_label.lower() in label.lower()):
            found.append(label)

cap.release()
return list(set(found))  # remove duplicatas

