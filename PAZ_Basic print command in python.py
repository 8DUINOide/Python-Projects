# =================================================
# Filename :  PAZ_Basic print command in python.py
# Author : Al Francis B. Paz
# Email : afpaz@gbox.adnu.edu.ph
# Exercise Number(Python) : 1 
# Description: Basic print command in python, to display the Cigarettes Sold, Profit, and Nicotine Consumed 
# Last modified: November 10, 2022
# =================================================


cigarettes_sold_per_day = int(input('On average, how many cigarettes does your store sell daily? '))
cigarette_packs_sold_per_year = int(cigarettes_sold_per_day*365/20)
print('Number of packs sold per year: ', cigarette_packs_sold_per_year )
profit_per_day = float(cigarettes_sold_per_day*13.50/20)
print('Profit per day (Php): ', profit_per_day)
profit_per_year = profit_per_day*365
print('Profit per year (Php): ', '%.1f' % profit_per_year )
print('Nicotine consumed by customers in a year: ', cigarettes_sold_per_day*365*12, "mg")
