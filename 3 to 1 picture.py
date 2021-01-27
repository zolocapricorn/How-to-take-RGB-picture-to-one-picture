import numpy as np
import cv2

image_red, image_green, image_blue = cv2.imread("blue.jpg"), cv2.imread("green.jpg"), cv2.imread("red.jpg") #สลับ BGR เป็น RGB เรียบร้อยละผ่านตัวแปร
red_c= cv2.resize(image_red, (1188, 1067))
green_c = cv2.resize(image_green, (1188, 1067))
blue_c = cv2.resize(image_blue, (1188, 1067))

red = red_c[0:1188, 41:1067]
green = green_c[20:1188, 20:1067]
blue = blue_c[0:1188, 1:1067]

f_red= cv2.resize(red, (1188, 1067))
f_green = cv2.resize(green, (1188, 1067))
f_blue = cv2.resize(blue, (1188, 1067))

(blue_1, green_1, red_1)= cv2.split(f_red) # Split the three channels of the image
(blue_2, green_2, red_2) = cv2.split(f_green)# เป็น BGR
(blue_3, green_3, red_3) = cv2.split(f_blue)

merged = cv2.merge((red_1, green_2, blue_3)) #เรียงแบบ BGR
cv2.imshow("Merged", merged)
cv2.waitKey()
