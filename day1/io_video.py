import os
import cv2 

# Read Videos

video_path = os.path.join('.','videos','video.mp4')
print(video_path)

if not os.path.exists(video_path):
    print(f"Error No Video File found at {video_path}")
else:
    print("File exits")


video = cv2.VideoCapture(video_path)

# Visualize Videos
ret = True;

while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('frame',frame)
        cv2.waitKey(10)

video.release() #de-allocate memory of the video.
cv2.destroyAllWindows()