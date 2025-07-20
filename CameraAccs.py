import cv2

cam = cv2.VideoCapture(0)

# access to camera, by just using cv2 package!
while True :
    _ , frame = cam.read()
    frame = cv2.flip(frame, 1)
    
    cv2.imshow('Eye controlled mouse' , frame)
    cv2.waitKey(1)

