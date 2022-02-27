import cv2
import numpy as np

#Pencerenin boyutunu manuel ayarlamak
frameWidht = 640 #çerçeve en
frameHeight = 360 #çerçeve boy

cap = cv2.VideoCapture(0) #Bilgisayara entegre kamerayı açmak için 0
                          # sonradan bağlanan kamera için 1
                          # video için "" içinde video ve formatı yazılır
cap.set(3,frameWidht)
cap.set(4,frameHeight)

def empty(a):
    pass

#Trackbar oluşturma
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",648,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("Value Min","HSV",0,255,empty)
cv2.createTrackbar("Value Max","HSV",0,255,empty)


#kamera görüntüsünü HSV ye döndürme
while True:
    _,img=cap.read()
    imgHsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#Trackbarı atama
    h_min=cv2.getTrackbarPos("HUE Min","HSV")
    h_max=cv2.getTrackbarPos("HUE Max","HSV")
    s_min=cv2.getTrackbarPos("SAT Min","HSV")
    s_max=cv2.getTrackbarPos("SAT Max","HSV")
    v_min=cv2.getTrackbarPos("Value Min","HSV")
    v_max=cv2.getTrackbarPos("Value Max","HSV")
    print(h_min)

#Kamera track bar uygulama
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(imgHsv,lower,upper)
    result=cv2.bitwise_and(img,img,mask=mask)
    
#Tek pencerede görüntüleme
    mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    hstack=np.hstack([img,mask,result])
#Ayrı pencerelerde görüntüleme    
    #cv2.imshow("original",img)
    #cv2.imshow("HSV image",imgHsv)
    #cv2.imshow("mask",mask)
    #cv2.imshow("result",result)

#Tek pencerede görüntüleme
    cv2.imshow("genel",hstack)
 
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
