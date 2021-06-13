#Start of Code
nums = input() #inputs from user
nums_list = nums.split() #definding the num_lists
nums_list = [int(x) for x in nums_list] #keeps adding the numbers to the list ofr num_list
total_nums = 0 #Definding what the variable is
max_num = 0 #Definding what the variable is
for num in nums_list: #for loop for num in nums_list
    total_nums = total_nums + num # adding totale with num
    if num > max_num: # if a number is > max 
        max_num = num #making variable = the num
average = total_nums / len(nums_list) # averging things out for length of the number lists
print(str(f'{float(average):g}'), max_num) #To remove the extra 0 and print average and max numbers
#End of Code
#Spent a while trying to get/find something to work for getting that stubbern 0 away.
