#Start of Code
import csv #importing in the cvs
name_file = input() #input for the file
word_freq = {} #frequency of the file
with open(name_file, 'r') as csvfile: #opening file of name in 'r' in cvsfile
  csvreader = csv.reader(csvfile)#naming for the cvsreaders
  for area in csvreader: #for area where it will read
     for words in area: #for the words that are in the area 
        if words not in word_freq.keys(): #if its not the freq it = 1
           word_freq[words] = 1 # veraible then words
        else: #else statemenet
           word_freq[words] += 1 #adding 1
for key in word_freq.keys(): #Had trouble with naming the
  print(key + " " + str(word_freq[key]))#print results for each read of cvs
  #End of Code
