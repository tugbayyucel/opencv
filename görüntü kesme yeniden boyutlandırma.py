import cv2

path = "ayasofya.jpg"

img = cv2.imread(path)
print(img.shape)

widht,height=400,400
imgRes = cv2.resize(img,(widht,height))
imgCrop = img[200:450,0:690]
imgCropRes = cv2.resize(imgCrop,(img.shape[1],img.shape[0]))


cv2.imshow("normal",img)
cv2.imshow("resize",imgRes)
cv2.imshow("Crop",imgCrop)
cv2.imshow("Crop Resize",imgCropRes)

cv2.waitKey(0)
cv2.destroyAllWindows()
