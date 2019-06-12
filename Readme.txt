Guarini's  puzzle involves four knights, two white and two black, at the four corners of a small 3x3 chessboard.
The puzzle is to exchange the places of the white knights and the black knights.This problem can be solved very easily using graph theory.

The code will check if it is possile to move the knights from any cell configuration to another configuration 
(no knight will be in the middle cell) and also give number of moves needed to reach the final configuration via shortest path.
The idea is - one configuraion can be reached from another configuration if they are part of the same connected component.
The code is written using NetworkX python library.

codefile -->config2config
supportingfile -->nx_pylab
