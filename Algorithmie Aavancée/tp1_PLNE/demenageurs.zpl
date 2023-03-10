#Copyright (C) 2022 - Pénélope Delabrière, <penelope.delabriere@master-developpement-logiciel.fr>

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

set I := { 0 to 23 by 1 } ;
set J := { 0 to 23 by 1 } ;
param taille [ I ] := <0 > 6 , <1 > 6 , <2 > 5 , <3> 5, <4> 5, <5> 4, <6> 4, <7> 4, <8> 4, <9> 2, <10> 2, <11> 2, <12> 2, <13> 3, <14> 3, <15> 7, <16> 7, <17> 5, <18> 5, <19> 8, <20> 8, <21> 4, <22> 4, <23> 5; 
var x[I*J] binary;
var y[J] binary;
param capacite := 9;

minimize nb: sum<j> in J: y[j];
subto C1: forall <i> in I: sum<j> in J: x[i, j]==1;
subto C2: forall <j> in J: sum<i> in I: taille[i]*x[i, j] <= capacite;
subto C3: forall <i, j> in I*J: x[i, j] <= y[j];
