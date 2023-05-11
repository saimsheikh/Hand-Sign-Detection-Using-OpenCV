import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=2)

while True:
    success, img = cap.read()
    if not success:
        continue  # Skip the iteration if the image is not read successfully
    hands, img = detector.findHands(img)
    cv2.imshow("Image", img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break 