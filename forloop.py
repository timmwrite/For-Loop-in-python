# For loops in python
# @timmwrite 
# we will be iterating through a list and doin some expressions!
# Enjoy 

# How to find the sum of numbers 1 trough 100 i.e 1, 2 , 3 ..........100

e = list(range(1, 101))

total = 0

for x in e:
    total = total + x

print(total)