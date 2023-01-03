import sys
import time
import random
from multiprocessing import Process, Lock, Condition, Value, Array

class ExtendedCondition:
	def __init__(self, nb_isoloirs):
		self.lock = Lock()
		self.accesIsoloir= Condition(self.lock)
		self.nbIsoloirsOccupes = Value('i', 0)

	def entrer_isoloir(self, prio):
		with self.lock:
			if prio:
				while self.nbIsoloirsOccupes.value == nb_isoloirs:
					self.accesIsoloir.wait(0)
			else:
				while self.nbIsoloirsOccupes.value == nb_isoloirs:
					self.accesIsoloir.wait(1)
			self.nbIsoloirsOccupes.value+=1

	def sortir_isoloir(self):
		with self.lock:
			self.nbIsoloirsOccupes.value-=1
			self.accesIsoloir.notify()

def process_electeur(id_elec, synchro, ratio):
	prio = id_elec%ratio==0
	time.sleep(.1 + random.random())
	if prio:
		print("electeur handicapé ", id_elec, "est arrivé à la mairie")
	else:
		print("electeur ", id_elec, "est arrivé à la mairie")
	synchro.entrer_isoloir(prio)
	if prio:
		print("electeur handicapé ", id_elec, "est entré dans l'isoloir")
	else:
		print("electeur ", id_elec, "est entré dans l'isoloir")
	time.sleep(.1 + random.random())    
	print("electeur", id_elec, "vient de sortir")        
	synchro.sortir_isoloir()
        
if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage: %s <Nb electeurs> <Nb isoloirs> <Ratio>\n" % sys.argv[0])
		sys.exit(1)

	nb_electeurs = int(sys.argv[1])
	ratio = int(sys.argv[3])
	nb_isoloirs = int(sys.argv[2])

	synchro = ExtendedCondition(nb_isoloirs)

    # To initialize the common data
	processes = []
	for id_elec in range(nb_electeurs):
		electeur = Process(target=process_electeur, args=(id_elec, synchro, ratio))
		electeur.start()
		processes.append(electeur)

	for process in processes:
		process.join()
