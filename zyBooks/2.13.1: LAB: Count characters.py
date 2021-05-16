#Start of code
words = input() #user input for variable word
char = words[0] #char will = search
str = words[2:]
number_time = 0 #setting number_time to 0
#if statement
for x in str:
    if(x==char):#if x  == characters then += 1
        number_time += 1 #number of time is 0 but add 1 for statement
print(number_time) #print new number_time
#End of code
