import os
import cv2

img_path = os.path.join('spiderman.png')

if not os.path.exists(img_path):
    print("No Item")
img = cv2.imread(img_path)


converted_image = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
converted_image2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
converted_image3 = cv2.cvtColor(converted_image2,cv2.COLOR_GRAY2RGB)
cv2.imshow("Image",img)
cv2.imshow("Image2",converted_image)
cv2.imshow("Image3",converted_image2)
cv2.imshow("Image4",converted_image3)
cv2.waitKey(0);