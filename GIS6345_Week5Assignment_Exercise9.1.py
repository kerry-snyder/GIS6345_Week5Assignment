#Exercise 9.1
#Write a program that reads words.txt and prints only the words with more than 20 characters
#Each line has one white space, so the code must search for lines of 21 or more characters.

fin = open('words.txt')
for line in fin:
    if len(line) > 21:
        print (line)
    else:
        None
