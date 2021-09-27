import cv2
import pyrealsense2
from realsense_depth import *
# Initialize Camera Intel Realsense
dc = DepthCamera()
ret, depth_frame, color_frame = dc.get_frame()

 # Show distance for a specific point
point = (400,300)
cv2.circle(color_frame, point, 4, (0, 0, 255))
distance = depth_frame[point[1], point[0]]

cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)