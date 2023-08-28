# 53. Maximum Subarray
#{     *******************     Kadane’s Algorithm : Maximum Subarray Sum in an Array          **********************     }

# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# Examples
# Example 1:

# Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output: 6 

# Explanation: [4,-1,2,1] has the largest sum = 6. 

# Examples 2: 

# Input: arr = [1] 

# Output: 1 

# Explanation: Array has only one element and which is giving positive sum of 1. 


def maxSubarraySum(nums, n):
    max_k = float('-inf')
    temp_sum = 0
    for i in range(n):
        temp_sum+=nums[i]
        if (temp_sum > max_k):
            max_k = temp_sum
        if(temp_sum < 0):
            temp_sum = 0
    return max_k





arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)
