#Copyright (C) 2022 - Pénélope Delabrière, <penelope.delabriere@master-developpement-logiciel.fr>

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

# Une instance de sac a dos simple à 12 objets numérotés de 0 à 11

param capacite := 20;
set Objets := { 0 to 11 by 1 } ;
param poids[Objets] :=
	<0> 11, <1> 7, <2> 5, <3> 5, <4> 4, <5> 3, <6> 3, <7> 2, <8> 2, <9> 2, <10> 2, <11> 1;
param valeurs[Objets] :=
	<0> 20, <1> 10, <2> 25, <3> 11, <4> 5, <5> 50, <6> 15, <7> 12, <8> 6 , <9> 5, <10> 4, <11> 30;
var x[Objets] binary;

maximize valeur : sum<i> in Objets: valeurs[i] * x[i];
subto poids : sum<i> in Objets: poids[i] * x[i] <= capacite;
# subto domain : forall<i> in Objets : 0 <= x[i] <= 1 ;
