from __future__ import print_function

import time
from sr.robot import *


R = Robot()          				
	#instance of the class Robot

def drive(speed, seconds):			
    	#Function for setting a linear velocity 
 	# Args: speed (int): the speed of the wheels
	# seconds (int): the time interval
   
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
  	 # Function for setting an angular velocity    
 	 # Args: speed (int): the speed of the wheels
	 # seconds (int): the time interval
 
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_silver_token():
   	#Function to find the closest silver toke,
    	#Returns:
	#dist (float): distance of the closest silver token (-1 if no silver token is detected)
	#rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
   
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

def find_golden_token():
    	#Function to find the closest golden token
    	#Returns:
	#dist (float): distance of the closest golden token (-1 if no golden token is detected)
	#rot_y (float): angle between the robot and the golden token (-1 if no golden token is detected)
   
    dist=100
    for token in R.see():
        if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD:
            dist=token.dist
	    rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y
dist_g, rot_y_g = find_golden_token()
print("initial %f   %f",dist_g ,rot_y_g)   		#Check the distance and angle between robot and golden marker at the initial position 
drive(40,4)          
	 #at the begining if we check the distance between robot and golden marker we find it very small even if it is far
	 #so at the begining we drive the robot for 4seconds untill the find golden function starts work accuratly"

while 1:       
    dist_g, rot_y_g = find_golden_token()
    dist_s, rot_y_s = find_silver_token()
    if dist_g>0.8:     				#if the golden marker is far 
        print("Far Golden")
        if dist_s<0.8 and -85<rot_y_s<85: 	#if there is a close Silver and it is not behind the robot
            print("Ther is Silver")
            if dist_s<0.4:
                if R.grab(): 			# if we grab the token, we move the robot forward and on the right, we release the token, and we go back to the initial position
                    print("Gotcha!")
	            turn(30,2)
	            drive(20,1)
	            R.release()
	            drive(-20,1)
	            turn(-33,2)
	    elif -2<= rot_y_s <=2: 		# if the robot is well aligned with the token, we go forward
	            print("it is alligned")
                    drive(30, 0.5)
            elif rot_y_s < -2: 			# if the robot is not well aligned with the token, we move it on the left or on the right
                    print("silver Left a bit...")
                    turn(-2, 0.5)
            elif rot_y_s > 2:
                    print(" silver Right a bit...")
                    turn(+2, 0.5)                    
        else:
             drive(40,0.2)  			#if there is a close Silver marker but it is not close enough to be grabed, drive the robot
    elif dist_g<0.8:				#if the golden is close,we turn clockwise or counter clockwise by diffrent angles dependig 
        print("CLOSE golden")			#on the exact location of the marker with respect to the robot
        print("%f       %f",rot_y_g,dist_g)
        if -80<rot_y_g<0:      			#if the angle is negative,the golden marker is on the left,the robot turn clockwise
             print("turn a lot clock wise")		#if angle is close to '0', turn sharply
             turn(7, 2)			#if angle is close to '-180' turn smoothly 
             drive(10,1)
        elif -110<rot_y_g<-80:
             print("turn clock wise")
             turn(3, 1)
             drive(10,1)
        elif -180<rot_y_g<-110:
             print("turn a bit clock wise")
             turn(1, 1)
             drive(20,2.5)
        elif 0<rot_y_g<80:			#if the angle is positive,the golden marker is on the right,the robot turn coubter clockwise			
             print("turn a lot conter clock wise")	#if angle is close to '0', turn sharply
             turn(-10, 2)			#if angle is close to '180' turn smoothly 
             drive(10,1)
             drive(10,1)
        elif 80<rot_y_g<110:
             print("turn conter clock wise")
             turn(-3, 1)
             drive(10,1)
        elif 110<rot_y_g<180:
             print("turn a bit conter clock wise")
             turn(-1, 1)
             drive(20,2.5)
   
        
             
           
        
        
       
        
             
           
        
        
