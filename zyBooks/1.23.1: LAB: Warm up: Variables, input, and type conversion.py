#Start of code
# FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
user_int = int(input('Enter integer (32 - 126):\n')) #input for user_int
user_float = float(input('Enter float:\n')) #input for user_float
user_character = str(input('Enter character:\n')) # input for user_character
user_string = str(input('Enter string:\n'))#input for user_string
print(user_int, user_float, user_character, user_string) #print the output 
# FIXME (2): Output the four values in reverse
print(user_string, user_character, user_float, user_int)#prints the output backwards
# FIXME (3): Convert the integer to a characer, and output that character
print(user_int,'converted to a character is', chr(user_int))#prints out the char
#End of code
