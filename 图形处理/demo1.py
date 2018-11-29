#encoding:utf-8

#
#图像的逻辑运算
#

import numpy as np
import cv2

#画矩形
Rectangle = np.zeros((300,300),dtype="uint8")
cv2.rectangle(Rectangle,(25,25),(275,275),255,-1)
cv2.imshow("Rectangle",Rectangle)
# cv2.waitKey(0)

#画圆形
Circle = np.zeros((300,300),dtype="uint8")
cv2.circle(Circle,(150,150),150,255,-1)
cv2.imshow("Circle",Circle)
# cv2.waitKey(0)

#图像的交
bitwiseAnd = cv2.bitwise_and(Rectangle,Circle)
cv2.imshow("AND",bitwiseAnd)
cv2.waitKey(0)
