#Copyright (C) 2022 - Pénélope Delabrière, <penelope.delabriere@master-developpement-logiciel.fr>

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

import time
import random
import sys
from multiprocessing import Process, Lock, Condition, Value, Array


### Monitor start
class Buffer:
	def __init__(self, nb_cases, proch_type):
		self.nb_cases = nb_cases
		self.nb_cases_vides = Value('i', nb_cases)
		self.storage_val = Array('i',[-1] * nb_cases, lock=False)
		self.storage_type = Array('i',[-1] * nb_cases, lock=False)
		self.ptr_prod = Value('i', 0)
		self.ptr_cons = Value('i', 0)
		self.lock = Lock()
		self.lockDepot = Lock()
		self.estVide0 = Condition(self.lock)
		self.estVide1 = Condition(self.lock)
		self.estPlein=Condition(self.lock)

	def produce(self, msg_val, msg_type, msg_source):
		with self.lock:
			while(self.nb_cases_vides.value<2) :
				self.estPlein.wait()
			position = self.ptr_prod.value
			self.storage_val[position] = msg_val
			self.storage_type[position] = msg_type
			self.ptr_prod.value = (position + 1) % self.nb_cases
			print('%3d produced %3d (type:%d) in place %3d and the buffer is\t\t %s' %
			(msg_source, msg_val, msg_type, position, self.storage_val[:]))
			self.nb_cases_vides.value-=1;
			if(self.nb_cases_vides.value==self.nb_cases-1):
				if msg_type==0:
					self.estVide0.notify()
				else:
					self.estVide1.notify()

	def consume(self, id_cons):
		with self.lock:
			while(self.nb_cases_vides.value==self.nb_cases or id_cons%2 !=self.storage_type[self.ptr_cons.value]) :
				if id_cons%2==0:
					self.estVide0.wait()
				else:
					self.estVide1.wait()
			position = self.ptr_cons.value
			result = self.storage_val[position]
			result_type = self.storage_type[position]
			self.storage_val[position] = -1
			self.storage_type[position] = -1
			self.ptr_cons.value = (position + 1) % self.nb_cases
			print('\t%3d consumed %3d (type:%d) in place %3d and the buffer is\t %s' %
			(id_cons, result, result_type, position, self.storage_val[:]))
			self.nb_cases_vides.value+=1
			if self.nb_cases_vides.value!=self.nb_cases:
				if self.storage_type[self.ptr_cons.value]==0:
					self.estVide0.notify()
				else:
					self.estVide1.notify()
			if self.nb_cases_vides.value>=2:
				self.estPlein.notify()
		return result
#### Monitor end

def producer(msg_val, msg_type, msg_source, nb_times, buffer):
	for _ in range(nb_times):
		time.sleep(.1 + random.random())
		buffer.produce(msg_val, msg_type, msg_source)
		msg_val += 1

def consumer(id_cons, nb_times, buffer):
	for _ in range(nb_times):
		with buffer.lockDepot:
			time.sleep(.5 + random.random())
			buffer.consume(id_cons)

if __name__ == '__main__':
	if len(sys.argv) != 6:
		print("Usage: %s <Nb Prod <= 20> <Nb Conso <= 20> <Nb Cases <= 20> <nb_times_prod> <nb_times_cons>" % sys.argv[0])
		sys.exit(1)

	nb_prod = int(sys.argv[1])
	nb_cons = int(sys.argv[2])
	nb_cases = int(sys.argv[3])

	nb_times_prod = int(sys.argv[4])
	nb_times_cons = int(sys.argv[5])

	buffer = Buffer(nb_cases, 0)
    
	producers, consumers = [], []
    
	for id_prod in range(nb_prod):
		msg_val_start, msg_type, msg_source = id_prod * nb_times_prod, id_prod % 2, id_prod
		prod = Process(target=producer, args=(msg_val_start, msg_type, msg_source, nb_times_prod, buffer))
		prod.start()
		producers.append(prod)

	for id_cons in range(nb_cons):
		cons=Process(target=consumer, args=(id_cons, nb_times_cons, buffer))
		cons.start()
		consumers.append(cons)

	for prod in producers:
		prod.join()

	for cons in consumers:
		cons.join()
