# start of my code
Name = input() #input the name all on one line
#split the name into list and store them into list variable
# list[0] --first name
# list[1] --middle name
# list[2] --last name
list = Name.split(' ') 
# check if length is 2 - start of if else statement
if len(list)==2: #the len counts the amount in list ==2
  print(list[1]+",",list[0][0]+".")# print out the names if ==2 :middle name. forstnae then the [0]  counts lettering
else:
  print(list[2]+",",list[0][0]+"."+list[1][0]+".")# else statmenet that prints the other: last name - firstname - middle.
#end of my code
