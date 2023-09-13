#======================================================================================
#Filename : PAZ_Using while loop in python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Exercise Number(Python) : 2
#Description : Using while loop in python, to find the temperature of the air affects the speed of the molecules, which in turn affects the speed of sound.
#Last modified: November 10, 2022
#======================================================================================


print("Welcome to Doppler Shift Happens! ")
degrees_input_begin= int(input("Please enter the starting temperature (degrees): "))
degrees_input_end= int(input("Please enter the ending temperature (degrees): "))

while (degrees_input_begin <=degrees_input_end):
    velocity = 331.3 + 0.61 * degrees_input_begin
    print("At",degrees_input_begin, "degrees celcius the velocity of sound is", '%.2f' % velocity, "m/s" )
    degrees_input_begin +=1