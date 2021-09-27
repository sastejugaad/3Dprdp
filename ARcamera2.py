"""
Aruco marker program. This program implements aruco marker
Replace the import camera to import ARcamera 
everything should work fine if libray is installed properly

"""

import cv2
import numpy as np
#import cv2.aruco as aruco

font = cv2.FONT_HERSHEY_DUPLEX

c = 0
score = 0

markerID = 1
#cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
#faceCascade = cv2.CascadeClassifier(cascPath)python

#scaling_factorx=0.3
#scaling_factory=0.3

def gstreamer_pipeline(
    capture_width=600,
    capture_height=300,
    display_width=600,
    display_height=300,
    framerate=20,
    flip_method=0,
):
    
  
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

print(gstreamer_pipeline(flip_method=0))
video_capture = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)


#video_capture = cv2.VideoCapture(1)  # 0 for web camera live stream

#if not video_capture:
 #   print("Failed")
#else:
 #  ret, frame= video_capture.read()

def camera_stream():
    global c
    global font
    global markerID

    global score
     # Capture frame-by-frame
    ret, frame = video_capture.read()
    #frame = imutils.resize(frame, width=400)

    #frame=cv2.resize(frame,None,fx=scaling_factorx,fy=scaling_factory,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    #height, width, channels = frame.shape
    #print(height)
"""
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
    arucoParameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=arucoParameters)
    frame = aruco.drawDetectedMarkers(frame, corners)
"""
    #cv2.rectangle(frame, (0,0), (width,int(height/10)), (32,32,32), -1)
"""
    markerID = ids
   
    if c == 0:
        c = 1
        if ids == markerID:
            score = score + 10
            #print("maje aa gaye frands")
"""  
    #cv2.putText(image, ‘Text to Display’, bottom left starting point, Font, Font Size, Color, Thickness)
   # cv2.putText(frame, "Score = "+str(score), (20, 20),font, 0.5, (255, 255, 255), 0)
    return cv2.imencode('.jpg', frame)[1].tobytes()



    

