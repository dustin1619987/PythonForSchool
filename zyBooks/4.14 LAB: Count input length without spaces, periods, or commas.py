#Start of Code
user_text = input() #input of users
letters = 0 #labeling value of letters(variable)
for characters in user_text: # for statement
    if characters != '.' and characters != ' ' and characters != ',': #If the characters = .,sapce count everything else
        letters += 1 #increments of 1
print(letters) #oddly it shows the output without print humm
#End of Code
