SETI R9, #0 @ width
SETI R4, #0 @ height
SETI R7, #0 @ x
SETI R6, #0 @ y
SETI R8, #1
SETI R5, #0
SETI R3, #0 @neighbour

INVOKE 1, 9, 4
L4:
GOTO_GE L2, R7, R9
L1:
GOTO_GE L3, R6, R4
INVOKE 3, 7, 6 @move to the current cell
INVOKE 5, 3, 3
GOTO_NE L6, R3, R8
INVOKE 4, 8, 0
L6: 
ADD R6, R6, R8
GOTO L1
L3:
SET R6, R5
ADD R7, R7, R8
GOTO L4
L2:
	STOP
