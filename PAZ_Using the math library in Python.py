#==========================================================================================================
#Filename : PAZ_Using the math library in Python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Assignment Number(Python) : 1
#Description : Using the math library in Python, to Calculate the release angles and speeds for shooting a basketball into the rim.
#Last modified: November 10, 2022
#==========================================================================================================

from math import*

distance= float(input("Enter the distance of the shooting hand of the robot from the center of the basketball rim (in meters): "))
initial_ball_speed= float(input("Enter the initial ball speed (in meters/second): "))
height= float(input("Enter the height of the ceiling (in meters): "))

#compute and display the optimal angle (in degrees) for releasing the ball, such that it shoots at the center of the rim

optimal_angle= (asin(9.8* distance/(initial_ball_speed*initial_ball_speed))/2)*180.0/3.14159265359
print("The optimal angle to launch the ball is", '%.3f' % optimal_angle, "degrees.")

#compute and display the smallest angle (in degrees) that will still make the ball go into the rim

smallest_angle=(asin(9.8*(distance-(0.45/2))/(initial_ball_speed*initial_ball_speed))/2)*180/3.14159265359
print("Smallest angle to make the shot is", '%.3f' % smallest_angle, "degrees.")

#compute and display the largest angle (in degrees) that will still make the ball go into the rim

largest_angle=(asin(9.8*(distance+(0.45/2))/(initial_ball_speed*initial_ball_speed))/2)*180/3.14159265359
print("Largest angle to make the shot is", '%.3f' % largest_angle, "degrees.")

#compute and display the maximum height (in meters)

optimal_angle_deg=optimal_angle*3.14159265359/180.0
maximum_height=(pow(initial_ball_speed,2.0)*pow(sin(optimal_angle_deg),2.0))/(2*9.8)
print("The basketball will reach a maximum height of", '%.3f' % maximum_height, "meters")

#determine whether or not the basketball will hit the ceiling when thrown at the optimal angle

if(maximum_height<height):
    print("The basketball will not hit the ceiling. ")
else :
    print("The basketball will hit the ceiling. ")