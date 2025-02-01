import os 
import cv2

# ------ Read Images ------
image_path = os.path.join('.','image.png')
img = cv2.imread(image_path)
# print("Image Shape: ",img.shape)
# print(img[0])

# ----------------

# Best way to get image size, is len function.
# print(len(img))
# print(img[0].shape)
# img[0] -> 0,0
# print(img[1].shape)

# print(img[0][0]) # Pixel
# print(img[0][0][0]) # Pixel Red Color
# print(img[0][0][1]) # Pixel Green Color
# print(img[0][0][2]) # Pixel Blue Color

# ----------------

# How to get the pixel in the middle of the image.
# img -> (x,y,(pixel array RGB))
midY = len(img)//2 #Takes height array
midX = len(img[0])//2 #img[0], Takes width array, then mid point.
# print(img[midY][midX]) # Correct Answer



# ------ Writing Images ------
cv2.imwrite(os.path.join('.',"newimage.png"),img) # Writes the same image.

# ------ Visualize Image ------
cv2.imshow('image',img)
keyDelay = 1000
cv2.waitKey(keyDelay) #If the delay is 0, it will wait indefinitely.

