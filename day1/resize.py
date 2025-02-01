import os
import cv2 


image_path = os.path.join(".","image.png")

img = cv2.imread(image_path)
height, width, channel = img.shape
resizedImage = cv2.resize(img,(width//2,height//2))

print(img.shape)
print(resizedImage.shape)

cv2.imshow('image1',img)
cv2.imshow('image2',resizedImage)
cv2.waitKey(2500)

cv2.imwrite('resizedImage.png',resizedImage)