#Start of Code
# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
favorite_color = input("Enter favorite color:\n") #Input from the user favorite color
pet_name = input("Enter pet's name:\n")#Input from the user pet name
enter_number =input("Enter a number:\n")#Input from the user number

print('You entered:', favorite_color, pet_name, enter_number) #output/prints the variables from above
# FIXME (2): Output two password options
password1 = favorite_color + '_' + pet_name #password1 then adds the color and pet name
print()#Adds correct spacing
print('First password:', password1) #printing first pasword

password2 = enter_number + favorite_color + enter_number #adds everything
print('Second password:',password2) #second password
# FIXME (3): Output the length of the two password options
print()#Adds correct spacing
print('Number of characters in {}: {}'.format(password1, len(password1)))#length of characters for password1
print('Number of characters in {}: {}'.format(password2, len(password2)))#length of characters for password2
#End of code
