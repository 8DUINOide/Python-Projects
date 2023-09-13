#======================================================================================
#Filename : PAZ_Using for loops in python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Exercise Number(Python) : 3
#Description : Using for loops in python, to print all of the prime numbers between 1 and 1000
#Last modified: November 11, 2022
#======================================================================================

for j in range(2, 1000):
    is_prime = True
    i = 2
    while i<=j/2:
        if (j % i == 0):
            is_prime = False
        i+=1
    if (is_prime):
        print(j,end=",")



