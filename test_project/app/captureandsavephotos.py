# -*- coding: utf-8 -*-
'''
使用web摄像头 (USB摄像头)捕捉图像并保存
'''
import os
import shutil

import cv2
import time
import sys

cap = cv2.VideoCapture(0)
cap.set(0, 640)  # set Width (the first parameter is property_id)
cap.set(1, 480)  # set Height
time.sleep(2)

images_dir = sys.argv[1]
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

for i in range(8):  # 拍8张图片就结束
    ret, img = cap.read()
    cv2.imshow('img', img)
    cv2.imwrite(images_dir + '/%d.jpg' % (i), img)

    # Press 'ESC' for exiting video
    k = cv2.waitKey(8) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
