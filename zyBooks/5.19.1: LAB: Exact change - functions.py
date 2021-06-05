#Start of code
def exact_change(user_total): #define fuction goes here
    num_dollars = user_total // 100 #variable = user_total // varibale count dollars
    user_total %= 100 #Remainder
    num_quarters = user_total // 25 #variable = user_total // varibale count quarters
    user_total %= 25 #Remainder
    num_dimes = user_total // 10 #variable = user_total // varibale count dimes
    user_total %= 10 #Remainder
    num_nickels = user_total // 5 #variable = user_total // varibale count for nickles
    user_total %= 5 #Remainder
    num_pennies = user_total #variable = user_total // varibale count for pennies
    return(num_dollars, num_quarters, num_dimes, num_nickels, num_pennies) #return the def
if __name__ == '__main__': #if statement from main
    input_val = int(input()) #user input
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val) #saying everything = exact_change(input_val)

    if input_val <= 0: #You have to have this at the top if not the exactchange won't work correctly it will miss the three section in the grading if this is at the bottom
        print('no change') #printing no change
    else: #else for plural and single
        if num_dollars == 1:
            print(num_dollars, "dollar") #Prints for Dollar single
            
        elif num_dollars > 1:
            print(num_dollars, "dollars") #Prints for Dollars Plural
            
        if num_quarters == 1:
            print(num_quarters, "quarter") #Prints for Quarter single
            
        elif num_quarters > 1:
            print(num_quarters, "quarters") #Prints for Quarters plural
            
        if num_dimes == 1:
            print(num_dimes, "dime") #Prints for Dimes single
            
        elif num_dimes > 1:
            print(num_dimes, "dimes") #Prints for Dimes plural
            
        if num_nickels == 1:
            print(num_nickels, "nickel") #Prints for Nickel single
            
        elif num_nickels > 1:
            print(num_nickels, "nickels") #Prints for Nickels plural
            
        if num_pennies == 1:
            print(num_pennies, "penny") #Prints for Penny single
            
        elif num_pennies > 1:
            print(num_pennies, "pennies") #Prints for Pennies Plural
#end of code - used the last exact change lab to help out with this one
