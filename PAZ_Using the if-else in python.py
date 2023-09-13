#======================================================================================
#Filename : PAZ_Using the if-else in python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Exercise Number : 4
#Description : Using the if-else in python, To calculate and output how many servings your favorite food should be eaten per day to maintain the persons current weight at the specified activity level.
#Last modified: November 27, 2022
#======================================================================================


#Write a function that computes the calories required for the basal metabolic rate, taking as input a parameter for the persons weight, height, age and gender.

age = float(input("Enter your age: "))
gender = input("Enter [M] for male and [F] for female: ").upper()
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in cm): "))
print("................................................")

if (gender == 'M'):
    BMR = (10 * weight) + (6.25 * height) - (5.0 * age) + 5
    print( "BMR is", BMR, "cal per day")

elif (gender == 'F'):
    BMR = (10 * weight) + (6.25 * height) - (5.0 * age) - 161
    print("BMR is", BMR, "cal per day")

#Write another function that computes the calories required for physical activity, taking as input parameters for the intensity, weight, and minutes spent exercising.

print("................................................")
print("Choose a daily physical activity")
print("[1] Running 10 mph ")
print("[2] Running 6 mph ")
print("[3] Basketball")
print("[4] Walking 1 mph")
number_of_activity = int(input("Enter the number of the chosen activity: "))

#CRPA= 0.0385*Intensity*weight*minutes

if(number_of_activity == 1):
    minutes = int(input("Enter minutes spent on Running 10 mph: "))
    CRPA = 0.0385 * 17 * weight * minutes
elif(number_of_activity == 2):
    minutes = int(input("Enter minutes spent on Running 6 mph: "))
    CRPA = 0.0385 * 10 * weight * minutes
elif (number_of_activity == 3):
    minutes = int(input("Enter minutes spent on Basketball: "))
    CRPA = 0.0385 * 8 * weight * minutes
elif (number_of_activity == 4):
    minutes = int(input("Enter minutes spent on Walking 1 mph: "))
    CRPA = 0.0385 * 1 * weight * minutes

'''
Write a program, using these functions to calculate and output how many servings your favorite food should be eaten
per day to maintain the person's current weight at the specified activity level. The computation should include the 
        energy that is required to digest food.
'''
print("................................................")
print("Choose a food to be consumed")
print("[1] Doughnuts  ")
print("[2] Rice ")
print("[3] Spaghetti ")
print("[4] Chicken")
number_of_food = int(input("Enter the number of the chosen food: "))
print("................................................")

#servings = CRPA / TotalCaloriesConsumed

if(number_of_food == 1):
    kCal = 210
    CRDF = kCal * 0.1
    consume_calories = BMR + CRPA + (CRDF)
    servings = consume_calories / kCal
    print("To be just the weigh you are, you would have to consume ",'%.2f' % consume_calories, " calories or ",'%.4f' % servings,
          " servings of your favorite Doughnuts per day.")
elif(number_of_food == 2):
    kCal = 225
    CRDF = kCal * 0.1
    consume_calories = BMR + CRPA + (CRDF)
    servings = consume_calories / kCal
    print("To be just the weigh you are, you would have to consume ",'%.2f' % consume_calories, " calories or ",'%.4f' % servings,
          " servings of your favorite Rice per day.")
elif (number_of_food == 3):
    kCal = 190
    CRDF = kCal * 0.1
    consume_calories = BMR + CRPA + (CRDF)
    servings = consume_calories / kCal
    print("To be just the weigh you are, you would have to consume ",'%.2f' % consume_calories, " calories or ",'%.4f' % servings,
          " servings of your favorite Spaghetti per day.")
elif (number_of_food == 4):
    kCal = 75
    CRDF = kCal * 0.1
    consume_calories = BMR + CRPA + (CRDF)
    servings = consume_calories / kCal
    print("To be just the weigh you are, you would have to consume ",'%.2f' % consume_calories, " calories or ",'%.4f' % servings," servings of your favorite Chicken per day.")


