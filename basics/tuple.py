#Tuples are imutable sequece of objects
print("hello")

t= ("France",4.4564,3)
print(t)

def minmax(items):
    return min(items),max(items)

print(minmax([83,33,84,32,85,31,86]))

#Tuple unpacking -  Destructuring operation that unpacks data stuructures into named refereneces 
# can assign nested values to nested tuples
(a,(b,(c,d))) = (4,(3,(2,1)))
print(a,b,c,d)

#can test if a value is in a tuple
print(5 in (3,2,5,275,7))

print(6 not in (3,2,5,275,7))
