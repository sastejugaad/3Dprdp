import numpy as np
import cv2
import cv2.aruco as aruco




calib_path  = ""
#camera_matrix   = np.loadtxt(calib_path+'cameraMatrix_webcam.txt', delimiter=',')
#camera_distortion   = np.loadtxt(calib_path+'cameraDistortion_webcam.txt', delimiter=',')
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
arucoParameters = aruco.DetectorParameters_create()



cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#chage to adaptive one later
    
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        gray, aruco_dict, parameters=arucoParameters)
    #print(corners)
    print(ids)

    if np.all(ids == 63):# != None
        display = aruco.drawDetectedMarkers(frame, corners)
        x1 = (corners[0][0][0][0], corners[0][0][0][1])
        x2 = (corners[0][0][1][0], corners[0][0][1][1])
        x3 = (corners[0][0][2][0], corners[0][0][2][1])
        x4 = (corners[0][0][3][0], corners[0][0][3][1])

        im_dst = frame
        im_src = cv2.imread('red.jpg')
        size = im_src.shape
        pts_dst = np.array([x1, x2, x3, x4])
        pts_src = np.array(
            [
                [0, 0],
                [size[1] - 1, 0],
                [size[1] - 1, size[0] - 1],
                [0, size[0] - 1]
            ], dtype=float
        )

        h, status = cv2.findHomography(pts_src, pts_dst)
        temp = cv2.warpPerspective(
            im_src, h, (im_dst.shape[1], im_dst.shape[0]))
        cv2.fillConvexPoly(im_dst, pts_dst.astype(int), 0, 16)
        im_dst = im_dst + temp
        cv2.imshow('Display', im_dst)
    else:
        display = frame
        cv2.imshow('Display', display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()