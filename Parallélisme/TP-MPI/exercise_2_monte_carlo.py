# -----------------------------------------------------------
# (C) 2022 Pénélope Delabrière, Toulouse, France
# Released under GNU Affero General Public License v3.0 (AGPLv3)
# -----------------------------------------------------------

#! /usr/bin/python3

#With 1 process : 3.2671592235565186  seconds
#With 2 processes : 1.695228576660156 seconds
#With 4 processes :  0.9725539684295654 seconds

from mpi4py import MPI

import time
import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

nb = 10000001 // size
inside = 0

random.seed(rank)

start_time = time.time()

for _ in range(nb):
	x = random.random()
	y = random.random()
	if x*x + y*y <= 1:
		inside +=1
end_time = time.time()

print("rank =", rank, "inside=", inside, " in ", end_time-start_time, " seconds")
res=comm.reduce(inside, op=MPI.SUM, root=0)
if rank==0:
	res = (res*size)//nb
	print("Pi =", 4 * res, "in ", end_time-start_time, 'seconds')
