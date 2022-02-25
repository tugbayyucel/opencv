# Görüntüde kenarları belirleme
import cv2
import numpy as np

img = cv2.imread("ayasofya.jpg")

laplacian = cv2.Laplacian(img,cv2.CV_64F)

sobel = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) #dikey
sobely = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) #yatay

cv2.imshow("original",img)
cv2.imshow("Laplacian",laplacian)
cv2.imshow("Sobel",sobel)
cv2.imshow("Sobel Yatay",sobely)

