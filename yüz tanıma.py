import cv2
import numpy as np

#https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml
#xml dosyasıyla kodlar aynı dizinde kaydedilecektir.
face_casc=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img=cv2.imread("i.jpg")

griton=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_casc.detectMultiScale(griton,1.1,4)

print(faces)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("face",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
