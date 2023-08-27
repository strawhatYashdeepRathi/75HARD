# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.
# Examples 1:

# Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]

# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.

# Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0

def zeroMatrix(matrix, n, m):
    col0 = 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    if matrix[0][0] == 0:
        for j in range(n):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(m):
            matrix[i][0] = 0
    return matrix



if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    m = len(matrix)
    n = len(matrix[0])
    ans = zeroMatrix(matrix, n, m)

    print("The Final matrix is:")
    for row in ans:
        for ele in row:
            print(ele, end=" ")
        print()
