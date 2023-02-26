import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
 
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
officialPrediction = "initial message"
offset = 20
imgSize = 500
 

def get_video_stream():
    labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    officialPrediction = "nope"
    while True:
        success, img = cap.read()
        imgOutput = img.copy()
        
        hands, img = detector.findHands(img)
        if hands:
            hand = hands[0]
            x, y, w, h = hand["bbox"]
    
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            #imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
            imgCrop = img[50:450, 0:640]  
            aspectRatio = h / w
    
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                
                
            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                if imgCrop is not None:
                    imgResize = cv2.resize(imgCrop,(imgSize, hCal))        
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
            
            cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)
            imgOutput = cv2.flip(imgOutput,1)
            cv2.rectangle(imgOutput, (290, 460), (345, 410), (255, 0, 255), cv2.FILLED)
            cv2.putText(imgOutput, labels[index], (300, 480 -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
            print(x)
            print(y)
            
            officialPrediction = labels[index]
        else:
            officialPrediction = ""
            imgOutput = cv2.flip(imgOutput,1)
        ret, imgOutput = cv2.imencode('.jpg', imgOutput)

        # Convert the JPEG buffer to bytes and yield it to Flask
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + imgOutput.tobytes() + b'\r\n'

        
        cv2.waitKey(1)
    cap.release()

def getPrediction():
    return officialPrediction
