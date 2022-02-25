import cv2
import numpy as np

circles = np.zeros((4,2),np.int_)
counter=0

def mousePoint(event,x,y,flags,param):
    global counter
    if event ==cv2.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter = counter +1
        print(circles)

cv2.namedWindow("myImage",cv2.WINDOW_NORMAL)
img = cv2.imread("klavye.jpeg")
while True:

    if counter ==4:
        width,heihgt = 56,28
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[widht,0],[0,height],[widht,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img,matrix,(widht,height))
        cv2.imshow("kusbakisi",output)

    for x in range (0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),5,(255,0,0),cv2.FILLED)


cv2.imshow("myImage",img)
cv2.setMouseCallback("myImage",mousePoint)
cv.waitKey(1)
