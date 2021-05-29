#Start of Code
the_list = []
while True: #while statement - true
    letter = input() #the input is take on the name of variable letter
    in_lists = letter.split() #in the list variable input letter.split
    sentence = in_lists[0] #setnece with the varibale in_lists 0
    integer = in_lists[1] #the varibale number within the in_list 1
    if sentence == 'quit': #if user input quit it breaks
        break # break the while loop
    else: #this is part of the if else statement
        the_list.append(f"Eating {integer} {sentence} a day keeps the doctor away.") #printing out the sentence with list
for output in the_list: #for variable in container
    print(output) #prints out the sentence
#End of Code
