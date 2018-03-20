import numpy as np

# (a)
A = np.fromfunction(lambda x,y: x%y, (10,10))
print(A)

# (b)
B = 1/A
print(B)

# (c)
print('\n\n')
print('Max\n')
print(np.nanmax(B), end='\n\n')
print('Min\n')
print(np.nanmin(B), end='\n\n')
print('Column Max\n')
print(np.nanmax(B, axis=0), end='\n\n')
print('Column Min\n')
print(np.nanmin(B, axis=0), end='\n\n')



print('\n\n')
print('Max\n')
print(np.fmax(B), end='\n\n')
print('Min\n')
print(np.fmin(B), end='\n\n')
print('Column Max\n')
print(np.fmax(B, axis=0), end='\n\n')
print('Column Min\n')
print(np.fmin(B, axis=0), end='\n\n')


