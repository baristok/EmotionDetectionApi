from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
import tensorflow as tf
from io import BytesIO
from PIL import Image

app = FastAPI()

model = tf.keras.models.load_model(r'C:\EmotionDetection\emotiondetector.h5')
haar_file = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)

labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0

@app.post("/api")
async def predict_emotion(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(BytesIO(image_bytes)).convert("L")
    image = np.array(image)
    

    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    if len(faces) == 0:
        return {"error": "No face detected"}

    for (p, q, r, s) in faces:
        cropped_face = image[q:q+s, p:p+r]
        resized_face = cv2.resize(cropped_face, (48, 48))
        img = extract_features(resized_face)
        pred = model.predict(img)
        prediction_label = labels[np.argmax(pred)]
        return {"emotion": prediction_label}

    return {"error": "No emotion detected"}

