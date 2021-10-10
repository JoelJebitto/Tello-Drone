import cv2
import numpy as np

img_rgb = np.zeros((100,100), dtype=np.float32)
img_hsv = np.zeros((100,100), dtype=np.float32)

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

def print_pixel(event,x,y,flags,param):    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f"X={x},Y={y}")
        print(f"RGB=({img_rgb[y,x,0]},{img_rgb[y,x,1]},{img_rgb[y,x,2]})")
        print(f"HSV=({img_hsv[y,x,0]},{img_hsv[y,x,1]},{img_hsv[y,x,2]})")

while True:

    _, img = cap.read()
    imgContour = img.copy()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    cv2.imshow('Horizontal Stacking', imgContour)
    
    if cv2.waitKey(1) & 0xFF == ord('o'):        
        print("o pressed")
        img_rgb = img.copy()
        img_hsv = imgHsv.copy()
        cv2.imshow('Pixel Value', img_rgb)
        cv2.setMouseCallback('Pixel Value',print_pixel)
                
    if cv2.waitKey(1) & 0xFF == ord('p'):
        print(imgHsv)

        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break