
#!/usr/bin/python
"""
We are using a small REST server to control our robot.
"""

from flask import Flask, render_template, Response, request, jsonify
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import math
from multiprocessing import Process, Queue
from camera import camera_stream
import webbrowser
import time
from time import sleep
from engineio.payload import Payload
#from adafruit_servokit import ServoKit

from arduino_control import *
from turret import *

#remove http logging msg from output
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
#--------
Payload.max_decode_packets = 200 #to remove too many vaule unpack error

# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
#kit = ServoKit(channels=16)
#pca.frequency = 50

# TODO: axis-mapping should be OOP and automatic!

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
CORS(app)
socketio = SocketIO(app, async_mode='threading') #threading,gevent


@app.route('/')
def index():
    return render_template('joy.html')
    #print("page")



def gen_frame():
    """Video streaming generator function."""
    while True:
        
        frame = camera_stream()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n') # concate frame one by one and show result



@app.route('/video_feed')
def video_feed():
    #print("feed")
   
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frame(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@socketio.on('control', namespace='/control')
def control(message):
   # print("control")
    #plz()
    
    data = message["data"]
    #print(data)

    if "joystick" in data.keys():
        x = data["joystick"][0]
        
        if x == 'N':
            fwd()

        elif x == 'S':
            back()

        elif x == 'E':
            right()

        elif x == 'W':
            left()

        elif x == 'C':
           Stop()
        
        elif x == 'NW' or x == 'NE' or x == 'SW' or x == 'SE':#to stop NE,SE movements and so on
           Stop()


        
        #y = data["joystick"][1]
        #print ("Left: ",x,",",y)
        #print("mocvew")
       #if _debug: print ("[Server] Left: ",x,",",y)
        #linear.q.put(("left",x,y))
    elif "joystick2" in data.keys():
        x = data["joystick2"][0]
        y = data["joystick2"][1]

        Xturret(x)
        Yturret(y)

        #kit.servo[0].angle = x
        #time.sleep(1)
        #kit.servo[3].angle = y
      #  sleep(0.1)
       # print (" Right: ",x,",",y)
       # if _debug: print ("[Server] Right: ",x,",",y)
       # servo.q.put(("right",x,y))
       # servo2.q.put(("right",y,x))
   # elif "A" in data.keys():
      #  a=1
      #  print (" A")
        #if _debug: print ("[Server] A")
       # binary.q.put(("A",1,0))
  #  elif "B" in data.keys():
   #     b=1
   #     print (" b")
        #if _debug: print ("[Server] B")
       # binary2.q.put(("B",1,0))

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", use_reloader=False)
  #  socketio.run(app, host="0.0.0.0")
