
# Trapping Rainwater
# Problem Statement: Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain.

# Examples:

# Example 1:

# Input: height= [0,1,0,2,1,0,1,3,2,1,2,1]

# Output: 6

def trap(arr):
    l, r = 0, len(arr) - 1
    maxL, maxR = arr[l], arr[r]
    ans = 0
    while l<r:
        if maxL<maxR:
            l+=1
            maxL = max(maxL, arr[l])
            ans+= maxL - arr[l]
        else:
            r-=1
            maxR = max(maxR, arr[r])
            ans+= maxR - arr[r]
    return ans


if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")