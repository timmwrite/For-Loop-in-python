# finding the sum of mutiples of 3 between 1 and 500 including 500
# @timmwrite
# using for loop

x = list(range(1, 501))

#print(x) if you print x, you will get all the mutiples of 3 btwn 1 and 500 ncluding 500

total = 0

for elements in x:
    if elements % 3 == 0:
        #total += elements you can either us this or 
        """The expression a += b is shorthand for a = a + b , where a and b can be numbers, or strings, or tuples, or lists (but both must be of the same type)."""
        
        total = elements + total

print(total)