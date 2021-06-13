#Start of Code
vocabs = input() #These are the replacement words- Make sure to read question. At first thought it was one input
phrase = input() #This is the whole setence
vocabulary = vocabs.split() #Making sure things come out corretly and not in one line down
dict = {} #adding a dictonary - Guessing it can be any name
for i in range(0, len(vocabulary), 2): #for vocabulary length in skipping
    dict[vocabulary[i]] = vocabulary[i + 1]  #adding values to dict if you have more the 1 its out of range for this since theres 1
replace = '' #Defind the replace. Remember cant defind this as 0 due to there needing to be ''
for word_list in phrase.split(): #Replacing everything for loop
    if word_list in dict: #If statement loop with word_list and the dict
        replace += dict[word_list] + ' ' #adding the replace and dict word list
    else: #else statment 
        replace += word_list + ' ' #add wordlist and replace
print(replace.strip()) #remove spaces if not it has spaces
#End of code
