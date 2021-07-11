import os
import sys

def zero_matrix(matrix):
    zero_arr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zero_arr.append((i,j))

    for pair in zero_arr:
        x = pair[0]
        y = pair[1]

        matrix[x] = [0 for j in range(len(matrix[0]))]

        for i in range(len(matrix)):
            matrix[i][y] = 0

    return matrix




#matrix = [[1,2,3,4],[1,0,3,4],[1,2,3,0],[0,4,5,9],[1,2,3,4]]

matrix =[[1, 2, 3, 4, 0],
         [6, 0, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]]

expected  = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]]


altered_matrix = zero_matrix(matrix)

print("altered_matrix == matrix", matrix == expected)
