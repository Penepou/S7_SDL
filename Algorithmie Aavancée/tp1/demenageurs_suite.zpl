
param fichier := "./u20_00.bpa";

param capacite := read fichier as "1n" comment "#" use 1 skip 1;
param nb_objets := read fichier as "2n" comment "#" use 1 skip 1;

set Objets := { 1 to nb_objets by 1 };
set Boites := { 1 to nb_objets by 1 };
set I := { 1 to nb_objets by 1 };

set tmp [ <i> in I ] := { read fichier as "<1n>" skip 1 + i use 1};
param taille [ <i> in I ] := ord ( tmp [ i ] ,1 ,1);

var x[Objets * Boites] binary;
var y[Boites] binary;

minimize nbBoites : sum<j> in Boites: y[j];
subto c1: forall<i> in Objets: sum<j> in Boites: x[i, j]==1;
subto c2 : forall<i> in Objets : forall<j> in Boites: x[i, j] <= y[j];
subto c3: forall<j> in Boites: sum<i> in Objets: taille[i]*x[i, j] <= capacite;

