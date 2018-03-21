import numpy as np

# Problem 11

#1)
print('Problem 1) Create a = 0-92 and b = all ones')
a = np.arange(93)
b = np.ones(a.size)

print(a)
print(b)
print('\n\n')


#2)
print('Problem 2) Create 3x3 Array of \'True\'s')
c = np.full((3,3), True)

print(c)
print('\n\n')

#3)
print('Problem 3) Replpace odds in \'a\' with -1')
a[1::2] = -1

print(a)
print('\n\n')

#4)
print('Problem 4) Reshape \'a\' to a 2d array with 3 rows')
print(np.reshape(a,(3,-1)))
print('\n\n')

#5)
print('Problem 5) Stack \'a\' and \'b\' vertically')
print(np.vstack((a,b)))
print('\n\n')

#6)
print('Problem 6) Transpose a & b, then stack them horizontally')
print(np.hstack((a.T,b.T)))
print('\n\n')

#7)
print('Problem 7) Create c=np.array([1,2,3]) using only nunmpy functions')
c = np.arange(1,4)

print(np.append(np.repeat(c,3),np.tile(c,3)))
print('\n\n')

#8)
print('Problem 8) Get the common elements of two arrays')
d=np.array([1,2,3,2,3,4,3,4,5,6])
e=np.array([7,2,10,2,7,4,9,4,9,8])

print('Overlap of d and e where',end='\t')
print('e = ',e,end='\t')
print('d = ',d,end='\n')
print(np.intersect1d(d,e,assume_unique=False))
print('\n\n')

#9)
print('Problem 9) Remove all elements from d that are also in e')
print(np.setdiff1d(d,e,assume_unique=False))
#The above function returns a set, which I'm not sure is what the problem really wanted
#Numpy Arrays are 'immutable' so delete returns a totally new array
#Not sure if this is considered efficient
print(np.delete(d,np.where(np.isin(d,np.intersect1d(d,e)))))
print('\n\n')

#10)
print('Problem 10) Find the positions where e and d match')
print(np.where(e==d)[0])

print('\n\n')

#11)
print('Problem 11) let A=np.arange(9).reshape(3,3), swap column 1 and 3')
A = np.arange(9).reshape(3,3)
print('A = ')
print(A, end='\n\n')
'''
https://stackoverflow.com/questions/4857927/swapping-columns-in-a-numpy-array
I found multiple approaches to this one, the 2 most interestering were advanced slicing
or using the .copy() method, which is what I went with.

'''
A[:,0], A[:,2] = A[:,2], A[:,0].copy()
print(A)
print('\n\n')

#12)
print('Problem 12) swap the 1 and 3 rows of A')
print('A = ')
print(A, end='\n\n')
A[0,:],A[2,:] = A[2,:],A[0,:].copy()
print(A)
print('\n\n')

#13)
print('Problem 13) reverse all the rows of A')
print('A = ')
print(A,end='\n\n')
print(np.flip(A,1))
print('\n\n')

#14)
print('Problem 14) reverse all the columns of A')
print('A = ')
print(A,end='\n\n')
print(np.flip(A,0))
print('\n\n')

#15)
print('Problem 15) Create a 2D array (5x3) filled with rand numbers between [5,10)')
print((np.random.rand(5,3)*5)+5)
print('\n\n')

#16)
print('Problem 16) Find max,min,mean,median,std_dev,and var of a and A')
print('a =')
print(a)
print('max = {0}\t\tmin = {1}'.format(a.max(0),a.min(0)))
print('mean = {0}\tmedian = {1}'.format(a.mean(0),np.median(a)))
#The variance is also equal to std_dev**2, which I suspect would be faster, but the point is to use numpy
print('std_dev = {0}\tvariance = {1}\n'.format(a.std(0),a.var(0)))

print('A =')
print(A)
print('max = {0}\t\tmin = {1}'.format(np.amax(A),np.amin(A)))
print('mean = {0}\tmedian = {1}'.format(np.mean(A),np.median(A)))
print('std_dev = {0}\tvar = {1}'.format(np.std(A),np.var(A)))
print('\n\n')

