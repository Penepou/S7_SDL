import random
import sys
import time
import numpy as np
from math import *
import copy 

def read(file_m):
	array = []
	with open(file_m) as f:
		Lines = f.readlines()
		Lines.pop(0)
	for line in Lines:
		ff = line.split('\t')
		nb = int(ff[0])
		x = int(ff[1])
		y = int(ff[2].split('\n')[0])
		array.append((nb, x, y))
	return array

def random_solution(file_m):
	countries = read(file_m)
	solution = []
	while len(countries)>0:
		s = random.randint(0, len(countries)-1)
		solution.append(countries.pop(s))
	return solution
	
def liste_villes(solution):
	villes = []
	for s in solution:
		villes.append(s[0])
	return villes

def liste_villes_tabou(tabou):
	temp = []
	for sol in tabou:
		temp.append(liste_villes(sol))
	return temp
	
def euclidian_distance(v, w):
	return sqrt((v[1]-w[1])**2 + (v[2]-w[2])**2)

def distance(solution):
	distance=0
	x=(-1, 0, 0)
	for country in solution:
		distance+=euclidian_distance(x, country)
		x=country
	distance+=euclidian_distance(x, (-1, 0, 0))
	return distance

def voisins_non_tabou(solution, tabou):
	voisins = []
	for i in range(len(solution)):
		for j in range(len(solution)):
			s = solution.copy()
			temp = s[i]
			s[i]=s[j]
			s[j] = temp
			if s not in voisins and s not in tabou:
				voisins.append(s)
	voisins.remove(solution)
	return voisins

def voisins(solution):
	voisins = []
	for i in range(len(solution)):
		for j in range(len(solution)):
			s = solution.copy()
			temp = s[i]
			s[i]=s[j]
			s[j] = temp
			if s not in voisins:
				voisins.append(s)
	voisins.remove(solution)
	return voisins

def meilleur_voisin(voisins):
	msol = voisins[random.randint(0, len(voisins)-1)]
	for v in voisins:
		if distance(v) < distance(msol):
			msol = v.copy()
	return msol

def steepest_Hill_Climbing(file_m, max_depl):
	init = random_solution(file_m)
	s = init.copy()
	nb_depl=0
	stop=False
	while(nb_depl<max_depl and not(stop)):
		ss = meilleur_voisin(voisins(s))
		if distance(s) > distance(ss):
			s = ss.copy()
		else:
			stop = True
		nb_depl+=1
	print("- solution initiale : ", liste_villes(init))
	print("- solution atteinte : ", liste_villes(s))
	print("- nombre de déplacement parcouru : ", nb_depl)
	return s, distance(s), init, nb_depl

def steepest_Hill_Climbing_redemarrage(file_m, max_depl, max_essais):
	meilleur=None
	for i in range(max_essais):
		print("\nESSAI N°", i)
		msol, d, init, nb_depl = steepest_Hill_Climbing(file_m, max_depl)
		if meilleur==None or distance(meilleur) > d:
			meilleur=msol.copy()
	return meilleur, distance(meilleur)

def tabou(file_m, max_depl, taille_tabou):
	init = random_solution(file_m)
	s = init.copy()
	tabou = []
	nb_depl = 0
	msol = s.copy()
	stop = False
	while nb_depl < max_depl and not(stop):
		voisins = voisins_non_tabou(s, tabou)
		if voisins !=[]:
			ss = meilleur_voisin(voisins)
		else:
			stop=True
		if len(tabou)==taille_tabou:
			tabou.pop(0)
		tabou.append(s)
	
		if distance(ss) < distance(msol):
			msol = ss.copy()
		s = ss.copy()
		nb_depl+=1
	return msol, distance(msol), init, nb_depl, tabou, s

if __name__ == '__main__':
	if len(sys.argv) != 5:
		print("Usage: python3 exercice2.py <file_name> <max_depl> <max_essais> <taille_tabou>")
		sys.exit(1)

	file_m = sys.argv[1]
	max_depl = int(sys.argv[2])
	max_essais = int(sys.argv[3])
	taille_tabou = int(sys.argv[4])
	
	print("\t\t\t--------- STEEPEST HILL CLIMBING ---------")
	start = time.time()
	s, d, init, nb_depl = steepest_Hill_Climbing(file_m, max_depl)
	end = time.time()
	print("- distance de la meilleure solution : ", d)
	print("- temps effectué : ", end - start, " sec")

	print("\n\n\t\t--------- STEEPEST HILL CLIMBING REDEMARRAGE ---------")
	start = time.time()
	meilleur, d = steepest_Hill_Climbing_redemarrage(file_m, max_depl, max_essais)
	end = time.time()
	print("\n")
	print("meilleure solution rencontrée : ", liste_villes(meilleur))
	print("distance de la solution : ", d)
	print("temps effectué : ", end - start, " sec")
	
	print("\n\n\t\t--------- TABOU ---------")
	start = time.time()
	msol, d, init, nb_depl, tabou, s = tabou(file_m, max_depl, taille_tabou)
	end = time.time()
	print("solution initiale : ", liste_villes(init))
	print("solution atteinte : ", liste_villes(s))
	print("meilleure solution rencontrée : ", liste_villes(msol))
	print("distance de la solution : ", d)
	print("nombre de déplacement parcouru : ", nb_depl)
	print("liste tabou = ", liste_villes_tabou(tabou))
	print("temps effectué : ", end - start, " sec")
	
