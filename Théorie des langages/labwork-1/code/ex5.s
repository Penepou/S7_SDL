SETI R9, #0 @ width
SETI R4, #0 @ height
SETI R7, #0 @ x
SETI R6, #0 @ y
SETI R8, #1 @invariant
SETI R5, #0 @invariant
SETI R3, #0 @current
SETI R2, #1 @index neighbour
SETI R0, #0 @neighbour

INVOKE 1, 9, 4
L4:
GOTO_GE L2, R7, R9 @ parcours des lignes
L1:
GOTO_GE L3, R6, R4 @ parcours des colonnes
INVOKE 3, 7, 6 @move to the current cell
INVOKE 5, 3, 0 @récupère la valeur du current cell
GOTO_EQ L6, R3, R5 @ si égal à 1 on set à 0
INVOKE 4, 5, 0 
GOTO L7 @passage à une autre cellule
L6:
INVOKE 5, 0, 1
GOTO_EQ L8, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L8:
INVOKE 5, 0, 2
GOTO_EQ L9, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L9:
INVOKE 5, 0, 3
GOTO_EQ L10, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L10:
INVOKE 5, 0, 4
GOTO_EQ L11, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L11:
INVOKE 5, 0, 5
GOTO_EQ L12, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L12:
INVOKE 5, 0, 6
GOTO_EQ L13, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L13:
INVOKE 5, 0, 7
GOTO_EQ L14, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
GOTO L7
L14:
INVOKE 5, 0, 8
GOTO_EQ L7, R0, R5 
INVOKE 4, 8, 0	@ met à 1 la cellule courante
L7:
ADD R6, R6, R8
GOTO L1 @limite parcours colonne
L3:
SET R6, R5
ADD R7, R7, R8
GOTO L4 @limite parcours ligne
L2:
STOP
