#Exercise 10.2
#Write a function called cumsum that takes a list of numbers and returns the cumulative sum

#This function starts with a baseline total of 0.
#Each number in the list to the total sequentially.
#This creates a new value for total each time.
#'total += x' is equlivalent to 'total = total + x'
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

t = [1,2,3]
print(cumsum(t))
