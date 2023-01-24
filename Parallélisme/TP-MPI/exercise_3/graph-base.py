# -----------------------------------------------------------
# (C) 2022 Pénélope Delabrière, Toulouse, France
# Released under GNU Affero General Public License v3.0 (AGPLv3)
# -----------------------------------------------------------

from matplotlib import pyplot as plt
from mpi4py import MPI
import networkx as nx

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

def plot_graph(graph, save=False, display=True):
    g1=graph
    plt.tight_layout()
    nx.draw_networkx(g1, arrows=True)
    if save:
        plt.savefig("graph.png", format="PNG")
    if display:
        plt.show(block=True)


#graph = nx.scale_free_graph(20).reverse()
graph = nx.gnr_graph(30, .01).reverse()
#graph = nx.random_k_out_graph(20, 2, .8).reverse()

if rank==0:
	new_elements = [0]
	old_elements = []
else:
	new_elements = None
	old_elements = None

verif = True

#while len(new_elements) != 0: 
while(verif):
	old_elements_local = comm.bcast(old_elements, root=0)
	new_elements_local = comm.scatter(new_elements, root=0)
	tmp = []

	for node_src in new_elements_local:
		for node in graph.neighbors(node_src):
			if not node in old_elements_local and not node in new_elements_local and not node in tmp:
				tmp.append(node)

	old_elements_local += new_elements_local
	new_elements_local = tmp
	old_elements = comm.gather(old_elements_local, root=0)
	new_elements = comm.gather(new_elements_local, root=0)

	if rank==0:
		printf("neighbors:")
		for node_neigh in old_elements:
			print(node_neigh)
		printf("news:")
		for node_new in new_elements:
			print(node_new)
		print(len(old_elements) == len(graph))
		
		#if len(old_elements) == len(graph):
		verif = False

	verif = comm.broadcast(verif, root=0)
plot_graph(graph, save=True, display=True)
