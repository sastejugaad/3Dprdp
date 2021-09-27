"""
simple csi camera implementation
"""
import cv2
import numpy as np

#cascPath = 'haarcascade_frontalface_dataset.xml'  # dataset
#faceCascade = cv2.CascadeClassifier(cascPath)
scaling_factorx=0.3
scaling_factory=0.3
#video_capture = cv2.VideoCapture(1)  # 0 for web camera live stream
#  for cctv camera'rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp'
#  example of cctv or rtsp: 'rtsp://mamun:123456@101.134.16.117:554/user=mamun_password=123456_channel=1_stream=0.sdp'


def gstreamer_pipeline(
    capture_width=3264,
    capture_height=2464,
    display_width=640,
    display_height=320,
    framerate=20,
    flip_method=2,
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

def camera_stream():
     # Capture frame-by-frame
    ret, frame = video_capture.read()

    #frame=cv2.resize(frame,None,fx=scaling_factorx,fy=scaling_factory,interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #image = np.zeros((512,512,3),np.uint8)

    height, width, channels = frame.shape

    #print(height)

    #cv2.rectangle(frame, (0,0), (width,30), (96,96,96), -1)

    # Display the resulting frame in browser
    return cv2.imencode('.jpg', frame)[1].tobytes()
