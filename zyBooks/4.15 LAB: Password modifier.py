#Start of code
word = input() #word is the input
password = '' #variable = ''

for letter in word: #for variable in container - variable is letter but container is word
    if( letter == 'i'): #if else statment works here 
        password += '!' #if a letter = a certain letter then you add password += then replace letter elif others letters
        
    elif( letter == 'a'): #elif for a to @
        password += '@' #New replacement
            
    elif( letter == 'm'): #elif for m to M
        password += 'M' #New replacement
            
    elif( letter == 'B'): #elif B for 8
        password += '8' #New replacement
            
    elif( letter == 'o'): #elif o for .
        password += '.' #New replacement
    else: #else will be adding password a+ letter
        password += letter
password += 'q*s' #these are the letter with no replacements but is added at the end of Myp@ssw.rdq*s
print(password) #print out the password
#End of code
