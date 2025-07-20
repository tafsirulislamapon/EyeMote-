import cv2
import mediapipe as mp
import pyautogui


cam = cv2.VideoCapture(0)
faceMesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screenW, screenH = pyautogui.size()

while True :
    _ , frame = cam.read()
    frame = cv2.flip(frame, 1)

    rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = faceMesh.process(rgbFrame)
    landMarkPoints = output.multi_face_landmarks
    
    frameH , frameW , _ = frame.shape 

    # print(landMarkPoints)
    if landMarkPoints : 
        landMarks = landMarkPoints[0].landmark
        #for landmark in landMarks : 
        for id, landmark in enumerate(landMarks[474 : 478]) : #it will only focus on the eyes 
            x = int(landmark.x * frameW) 
            y = int(landmark.y * frameH)
            cv2.circle(frame, (x , y),  3 , (0, 255 , 0))
            #print(x,y)=
            if id == 1 :
                screen_X = screenW / frameW * x
                screen_Y = screenH / frameW * y

                pyautogui.moveTo(screen_X , screen_Y)


    cv2.imshow('Eye controlled mouse' , frame)
    cv2.waitKey(1)

