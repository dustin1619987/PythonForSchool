#Start of Code
def read_File(files_input): #defining the reading file and file input
    dictionary = {} #dictornnary = the input of the file
    with open(files_input, 'r') as infile: #when the file opens it is put into Read (r)
        line = infile.readlines() #reading each line of the file
        for index in range(0, len(line) - 1, 2): #when the index in the range of 0 to the length 
            if line[index].strip() == '': #if the line is index continue
                continue #continues the reading
            counts = int(line[index].strip()) #counts the int of the index
            named_file = line[index + 1].strip()  #the named files will = for each line + 1
            if counts in dictionary.keys(): #if statement for the count in dictinary
                dictionary[counts].append(named_file) #counts for dictinary
            else: #else statement 
                dictionary[counts] = [named_file] # else will be dictonary = files
        return dictionary #return back to dictonary
def keys(dict, file_nam): #defining the key, with fict nd file_name
    with open(file_nam, 'w+') as outfile: #with it opening file_name w(write)
        for key in sorted(dict.keys()): #for key in sorted 
            outfile.write('{}: {}\n'.format(key, '; '.join(dict.get(key))))
            print('{}: {}'.format(key, '; '.join(dict.get(key))))
def title_files(dict, file_nam): #defined titles_files in dict, file_name
    titles_forfile = [] #titles []
    for title_files in dict.values():
        titles_forfile.extend(title_files)
    with open(file_nam, 'w+') as outerfile: #when open file name w+
        for title_files in sorted(titles_forfile): #for titles in sorted
            outerfile.write('{}\n'.format(title_files))
            print(title_files) #prints out the titles files
def main(): #defining the main
    file_name = input() #the input of file
    reading = read_File(file_name)
    if reading is None: #if it not reading 
        print('Invalid {}'.format(file_name)) #print out invlid to help inform that there is a issue
        return #return back
    file0 = 'output_keys.txt' #file 0 name
    file = 'output_titles.txt' #file 2 name 
    keys(reading, file0) #reading
    print() #print space
    title_files(reading, file)
main()
#End of Code
