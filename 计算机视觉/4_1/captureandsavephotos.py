# -*- coding: utf-8 -*-

import cv2
import time
 
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width (文档代码有误，设置宽高应为3,4)
cap.set(4,480) # set Height
time.sleep(2)


for i in range(100):# 拍100张图片就结束
    ret, img = cap.read()
    cv2.imshow('img', img)
    images="images"+str(i)+".jpg"
    cv2.imwrite(images, img)
    
	# Press 'ESC' for exiting video
    k = cv2.waitKey(100) & 0xff 
    if k == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
