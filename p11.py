import numpy as np

# Problem 11

#1)
print('Problem 1) Create a = 0-92 and b = all ones')
a = np.arange(93)
b = np.ones(a.size)

print(a)
print(a.T)
print(b.T)

#2)
print('Problem 2) Create 3x3 Array of \'True\'s')
c = np.full((3,3), True)

print(c)

#3)
print('Problem 3) Replpace odds in \'a\' with -1')
a[1::2] = -1

print(a)

#4)
print('Problem 4) Reshape \'a\' to a 2d array with 3 rows')
a = np.reshape(a,(3,-1))

print(a)
print(a.T)

##5)
#print('Problem 5) Stack \'a\' and \'b\' vertically')
#print(np.stack((a,b), axis=-1))
#
##6)
#print('Problem 6) Transpose a & b, then stack them horizontally')
#print(np.hstack((a.T,b.T)))

#7)
print('Problem 7) Create c=np.array([1,2,3]) using only nunmpy functions')
c = np.arange(1,4)

print(c)
print(type(c))


