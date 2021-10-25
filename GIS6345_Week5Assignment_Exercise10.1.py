#Exercise 10.1
#Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists.

#This function takes a list of number lists 't'
#This function starts with a baseline total of 0.
#The sum of each list is added one by one to total, creating a new value for total.
#It returns the sum of all numbers within those lists.
#'total += sum(nested)' is equlivalent to 'total = total + sum(nested)'
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total

t = [[1,2], [3], [4,5,6]]
print(nested_sum(t))
