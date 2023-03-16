#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

	matrix_1 = []
	if len(matrix) > 0:
	    for i in matrix:
		matrix_1.append(list(map(lamda x: x ** 2, i)))

	return matrix_1
