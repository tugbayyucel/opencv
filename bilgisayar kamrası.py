import cv2

frameWidht = 640 #çerçeve en
frameHeight = 360 #çerçeve boy

cap = cv2.VideoCapture(0) #Bilgisayara entegre kamerayı açmak için 0
                          # sonradan bağlanan kamera için 1
                          # video için "" içinde video ve formatı yazılır

#while döngüsüyle kameradan alınan görüntünün en boy oranını üstte
# tanımlanan verilerle eşleştiriliyor.
while True:
    success,img = cap.read()
    img=cv2.resize(img,(frameWidht,frameHeight)) 
    cv2.imshow("video1",img)
    
#kamerayı kapatmak için X işareti değil buradaki harfi kullanmak için.
    if cv2.waitKey(25) & 0XFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
