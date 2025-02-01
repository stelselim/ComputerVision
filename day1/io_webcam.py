import cv2
import numpy as np

# I do not know why but numpy arrays are super slow.
# Here, I made a mirror screen kind of feature for camera.
def reverseFrame(frame): 
    array = []
    for row in frame:
        reversedRow = row[::-1]
        array.append(reversedRow)
    reversed_frame = np.array(array)
    return reversed_frame

webcam = cv2.VideoCapture(1)
print(webcam);

ret = True

while ret:
    ret, frame = webcam.read()
    if ret:
        reversedFrame = reverseFrame(frame)
        cv2.imshow('frame',reversedFrame)
        fpsCount=60
        cv2.waitKey(1000//fpsCount) # Makes low frame rate

webcam.release()
cv2.destroyAllWindows

