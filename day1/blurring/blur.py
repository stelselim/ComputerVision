import os
import cv2

img = cv2.imread(os.path.join('spiderman.png'))

cv2.imshow("image", img)
ksize = 20
blurred = cv2.blur(img,(ksize,ksize))
cv2.imshow("BlurredImage", blurred)
#cv2.imwrite("blurred_spiderman.png",blurred)

# Gaussian Blur requires different ksize, no idea for now. Need to check the reason later.
gaussian_blurred = cv2.GaussianBlur(img,(ksize+1,ksize+1),5);
median_blur = cv2.medianBlur(img,ksize=ksize+1);

cv2.imshow("Gaussian BlurredImage", gaussian_blurred)
cv2.imshow("Median BlurredImage", median_blur)

cv2.waitKey(0)


