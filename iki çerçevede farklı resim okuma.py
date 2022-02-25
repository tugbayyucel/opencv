import cv2

resim = cv2.imread("ayasofya.jpg") #birinci resim
resim2 = cv2.imread("a.gri.jpg")#ikinci resim

cv2.imshow("cerceve",resim) #açılacak çerçeve 1
cv2.imshow("cerceve2",resim2) #açılacak çerçeve 2

cv2.waitKey()
cv2.destroyAllWindows()
