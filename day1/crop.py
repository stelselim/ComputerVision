import image_utils
import cv2

img = image_utils.getImage("image.png")

# Crop half of the image from bottom.
# And 2/3 of the width
croppedImage = img[0:image_utils.getImageHeight(img)//2, 0:image_utils.getImageWidth(img)*2//3]
cv2.imshow("cropped-image",croppedImage)
cv2.imshow("image",img)
cv2.waitKey(0)