#17)
print('Problem 17) Find max,min,mean,median,std_dev, and var of cols of A')
print(A)
print('max = {0}\t\tmin = {1}'.format(np.amax(A,axis=0),np.amin(A,axis=0)))
print('mean = {0}\tmedian = {1}'.format(np.mean(A,axis=0),np.median(A,axis=0)))
print('std_dev = {0}\tvar = {1}'.format(np.std(A,axis=0),np.var(A,axis=0)))
print('\n\n')


#18)
print('Problem 18) Find max,min,mean,median,std_dev, and var of rows of A')
# my instincts tell me to do the exact same as 17 but us A.T,
# let me know if that is slow for some reason
print(A)
print('max = {0}\t\tmin = {1}'.format(np.amax(A,axis=1),np.amin(A,axis=1)))
print('mean = {0}\tmedian = {1}'.format(np.mean(A,axis=1),np.median(A,axis=1)))
print('std_dev = {0}\tvar = {1}'.format(np.std(A,axis=1),np.var(A,axis=1)))
print('\n\n')

#19)
print('Problem 19) Find the position of the max value of A')
# modulus operator to be used if you need an ordered pair
print(A.argmax())
print('\n\n')

#20)
print('Problem 20) Find the 5th and 95th percentile scores in a')
print(np.percentile(a,5))
print(np.percentile(a,95))
print('\n\n')

#21)
print('Problem 21) create a function max_of_2')
def max_helper(x,y):
    if x>y: return x
    else: return y
max_of_2 = np.vectorize(max_helper)
print('testing function with arrays [5,5,5] and [1,5,8]')
print(max_of_2([5,5,5],[1,5,8]))
print('\n\n')

#22)
print('Problem 22) create a function to normalize an array between 0 & 1')
# is there any problems with this solution?
print(a)
print((a-min(a))/(max(a)-min(a)))
print('\n\n')

#23)
print('Problem 23) create a large array A, add 200 random nans, save as B')
A = np.random.rand(5000)
print(A)
mask = np.random.choice(5000,200,replace=False)
B = A
B[mask] = np.nan
#print(np.array_equal(A,B))
#False
print(B)
print('\n\n')

#24)
print('Problem 24) find the positions of nan in B')
print(np.argwhere(np.isnan(B)))
print('\n\n')

#25)
print('Problem 25) Select the rows in B that have a nan in them')

B = np.reshape(B,(500,10))
# Print all rows that have a nan
print(B[np.isnan(B).any(axis=1)])
# Print all rows that do not have a nan
print(B[~np.isnan(B).any(axis=1)])
print('\n\n')

#26)
print('Problem 26) replace all nan in B with a 0')
# Change all nan to 0, pos inf to max int and neg inf to min int
print(np.nan_to_num(B))
print('\n\n')

#27)
print('Problem 27) C = (100x100), filled with random between [0,1)')
print('Find rows where 3rd column > .5 and 7th column >= .75')
C = np.random.rand(100,100)
I = C[C[:,2] > 0.5]
I = I[I[:,6] >= 0.75]
print(I)
print('\n\n')

#28)
print('Problem 28) Correlate two columns of C')
# IMPORTANT NOTE:
# I do not understand what this means or if it's what you wanted.
print(np.correlate(C[:,0],C[:,1]))

#29)
print('Problem 29) Find the unique values in C')
# print(set(C.flat))
print(np.unique(C))
print('\n\n')

#30)
print('Problem 30) Find the 2nd and 5th largest values in C')
# I saw multiple ways to do this, best practice depends on use case I think
flat = C.flatten()
# couldn't get away from needing a new variable, sort returns NONE
flat.sort()
print(flat[-2])
# Using the other method to find 5th largest
# this is clever, but I'm not the one who thought to use it.
# Runs in O(n) at worst tho, while sorting is at least O(log(n))i
# since np defaults to quicksort it can be as bad as O(n^2), very bad
# leave as quicksort for random data tho, will be faster

# -5 in the argument is the index of the partition value
# if the array were sorted. -1 would be the largest in the array,
# 0 would be the smallest, etc.
print(np.partition(C.flatten(), -5)[-5])


