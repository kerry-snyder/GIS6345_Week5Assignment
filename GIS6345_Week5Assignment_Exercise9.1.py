#Exercise 9.1

fin = open('words.txt')
for line in fin:
    if len(line) > 21:
        print (line)
    else:
        None
