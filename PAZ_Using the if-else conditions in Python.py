#==================================================================================================
#Filename : PAZ_Using the if-else conditions in Python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Assignment Number : 2
#Description : Using the if-else conditions in Python, that Calculates and outputs the linear displacement.
#Last modified: November 26, 2022
#==================================================================================================


g=0
while(g<1):

#values for  for different materials:

    Aluminum_value = 2.31 * pow(10, -5)
    Copper_value = 1.70 * pow(10, -5)
    Glass_value = 8.50 * pow(10, -6)
    Steel_value = 1.20 * pow(10, -5)
    Pyrex_value = 4.0 * pow(10, -6)
    Concrete_value = 14.5 * pow(10, -6)

#asks the user of what material

    user_material=input("Enter the name of the material: ").upper()

#for Aluminum material

    if(user_material =="ALUMINUM"):
        length_of_the_material= float(input("Enter the length of the ALUMINUM (in meters): "))
        change_in_temperature= float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement= Aluminum_value * length_of_the_material*change_in_temperature

#for Copper material

    elif (user_material == "COPPER"):
        length_of_the_material= float(input("Enter the length of the COPPER (in meters): "))
        change_in_temperature= float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement= Copper_value * length_of_the_material*change_in_temperature

#for Glass material

    elif (user_material == "GLASS"):
        length_of_the_material = float(input("Enter the length of the GLASS (in meters): "))
        change_in_temperature = float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement = Glass_value * length_of_the_material * change_in_temperature

#for Steel material

    elif (user_material == "STEEL"):
        length_of_the_material = float(input("Enter the length of the STEEL (in meters): "))
        change_in_temperature = float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement = Steel_value * length_of_the_material * change_in_temperature

#for Pyrex material

    elif (user_material == "PYREX"):
        length_of_the_material = float(input("Enter the length of the PYREX (in meters): "))
        change_in_temperature = float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement = Pyrex_value * length_of_the_material * change_in_temperature

#for Concrete material

    elif (user_material == "CONCRETE"):
        length_of_the_material = float(input("Enter the length of the CONCRETE (in meters): "))
        change_in_temperature = float(input("Enter the change in temperature (in degrees celsius): "))
        linear_displacement = Concrete_value * length_of_the_material * change_in_temperature

#to expand or contract

    if (linear_displacement > 0):
        print(user_material, " will expand by ", linear_displacement, " meters.")
    elif (linear_displacement < 0):
        print(user_material, " will contract by ", abs(linear_displacement), " meters.")

#if the name is not in the listed material above, the program will display the accepted names, and should ask the user for input again.

    else:
        print("Available materials only: ALUMINUM, COPPER, GLASS, STEEL, PYREX, CONCRETE")

    # Want to exit?
    To_exit = input("Press any key to continue. Type “BYE” to exit the program: ").upper()

    if (To_exit == 'BYE'):
        print("        ")
        g += 1
    else:
        print("        ")

