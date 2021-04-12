import cv2
import mediapipe as mp

# Initializing Hand Tracking Modules
mpHands = mp.solutions.hands
Hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


# Capturing Video From Camera 
cap = cv2.VideoCapture(0)

# Checking Camera is Opened or Not 
while (cap.isOpened()):
    success , img = cap.read() # reading Frame 
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # converting BGR to RGB
    results = Hands.process(converted_image) # Processing Image for Tracking 

    if results.multi_hand_landmarks: # Getting Landmark(location) of Hands if Exists 
        for hand_in_frame in results.multi_hand_landmarks: # looping through hands exists in the Frame 
            mpDraw.draw_landmarks(img,hand_in_frame, mpHands.HAND_CONNECTIONS) # drawing Hand Connections   

    cv2.imshow("Hand Tracking - Code Terra", img) # showing Video 

    if cv2.waitKey(1) == 113: # 113 - Q : press on Q : Close Video 
        break
