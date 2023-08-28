
# Rotate Image by 90 degree
# Problem Statement: Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

# Note: Rotate matrix 90 degrees anticlockwise

# Examples
# Example 1:

# Input: [[1,2,3],[4,5,6],[7,8,9]]

# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.


def rotate(List):
    n = len(List)

    for i in range(n):
        for j in range(i):
            List[i][j], List[j][i] = List[j][i], List[i][j]
    for i in range(n):
        List[i].reverse()




if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(arr)
    print("Rotated Image")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()

