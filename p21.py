from mpi4py import MPI
import numpy as np

'''
The only changes I would make at this point are
1) passing the size in as an argument so that the user gets to decide
-- already did the second one, so it's a bit faster now probably
2) counting the number of failures instead of successes
'''
size = 10**6
count = 0
ans = 0

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

for i in range(comm.Get_size()):
    if rank == i:
        data = np.random.rand(size,2)

# count = np.where(((data[:,1]**2+data[:,0]**2) <= 1))[0].size
count = np.where(((data[:,1]**2+data[:,0]**2) > 1))[0].size

if rank != 0:
    comm.send(count,dest=0)

if rank == 0:
    ans += count
    for i in range(1,comm.Get_size()):
        count = comm.recv(source=i)
        #print('recv %d'%count)
        ans += count
    #print((ans*4)/(size*comm.Get_size()))
    #print(ans)
    print(((size*comm.Get_size()-ans)*4)/(size*comm.Get_size()))
