# 3Dprdp
Nvidia jetson nano development platform

This is a 3D-printed robotics development platform. Originally inspired by DJI robomaster s1 I wanted to design something more affordable and accessible system of my own. 

Powered by Nvidia jetson nano board runs on ubuntu. AI and machine learning models can be implemented easily on this. With few changes in code, it can also support Nvidia jetracer and many other projects. I designed this to test out prototypes and ideas quickly. Instead of setting from scratch for every project, this will help in testing critical stuff early on the project.

The main program is written in python and uses flask and socket io to run a webserver on board. You can connect to the interface using the IP address.

Demo video
https://www.youtube.com/watch?v=7Dail3PpAlU

Tutorial article
https://www.instructables.com/3D-Printed-Robotics-Development-Platform-With-Nvid/

Cad Files:-
https://grabcad.com/library/nvidia-jetson-nano-robot-development-platform-for-3d-printing-1

Instagram:
https://www.instagram.com/saste.jugaad/

Discord:
https://discord.gg/fMXvGty

## How to run this 

- Install python3 and flask.
- Connect bot and your mobile device to same wifi network.
- Get the ip adress of the bot.
- Run the main.py (sudo python3 main.py)
- open your webbrowser on your mobile and go to <ipadressofbot>:5000
- You should get the live feed.

## Joystick and control libaray

Here is the original joystick library i used to create the controls its great and has a very good guide on how to use it.

- https://github.com/bobboteck/JoyStick

## Problems

- Many

- If you bump up the resolution of the video you will get lag. Also dont use your mobile hotspot, try a router or create a hotspot on jetson itself. 
Turn off firewall, VPN, ad blockers on your mobile device otherwise you might get lag.
