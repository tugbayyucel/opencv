import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #tamsayı kullanımı için unit8

print(img.shape)

#img[:] = 255,75,155 #çerçeveye renk tanımlaması

#başlangıç noktası, bitiş noktası ,renk ve renk kanalı
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #çizgi çizmek
#başlangıç noktası,bitiş noktası,renk ve içini doldurmak
cv2.rectangle(img,(110,200),(450,140),(0,250,250),cv2.FILLED)#dikdörtgen çizmek
#başlangıç noktası, yarıçap, renk ve renk kanalı
cv2.circle(img,(150,400),75,(255,255,56),3)#daire çizmek
# yazılacak metin , başlangıç noktası,font,font boyutu ve renk
cv2.putText(img,"Tugbay Yucel",(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,150),2)
#yazı yazmak

cv2.imshow("karaResim",img)

cv2.waitKey(0)
