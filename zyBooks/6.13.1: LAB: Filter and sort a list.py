#Start of Code
nums = input() #inputs from user
nums_list = nums.split() #definding the num_lists
nums_list = [int(x) for x in nums_list] #keeps adding the numbers to the list of num_list
sorted_numbers = sorted(nums_list) #Sorts the numbers lesst the greatest
no_negatives = [i for i in sorted_numbers if (i < 0) == 0] # the take a variable and output no negatives
res = str(no_negatives)[1:-1] #take off brackets
res = res.replace(',', '') #takes of ,
print(res, end= " ") #prints out the numbes list and adds end spaces
#End of Code
