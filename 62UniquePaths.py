# Grid Unique Paths | Count paths from left-top to the right bottom of a matrix
# Problem Statement: Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell you can either only move to the rightward direction or the downward direction.

# Example 1:

# Input Format: m = 2, n= 2
# Output: 2



#     {                  DP with recursion                   }
# def recursive(i, j, n, m, dp):
#     if(i == n-1 and j == m-1):
#         return 1
#     if (i>=n or j>=m):
#         return 0
#     if (dp[i][j] != -1):
#         return dp[i][j]
#     else:
#         dp[i][j] = recursive(i+1, j, n, m, dp) + recursive(i, j+1, n, m, dp)
#         return dp[i][j]


# def uniquePaths(m, n):
#     dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
#     nums = recursive(0, 0, m, n, dp)
#     if m == 1 and n == 1:
#         return nums
#     return dp[0][0]

def uniquePaths(m, n):
    ways = m+n-2
    # rights = n-1
    downs = m-1
    #       we need either ways C rights or ways C downs
    res = 1
    for i in range(1, downs + 1):
        res = res * (ways - downs + i)/i
    return int(res)



if __name__ == "__main__":
    totalCount = uniquePaths(3, 7)
    print("The total number of Unique Paths are ", totalCount)

