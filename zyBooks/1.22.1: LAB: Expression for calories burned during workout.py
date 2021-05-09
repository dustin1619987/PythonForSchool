 #Start of my Code
'''MathCode-> Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
'''MathCode-> Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''
#Input Variables below
Age = int(input()) 
Weight = int(input()) 
Heart_Rate = int(input()) 
Time = int(input())
#MathCode in python for man & women
calories_women = ((Age * 0.074) - (Weight * 0.05741) + (Heart_Rate * 0.4472) - 20.4022) * Time / 4.184
calories_man = ((Age * 0.2017) + (Weight * 0.09036) + (Heart_Rate * 0.6309) - 55.0969) * Time / 4.184
#prints the women and men calories
print('Women: {:.2f} calories'.format(calories_women))
print('Men: {:.2f} calories'.format(calories_man))
#End of my Code
