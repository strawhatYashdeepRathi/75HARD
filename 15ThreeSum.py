# 3 Sum : Find triplets that add up to a zero
# Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.

# Pre-requisite: 2 Sum Problem

# Examples
# Example 1: 

# Input: nums = [-1,0,1,2,-1,-4]

# Output: [[-1,-1,2],[-1,0,1]]

def triplet(arr):
    n = len(arr)
    res = []
    arr.sort()
    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        l = i+1
        r = n-1
        while l < r:
            if arr[i]+arr[l]+arr[r] == 0:
                res.append([arr[i], arr[l], arr[r]])
                l+=1
                r-=1
                while l<r and arr[l] == arr[l-1]:
                    l+=1
                while l<r and arr[r] == arr[r+1]:
                    r-=1
            elif arr[i]+arr[l]+arr[r] < 0:
                l+=1
                while l<r and arr[l] == arr[l-1]:
                    l+=1
            else:
                r-=1
                while l<r and arr[r] == arr[r+1]:
                    r-=1
    return res


arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
ans = triplet(arr)
for it in ans:
    print("[", end="")
    for i in it:
        print(i, end=" ")
    print("]", end=" ")
print()