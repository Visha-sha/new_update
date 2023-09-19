import cv2
frameHeight=315
frameWidth=500
img=cv2.imread("download.jpg")
img=cv2.resize(img,(frameWidth,frameHeight))
cv2.imshow("car",img)
cv2.waitKey(0)
