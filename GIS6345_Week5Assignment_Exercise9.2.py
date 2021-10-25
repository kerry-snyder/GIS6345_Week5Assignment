#Exercise 9.2

#Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it

def has_no_e(word):
    string_object = word
    goal = 'e'
    if (string_object.__contains__(goal)):
        print('False') 
    else: 
        print ('True')

has_no_e('spice')

has_no_e('banana')

#Write a program that reads words.txt and prints only the words that have no "e".
fin = open('words.txt')
for line in fin:
    string_object = line
    goal = 'e'
    if (string_object.__contains__(goal)):
        None 
    else:
        print(string_object)
        
#Compute the percentage of words in the list that have no "e".

#Computation of total lines in the entire text file
with open('words.txt') as fp:
    for count, line in enumerate(fp):
        pass
    total = count
    print('Total Lines', total)

#Count up for each line that does not contain "e".
#This for loop is similar to the first, but instead of printing the results, it counts up each time a word does not contain "e".
fin = open('words.txt')
count = 0
for line in fin:
    string_object = line
    goal = 'e'
    if (string_object.__contains__(goal)):
        None 
    else:
        count = count + 1
        
print(count, 'words do not contain the letter "e"')

#Calulcate percentage using total lines (words) and words that satisfy the condition.
percentage = ((count)/total)*100
print(percentage, '% of the words in the file do not contain the letter "e"')
