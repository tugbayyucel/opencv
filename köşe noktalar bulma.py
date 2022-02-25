import cv2
import numpy as np

img = cv2.imread('dama.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

koseler = cv2.goodFeaturesToTrack(gray,60,0.01,10)
koseler = np.int0(koseler)

for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(img,(x,y),10,(0,255,0),-1)

cv2.imshow('Photo', img)
cv2.waitKey(0)
