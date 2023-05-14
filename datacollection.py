import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)
offset = 20
ImgSize=300

counter=0
folders="data/a"


while True:
    success, img = cap.read()
    if not success:
        continue  # Skip the iteration if the image is not read successfully
    hands, img = detector.findHands(img)
    #croping the image
    if hands:
        hand = hands[0]
        x,y,w,h=hand['bbox']
        imgwhite=np.ones((ImgSize,ImgSize,3),np.uint8)*255
        imgcrop=img[y-offset:y+h+offset,x-offset:x+w+offset]

        
        #fow fixed height
        aspectRatio = h/w

        if aspectRatio>1:
                k=ImgSize/h
                newWidth=math.ceil(k*w)
                Imgresize=cv2.resize(imgcrop,(newWidth,ImgSize))
                wgap=math.ceil((ImgSize-newWidth)/2)
                imgwhite[:,wgap:newWidth+wgap] = Imgresize
        else:
                k=ImgSize/w
                newHeight=math.ceil(k*h)
                Imgresize=cv2.resize(imgcrop,(ImgSize,newHeight))
                hgap=math.ceil((ImgSize-newHeight)/2)
                imgwhite[hgap:newHeight+hgap,:] = Imgresize



        #startinh height and width , as well ending
        cv2.imshow("ImageCrop", imgcrop)
        cv2.imshow("Imagewhite", imgwhite)



    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break 
    elif key == ord('s'):
        counter += 1
        print("Image saved")
        cv2.imwrite(f'{folders}/{counter}.jpg',imgwhite)
        print(counter)
        
