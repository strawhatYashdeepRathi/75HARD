# Program to generate Pascal’s Triangle

# Example 1:
# Input Format: N = 5, r = 5, c = 3
# Result: 6 (for variation 1)
# 1 4 6 4 1 (for variation 2)

# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1 
# 1 4 6 4 1    (for variation 3)

# Explanation: There are 5 rows in the output matrix. Each row is formed using the logic of Pascal’s triangle.

# Example 2:
# Input Format: N = 1, r = 1, c = 1
# Result: 1 (for variation 1)
#     1 (for variation 2)
#     1  (for variation 3)
# Explanation: The output matrix has only 1 row.


def generateRow(n):
    test = 1
    ans = [1]
    for j in range(1, n):
        test = test * (n-j)
        test = test//j
        ans.append(test)
    return ans



def pascalTriangle(n):
    res = []
    for i in range(1, n+1):
        res.append(generateRow(i))
    return res



if __name__ == '__main__':
    n = 5
    ans = pascalTriangle(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()