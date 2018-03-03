import numpy as np

# Problem 11

#1)
print('Problem 1) Create a = 0-92 and b = all ones')
a = np.arange(93)
b = np.ones(a.size)

print(a)

print(b)


#2)
print('Problem 2) Create 3x3 Array of \'True\'s')
c = np.full((3,3), True)

print(c)

#3)
print('Problem 3) Replpace odds in a with -1')
d = a
d[1::2] = -1
a[1::2] = -1

print(d)
