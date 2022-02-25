import cv2

# Kullanılacak materyaller kodlarla aynı klasör içinde olmalıdır.
# Kodlamayla yapılan değişiklikler ve kaydetmeler aynı klasöre kaydedilir.
# İstediğiniz resimler üzerinde çalışma yapabilirsiniz.

resim=cv2.imread("resim.jpg",0) #resmi göster ve tonunu değiştir.
                                #0 tonlama yapar

cv2.imshow("cerceve",resim)  #resmin açılacağı çerçeve
cv2.imwrite("kitap_gri.jpg",resim) #Değişen tonlamanın ne olarak
                                    #kaydedileceği

cv2.waitKey(0) #Pencerenin açık kalma süresi. Ms değerinde giriş yapılabilir.
cv2.destroyAllWindows() #tüm pencereleri kapatır.


