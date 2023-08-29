# Search in a sorted 2D matrix
# Problem Statement: Given an m*n 2D matrix and an integer, write a program to find if the given integer exists in the matrix.

# Given matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row
# Example 1:

# Input: matrix = 
# [[1,3,5,7],
#  [10,11,16,20],
#  [23,30,34,60]], 

# target = 3

# Output: true

# Explanation: As the given integer(target) exists in the given 2D matrix, the function has returned true.


def search(matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    # i = 0
    # j = m-1
    # while i<n and j>=0:
    #     if (target == matrix[i][j]): return True          {   ********* for the problem which says all rows and columns sorted (refer GFG smilar problem)  **********    }
    #     elif (target < matrix[i][j]):
    #         j-=1
    #     else:
    #         i+=1
    # return False


    # {   *********       for problem that says all rows are sorted and first element of next row is greater than the last element of current row 
    #                                                                      (letcode problem) which makes it optimal for binary search        ************       }

    low = 0
    high = n*m -1
    while low <= high:
        mid = low + (high-low)//2
        if target == matrix[mid//m][mid%m]: return True
        if (target < matrix[mid//m][mid%m]):
            high = mid - 1
        else:
            low = mid + 1
    return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 30
    ans = search(matrix, target)

    print(ans)
    
