#Start of code
#x is first input
x = int(input())
#y is second input
y = int(input())
#z is third input
z = int(input())
#If input 1 is less than input 3 and if input 1 is less than input 2 then x is smallest 
if (x < z) and (x < y):
# x is smallest if statement above is true
    smallest = x 
#if not then i continues on
elif (y < x) and (y < x):
#If input 2 is less than input 3 and if input 2 is less than input 1 then y is smallest    
    smallest = y
#smalled is y is statement above is true if not then else is z = smallest    
else:
    smallest = z
#then print the smallest variable. It will pick the lowest number 
print(smallest)
#End of code
