#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
  newmatrix = []
  for row in matrix:
    newmatrix.append([row[i] * row[i] for i in range(len(row))])
  return newmatrix
