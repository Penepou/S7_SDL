# -----------------------------------------------------------
# (C) 2022 Pénélope Delabrière, Toulouse, France
# Released under GNU Affero General Public License v3.0 (AGPLv3)
# -----------------------------------------------------------

from mpi4py import MPI
import sys
import time

def nb_primes(n):
    result = 0
    for i in range(1, n+1):
        if n%i == 0:
            result += 1
    return result

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = int(sys.argv[1])
result = 0

start_time = time.time()
tmp = 0
#2nd version
#rank = 1  in  82.1809332370758  seconds
#rank = 0  in  83.26623296737671  seconds
#rank = 2  in  83.50528478622437  seconds
#rank = 3  in  83.84841823577881  seconds

for i in range(rank+1, N+1, size):
	tmp = nb_primes(i)
	result = max(result, tmp)
end_time = time.time()

print("rank =", rank," in ", end_time-start_time, " seconds")

current_max = comm.reduce(result, op=MPI.MAX, root=0)
if rank == 0:
	print(current_max)
'''
# 1st version
#rank = 0  in  16.37393879890442  seconds
#rank = 1  in  50.802985429763794  seconds
#rank = 2  in  88.55555391311646  seconds
#rank = 3  in  124.54378080368042  seconds

for i in range(rank* N//size+1, (rank+1)* N//size +1):
	tmp = nb_primes(i)
	result = max(tmp, result)
end_time = time.time()

print("rank =", rank," in ", end_time-start_time, " seconds")
current_max = comm.reduce(result, op=MPI.MAX, root=0)

if rank == 0:
	print(current_max)
'''
