# -----------------------------------------------------------
# (C) 2022 Pénélope Delabrière, Toulouse, France
# Released under GNU Affero General Public License v3.0 (AGPLv3)
# -----------------------------------------------------------

param fichier := "./shift-scheduling-1.zplread" ;
do print fichier ;

####################
# Horizon = nb days

param horizon := read fichier as "2n" comment "#" match "^h";
do print "horizon : ", horizon, " jours" ;


############################################
# Sets of days, week-ends, services, staff :

set Days := {0..horizon-1} ;
# All instances start on a Monday
# planning horizon is always a whole number of weeks (h mod 7 = 0)
set WeekEnds := {1..horizon/7} ;
do print card(WeekEnds), " week-ends :" ;
do print WeekEnds ;

set Services := { read fichier as "<2s>" comment "#" match "^d" } ;
do print card(Services), " services" ; 

set Personnes := { read fichier as "<2s>" comment "#" match "^s" } ;
do print card(Personnes) , " personnels" ;

############
# Parameters

param duree[Services] := read fichier as "<2s> 3n" comment "#" match "^d";
# do forall <t> in Services  do print "durée ", t, " : ", duree[t] ;

param ForbiddenSeq[Services*Services] :=
	read fichier as "<2s,3s> 4n" comment "#"  match "c" default 0 ;


param MaxTotalMinutes[Personnes] :=
  read fichier as "<2s> 3n" comment "#" match "^s"  ;
param MinTotalMinutes[Personnes] :=
  read fichier as "<2s> 4n" comment "#" match "^s"  ;
param MaxConsecutiveShifts[Personnes] :=
  read fichier as "<2s> 5n" comment "#" match "^s"  ;
param MinConsecutiveShifts[Personnes] :=
  read fichier as "<2s> 6n" comment "#" match "^s"  ;
param MinConsecutiveDaysOff[Personnes] :=
  read fichier as "<2s> 7n" comment "#" match "^s"  ;
param MaxWeekends[Personnes] :=
  read fichier as "<2s> 8n" comment "#" match "^s"  ;

param MaxShift[Personnes*Services] :=
  read fichier as "<2s,3s> 4n" comment "#" match "^m" default 0 ;

param requirement[Days*Services] :=
  read fichier as "<2n,3s> 4n" comment "#" match "^r" ;

param belowCoverPen[Days*Services] :=
  read fichier as "<2n,3s> 5n" comment "#" match "^r" ;

param aboveCoverPen[Days*Services] :=
  read fichier as "<2n,3s> 6n" comment "#" match "^r" ;

param dayOff[Personnes*Days] :=
  read fichier as "<2s,3n> 4n" comment "#" match "^f" default 0 ;

# penalité si jour "pas off" = "on"
param prefOff[Personnes*Days*Services] :=
  read fichier as "<2s,3n,4s> 5n" comment "#" match "^n" default 0 ;

# penalité si jour "pas on" = "off"
param prefOn[Personnes*Days*Services] :=
  read fichier as "<2s,3n,4s> 5n" comment "#" match "^y" default 0 ;

# do print "Services" ;
# do forall <s> in Services do print s, duree[s] ;
# do forall <s1,s2> in Services*Services with ForbiddenSeq[s1,s2] == 1
#   do print s1, s2, ForbiddenSeq[s1,s2] ;
# do print "Staff" ; 
# do forall <p> in Personnes
#   do print p, MaxTotalMinutes[p], MinTotalMinutes[p],
#     MaxConsecutiveShifts[p], MinConsecutiveShifts[p],
#     MinConsecutiveDaysOff[p], MaxWeekends[p] ;
# do print "Days Off" ;
# do forall<p,d> in Personnes * Days with dayOff[p,d] == 1 do print p,d,dayOff[p,d] ;
# do print "Pref Shifts On" ;
# do forall<p,d,s> in Personnes * Days * Services
#   with prefOn[p,d,s] >= 1 do print p,d,s,prefOn[p,d,s] ;
# do print "Pref Shifts Off" ;
# do forall<p,d,s> in Personnes * Days * Services
#   with prefOff[p,d,s] >= 1 do print p,d,s,prefOff[p,d,s] ;
# do print "Cover" ;
# do forall<d,s> in Days * Services
#   do print d,s,requirement[d,s], belowCoverPen[d,s], aboveCoverPen[d,s] ;

###########
var assigned[Personnes*Days*Services] binary;
var below[Days*Services] >= 0;
var above[Days*Services] >= 0;
var work[Personnes*Days] binary;

# minimize Obj : sum<d,s> in Days*Services : (below[d,s] + above[d,s]);

minimize Obj : sum<d,s> in Days*Services : (belowCoverPen[d,s] * below[d,s] + aboveCoverPen[d,s] * above[d,s]) + sum<p,d,s> in Personnes*Days*Services : (prefOff[p,d,s] * assigned[p,d,s] + prefOn[p,d,s] * (1 - assigned[p,d,s]));

subto work : forall<p,d> in Personnes*Days : (sum<s> in Services : assigned[p,d,s]) == work[p,d];

subto C1 : forall<d,s> in Days*Services : (sum<p> in Personnes : assigned[p,d,s]) + below[d,s] - above[d,s] == requirement[d,s];

subto C21 : forall<p,d> in Personnes*Days : (sum<s> in Services : assigned[p,d,s]) <= 1;

subto C22 : forall<p,d> in Personnes*Days: if dayOff[p,d] == 1 then (sum<s> in Services : assigned[p,d,s]) == 0 end;

subto C23 : forall<p,s> in Personnes*Services : (sum<d> in Days : assigned[p,d,s]) <= MaxShift[p,s];

subto C24 : forall<p> in Personnes : (sum<d,s> in Days*Services: duree[s] * assigned[p,d,s]) <= MaxTotalMinutes[p] and (sum<d,s> in Days*Services: duree[s] * assigned[p,d,s]) >= MinTotalMinutes[p];

subto C31 : forall<p> in Personnes : forall<j> in {0..max(Days)-MaxConsecutiveShifts[p]} : sum<k> in {j..j+MaxConsecutiveShifts[p]} : work[p,k] <= MaxConsecutiveShifts[p];

subto C32 : forall<p,d,s1,s2> in Personnes*Days*Services*Services with d < max(Days) and ForbiddenSeq[s1,s2] == 1 : assigned[p,d,s1] + assigned[p,d+1,s2] <= 1;

subto C421 : forall<p> in Personnes : forall<k> in {2..MinConsecutiveDaysOff[p]} : forall<j> in {0..max(Days)-k} : (work[p,j] + work[p,j+k] - 1) <= (sum<n> in {j+1..j+k-1} : work[p,n]);

subto C412 : forall<p> in Personnes with MinConsecutiveShifts[p] > 1 : forall<k> in {2..MinConsecutiveShifts[p]} : forall<j> in {0..max(Days)-k} : (work[p,j] + work[p,j+k]) >= sum<n> in {j+1..j+k-1} : (work[p,n]-k+2);
