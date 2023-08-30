
# Length of the longest subarray with zero Sum
# Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.

# Examples
# Example 1:
# Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
# Result: 5
# Explanation: The following subarrays sum to zero:
# {-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
# Since we require the length of the longest subarray, our answer is 5!



def Large0Sum(arr, n):
    hashh = {}
    res = 0
    summ = 0
    for i in range(n):
        summ+=arr[i]
        if summ == 0:
            res = i + 1
        elif summ in hashh:
            test = i-hashh[summ]
            res = max(res, test)
        else:
            hashh[summ] = i
    return res







a = [9, -3, 3, -1, 6, -5]
ans = Large0Sum(a, len(a))
print("The longest consecutive sequence is", ans)