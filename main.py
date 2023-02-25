import cv2
from cvzone.HandTrackingModule import *
import mediapipe as mp

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands= 2)

while True:
    success, img = cap.read()
    
    hands, img = detector.findHands(img)
    
        
    x, y, w, h = hands[0]['bbox']
    imgCrop1 = img[y : y + h, x : x + w]
    cv2.imshow("ImageCrop", imgCrop1)
    cv2.imshow("Image", img)
    cv2.waitKey(1)