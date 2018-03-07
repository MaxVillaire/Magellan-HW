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










