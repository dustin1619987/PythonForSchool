#Start of code
triangle_char = input('Enter a character:\n') #Input for triangle char
triangle_height = int(input('Enter triangle height:\n')) #input from user for taignle height
print('')#prints the space
for c in range(0,triangle_height): #fpr variabe in container range - use range start at 0, traingle height
   for h in range(0, c+1): #for the h in range start 0 the add c + a keeps triangle from extended out 
       print(triangle_char,end=" ") #print triangle output 
   print() #print out everything - if you forget this then the triangle doesn't stay in place
#End of code
# uses the user-specified triangle_char character DONE
#use a loop to output a right triangle of height triangle_height & make it looks like a triangle DONE
