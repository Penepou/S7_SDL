from mpi4py import MPI
import sys

#On suppose que le processus 0 possède deux vecteurs X et Y de même longueur N, dont il veut faire le produit scalaire X.Y . X, Y et N ne sont connus que par le processus 0

#Donner l’algorithme parallèle MPI pour paralléliser le produit scalaire sur P processeurs.

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

def split(x, size):
	n = len(x)//size
	if len(x)%size!=0:
		n+=1
	return [x[n*i:n*(i+1)] for i in range(size)]
	
if rank == 0:
	x = split([1, 2, 3], size)
	y = split([10, 20, 30], size)
	print("rank = 0, x=", x, " y=", y)

else:
	x = None
	y = None

x_local = comm.scatter(x, root=0)
y_local = comm.scatter(y, root=0)

if rank == 0:
	print("rank = 0, x=", x, " y=", y)
	
print(rank, "x_local=", x_local, " y_local=", y_local)
res = 0

for i in range(len(x_local)):
	res+=x_local[i]*y_local[i]

res = comm.reduce(res, op=MPI.SUM, root=0)

test = comm.gather(x_local, root=0)
if rank == 0:
	print("resultat=", res)
	print("gather=", test)
