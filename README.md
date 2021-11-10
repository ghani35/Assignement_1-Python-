# Assignement_1-Python-

Remark: the arguments of turn() and drive() functions have been chosen by simulating the code and observing the results



Define the needed functions  
turn()
drive()
find_silver_token()
find_golden_token()

give a starting linear velocity befor entring the whil loop 

while(true)
      if(the golden token is far)
            if(the silver token is detected and not behind the robot)
                  if (silver is close enough)
                        grabe it  
                  else
                        alligne the robot with respect to silver token
            else (silver is not detected and the golden is far )
                  drive the robot  
      else (the golden is close)
            if(then angle between robot and golden marker is negative and between (-80,0) )
                  turn clock_wise with larg angle 
            else if(then angle between robot and golden marker is negative and between (-110,-80))
                  turn clock_wise with meduim angle
            else if(then angle between robot and golden marker is negative and between (-180,-110))
                  turn clock_wise with small angle
            if(then angle between robot and golden marker is positive and between (0,80) )
                  turn counter_clock_wise with larg angle 
            else if(then angle between robot and golden marker is positive and between (80,110))
                  turn counter_clock_wise with meduim angle
            else if(then angle between robot and golden marker is positive and between (110,180))
                  turn counter_clock_wise with small angle

