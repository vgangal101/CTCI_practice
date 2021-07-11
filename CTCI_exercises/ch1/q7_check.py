
# THIS IS A WRONG IMPLEMENTATION
# def rotate_matrix(matrix):
#     new_matrix = matrix.copy()
#
#     print(new_matrix)
#
#     for i in range(len(matrix)):
#         new_matrix[:][i] = matrix[i][:]
#     return new_matrix

# THE CORRECT SOLUTION

def rotate_matrix(matrix):
    # length along axis 0
    n = len(matrix)

    # There are n/2 layers, but remember to floor
    # in a 9 by 9 , there are 9//2 layers, i.e. 4
    for layer in range(n//2):
        first,last = layer, n - layer -1
        for i in range(first,last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i-1][layer]

            # bottom -> left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]

            #right -> bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]

            #top -> right
            matrix[i][-layer-1] = top

    return matrix





def main():
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]]

    #print("len(matrix)=",len(matrix))

    #new_matrix = rotate_matrix(matrix)


    print(matrix[:][0])

    #print("before:",matrix)

    #print("after:",new_matrix)


if __name__ == '__main__':
    main()
