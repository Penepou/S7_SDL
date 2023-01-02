import random
import numpy as np
from math import *
import copy 

def random_solution(p):
	temp=[]
	for i in range(p):
		temp.append(random.randint(0, 1))
	return temp
	
def somme_bits(vector):
	sol=0
	for i in vector:
		sol+=i
	return sol

def readSquareMatrix(file_m):
	matrix=[]
	with open(file_m) as f:
		linestring= [int(x) for x in next(f).split()]
		n = linestring.pop(0)
		p = linestring.pop(0)
		for x in range(n):
			line=[]
			for y in range(n):
				line.append(linestring[y+x*n])
			matrix.append(line)
	return matrix, n, p

def solve_f(Q, temp):
	n=len(temp)
	solution=0
	for i in range(n):
		for j in range(n):
			solution+=Q[i][j]*temp[i]*temp[j]
	return solution
	
def voisins(vector):
	voisins= []
	sol=vector
	for i in range(len(vector)):
		sol[i]=1-vector[i]
		voisins.append(copy.copy(sol))
		sol[i]=1-vector[i]
	return voisins

def meilleur_voisin(Q, voisins):
	meilleur=voisins[0]
	sol=[]
	for i in voisins:
		if solve_f(Q, meilleur) > solve_f(Q, i):
			meilleur = i
	sol.append(meilleur)
	for i in voisins:
		if solve_f(Q, meilleur) == solve_f(Q, i) and meilleur!=i:
			sol.append(i)
	return sol[random.randint(0, len(sol)-1)]

def steepest_Hill_Climbing(Q, max_depl):
	s = random_solution(len(Q[0]))
	nb_depl=0
	stop=False
	while(nb_depl<max_depl and not(stop)):
		ss = meilleur_voisin(Q, voisins(s))
		if solve_f(Q, s) > solve_f(Q, ss):
			s = ss
		else:
			stop = True
		nb_depl+=1
	return s, solve_f(Q, s)


def steepest_Hill_Climbing_redemarrage(Q, max_depl, max_essais, p):
	meilleur=None
	for _ in range(max_essais):
		s = random_solution(len(Q[0]))
		nb_depl=0
		stop=False
		while(nb_depl<max_depl and not(stop)):
			ss = meilleur_voisin(Q, voisins(s))
			if solve_f(Q, s) > solve_f(Q, ss) and somme_bits(ss)>=p:
				s = ss
			else:
				stop = True
			nb_depl+=1
		if meilleur==None or solve_f(Q, meilleur) > solve_f(Q, s):
			meilleur=s
	return meilleur, solve_f(Q, meilleur)


def voisins_non_tabou(tabou, vector):
	voisins= []
	n = len(vector)
	sol=vector
	for i in range(len(vector)):
		sol[i]=1-vector[i]
		if vector not in tabou:
			voisins.append(copy.copy(sol))
		sol[i]=1-vector[i]
	return voisins

	
def tabou(Q, max_depl, taille_tabou):
	s = random_solution(len(Q[0]))
	tabou = []
	nb_depl = 0
	msol = s
	stop = False
	while nb_depl < max_depl and not(stop):
		voisins = voisins_non_tabou(tabou, s)
		if voisins !=[]:
			ss = meilleur_voisin(Q, voisins)
		else:
			stop=True
		if len(tabou)==taille_tabou:
			tabou.pop(0)
		tabou.append(s)
	
		if solve_f(Q, ss) < solve_f(Q, msol):
			msol = ss
		s = ss
		nb_depl+=1
	return msol, solve_f(Q, msol)
	
max_depl = 20
max_essais=10

Q1, n1, p1 = readSquareMatrix('partition6.txt')
Q2, n2, p2 = readSquareMatrix('graphe12345.txt')

#Exercice 1

#print(voisins([1, 0, 0, 1]))
#print(steepest_Hill_Climbing(Q1, max_depl))
#print(steepest_Hill_Climbing(Q2, max_depl))

#print(steepest_Hill_Climbing_redemarrage(Q2, max_depl, max_essais, p2))
#print(steepest_Hill_Climbing_redemarrage(Q2, matrix, max_depl, p2, max_essais))

print(tabou(Q1, 20, 10))
