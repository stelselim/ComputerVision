import os
import cv2 

def getImage(path):
    image_path = os.path.join('.',path)
    return cv2.imread(image_path)


def getImageHeight(imageArr):
    height, _,_ = imageArr.shape;
    return height

def getImageWidth(imageArr):
    _, width,_ = imageArr.shape;
    return width