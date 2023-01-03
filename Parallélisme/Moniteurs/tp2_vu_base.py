import sys
import os
import time
import random
from multiprocessing import Process, Lock, Condition, Value, Array

class Road:
	def __init__(self):
		self.nbVoitures = Value('i', 0)
		self.currentSens = Value('i', -1)
		self.lock = Lock()
		self.direction0 = Condition(self.lock)
		self.direction1 = Condition(self.lock)
        
	def enter_road(self, direction):
		with self.lock:
			while self.nbVoitures.value!=0 and self.currentSens.value==1-direction:
				if direction:
					self.direction1.wait()
				else:
					self.direction0.wait()
			self.nbVoitures.value+=1
			self.currentSens.value=direction
			if direction:
				self.direction1.notify()
			else:
				self.direction0.notify()

	def exit_road(self, direction):
		with self.lock:
			self.nbVoitures.value-=1
			if direction:
				if self.nbVoitures.value==0:
					self.direction0.notify()
			else:
				if self.nbVoitures.value==0:
					self.direction1.notify()

def drive(road_type, direction, identifier):
	print("Vehicule %d, coming from %d goes through the %s" % (identifier, direction, road_type))
	time.sleep(random.random())

def vehicule(nb_times, direction, road):
	identifier = os.getpid()
	random.seed(identifier)
	for i in range(nb_times):
		drive("Double road", direction, identifier)
		road.enter_road(direction)
		print("Vehicule %d, coming from %d enters the small road" % (identifier, direction))
		drive("Small road", direction, identifier)
		road.exit_road(direction)
		print("Vehicule %d, coming from %d exits the small road" % (identifier, direction))
	print("Vehicule %d, coming from %d finishes" % (identifier, direction))
        
if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("Usage : %s <Nb vehicules sens O> <Nb vehicules sens 1> <Nb passages sur VU>" % sys.argv[0]);
		sys.exit(1)

	nb_vehicules = [int(sys.argv[1]), int(sys.argv[2])]
	nb_times = int(sys.argv[3])
    
	road = Road()

	processes = []
	for v in range(nb_vehicules[0]):
		v0 = Process(target=vehicule, args=(nb_times, 0, road))
		v0.start()
		processes.append(v0)

	for v in range(nb_vehicules[1]):
		v1 = Process(target=vehicule, args=(nb_times, 1, road))
		v1.start()
		processes.append(v1)
        


	for process in processes:
		process.join()
