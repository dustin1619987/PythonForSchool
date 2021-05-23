#Start of Code
#defining variable
def Exact_change(x):
#Start of if statement
    if x > 0:
        dollars = x // 100 #x // 100 
        x %= 100 #Remainder
        quarters = x // 25 # x // 25
        x %= 25 #Remainder
        dimes = x // 10 #x // 10
        x %= 10 #Remainder
        nickels = x // 5 #x // 5
        x %= 5 #Remainder
        penny = x 
#Start of if Statement then goes into else if statements 
        if dollars == 1:
            print(dollars, "Dollar") #Prints for Dollar single
        elif dollars > 1:
            print(dollars, "Dollars") #Prints for Dollars Plural
        if quarters == 1:
            print(quarters, "Quarter") #Prints for Quarter single
        elif quarters > 1:
            print(quarters, "Quarters") #Prints for Quarters plural
        if dimes == 1:
            print(dimes, "Dime") #Prints for Dimes single
        elif dimes > 1:
            print(dimes, "Dimes") #Prints for Dimes plural
        if nickels == 1:
            print(nickels, "Nickel") #Prints for Nickel single
        elif nickels > 1:
            print(nickels, "Nickels") #Prints for Nickels plural
        if penny == 1:
            print(penny, "Penny") #Prints for Penny single
        elif penny > 1:
            print(penny, "Pennies") #Prints for Pennies Plural
#if above is not right then is will output else >
    else:
        print("No change")
#inputs      
if __name__ == '__main__':
    user_input = int(input()) #user_input
    Exact_change(user_input) #exact_change
#End of Code
